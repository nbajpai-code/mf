#!/usr/bin/env python3
"""
Mental Food Content Discovery Script

Automatically discovers new high-quality technical content from:
- YouTube (technical talks)
- arXiv (research papers)
- Hacker News (trending posts)
"""

import os
import sys
import yaml
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re

try:
    from googleapiclient.discovery import build
    import arxiv
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Error importing required libraries: {e}")
    print("Please install requirements: pip install -r requirements.txt")
    sys.exit(1)


class ContentDiscovery:
    def __init__(self, config_path: str = "scripts/config.yaml"):
        """Initialize content discovery with configuration."""
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.youtube_api_key = os.getenv('YOUTUBE_API_KEY')
        self.new_content = {
            'videos': [],
            'papers': [],
            'articles': []
        }
    
    def discover_youtube_content(self) -> List[Dict]:
        """Discover new technical talks from YouTube."""
        if not self.youtube_api_key:
            print("⚠️  YouTube API key not found, skipping YouTube discovery")
            return []
        
        print("🔍 Searching YouTube for new content...")
        youtube = build('youtube', 'v3', developerKey=self.youtube_api_key)
        
        videos = []
        keywords = self.config['keywords']['ai_ml'] + self.config['keywords']['engineering']
        
        # Calculate date threshold
        days_ago = self.config['quality']['youtube']['max_age_days']
        published_after = (datetime.now() - timedelta(days=days_ago)).isoformat() + 'Z'
        
        for keyword in keywords[:5]:  # Limit to avoid API quota
            try:
                request = youtube.search().list(
                    part='snippet',
                    q=keyword,
                    type='video',
                    order='viewCount',
                    publishedAfter=published_after,
                    maxResults=5,
                    videoDuration='medium',  # 4-20 minutes
                    relevanceLanguage='en'
                )
                response = request.execute()
                
                for item in response.get('items', []):
                    video_id = item['id']['videoId']
                    
                    # Get video statistics
                    stats_request = youtube.videos().list(
                        part='statistics,contentDetails',
                        id=video_id
                    )
                    stats_response = stats_request.execute()
                    
                    if stats_response['items']:
                        stats = stats_response['items'][0]['statistics']
                        view_count = int(stats.get('viewCount', 0))
                        
                        # Check quality threshold
                        if view_count >= self.config['quality']['youtube']['min_views']:
                            videos.append({
                                'title': item['snippet']['title'],
                                'url': f"https://www.youtube.com/watch?v={video_id}",
                                'channel': item['snippet']['channelTitle'],
                                'views': view_count,
                                'published': item['snippet']['publishedAt']
                            })
                
            except Exception as e:
                print(f"Error searching YouTube for '{keyword}': {e}")
                continue
        
        # Filter by trusted channels
        trusted_videos = [
            v for v in videos 
            if any(channel.lower() in v['channel'].lower() 
                   for channel in self.config['trusted_channels'])
        ]
        
        print(f"✅ Found {len(trusted_videos)} high-quality YouTube videos")
        return trusted_videos[:self.config['limits']['max_items_per_category']]
    
    def discover_arxiv_papers(self) -> List[Dict]:
        """Discover new research papers from arXiv."""
        print("🔍 Searching arXiv for new papers...")
        
        papers = []
        keywords = self.config['keywords']['ai_ml']
        
        for keyword in keywords[:3]:  # Limit searches
            try:
                search = arxiv.Search(
                    query=keyword,
                    max_results=10,
                    sort_by=arxiv.SortCriterion.SubmittedDate
                )
                
                for result in search.results():
                    # Check if paper is recent
                    days_old = (datetime.now() - result.published.replace(tzinfo=None)).days
                    
                    if days_old <= self.config['quality']['arxiv']['max_age_days']:
                        papers.append({
                            'title': result.title,
                            'url': result.entry_id,
                            'authors': [author.name for author in result.authors],
                            'published': result.published.strftime('%Y-%m-%d'),
                            'summary': result.summary[:200] + '...'
                        })
                        
            except Exception as e:
                print(f"Error searching arXiv for '{keyword}': {e}")
                continue
        
        # Remove duplicates by title
        unique_papers = {p['title']: p for p in papers}.values()
        papers = list(unique_papers)
        
        print(f"✅ Found {len(papers)} recent arXiv papers")
        return papers[:self.config['limits']['max_items_per_category']]
    
    def discover_hackernews_content(self) -> List[Dict]:
        """Discover trending technical content from Hacker News."""
        print("🔍 Searching Hacker News for trending content...")
        
        try:
            # Get top stories
            response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
            story_ids = response.json()[:50]  # Top 50 stories
            
            articles = []
            for story_id in story_ids:
                story_response = requests.get(
                    f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
                )
                story = story_response.json()
                
                if story and story.get('score', 0) >= self.config['quality']['hackernews']['min_score']:
                    # Check if it's technical content
                    title = story.get('title', '').lower()
                    keywords = ['ai', 'ml', 'engineering', 'programming', 'software', 'tech', 'algorithm']
                    
                    if any(kw in title for kw in keywords) and story.get('url'):
                        articles.append({
                            'title': story['title'],
                            'url': story['url'],
                            'score': story['score'],
                            'comments': story.get('descendants', 0)
                        })
                
                if len(articles) >= self.config['limits']['max_items_per_category']:
                    break
            
            print(f"✅ Found {len(articles)} trending HN articles")
            return articles
            
        except Exception as e:
            print(f"Error fetching Hacker News content: {e}")
            return []
    
    def format_content_for_markdown(self) -> str:
        """Format discovered content as markdown."""
        content = []
        
        if self.new_content['videos']:
            content.append("\n### 🆕 Recently Discovered Talks\n")
            for video in self.new_content['videos']:
                content.append(
                    f"#### [{video['title']}]({video['url']})\n"
                    f"- **Channel**: {video['channel']}\n"
                    f"- **Views**: {video['views']:,}\n"
                    f"- **Why**: High-quality technical content from trusted source\n\n"
                )
        
        if self.new_content['papers']:
            content.append("\n### 📄 Recent Research Papers\n")
            for paper in self.new_content['papers']:
                authors = ', '.join(paper['authors'][:3])
                if len(paper['authors']) > 3:
                    authors += ' et al.'
                content.append(
                    f"#### [{paper['title']}]({paper['url']})\n"
                    f"- **Authors**: {authors}\n"
                    f"- **Published**: {paper['published']}\n"
                    f"- **Summary**: {paper['summary']}\n\n"
                )
        
        if self.new_content['articles']:
            content.append("\n### 🔥 Trending Technical Content\n")
            for article in self.new_content['articles']:
                content.append(
                    f"#### [{article['title']}]({article['url']})\n"
                    f"- **HN Score**: {article['score']} | **Comments**: {article['comments']}\n\n"
                )
        
        return ''.join(content)
    
    def update_mf_file(self, new_content_md: str):
        """Append new content to mf.md file."""
        mf_path = 'mf.md'
        
        if not os.path.exists(mf_path):
            print(f"❌ Error: {mf_path} not found")
            return
        
        with open(mf_path, 'r') as f:
            current_content = f.read()
        
        # Add new content before the footer
        footer_marker = "---\n\n**Last Updated**:"
        
        if footer_marker in current_content:
            parts = current_content.split(footer_marker)
            updated_content = (
                parts[0] + 
                new_content_md + 
                "\n" + footer_marker + 
                parts[1]
            )
        else:
            # Append at the end if no footer found
            updated_content = current_content + "\n" + new_content_md
        
        # Update the timestamp
        today = datetime.now().strftime('%Y-%m-%d')
        updated_content = re.sub(
            r'\*\*Last Updated\*\*: \d{4}-\d{2}-\d{2}',
            f'**Last Updated**: {today}',
            updated_content
        )
        
        with open(mf_path, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Updated {mf_path} with new content")
    
    def run(self):
        """Run the content discovery process."""
        print("🧠 Starting Mental Food Content Discovery...\n")
        
        # Discover content from all sources
        self.new_content['videos'] = self.discover_youtube_content()
        self.new_content['papers'] = self.discover_arxiv_papers()
        self.new_content['articles'] = self.discover_hackernews_content()
        
        # Check if we found any new content
        total_items = (
            len(self.new_content['videos']) + 
            len(self.new_content['papers']) + 
            len(self.new_content['articles'])
        )
        
        if total_items == 0:
            print("\n📭 No new content found matching quality criteria")
            return
        
        print(f"\n🎉 Discovered {total_items} new items!")
        
        # Format and update mf.md
        new_content_md = self.format_content_for_markdown()
        self.update_mf_file(new_content_md)
        
        print("\n✨ Content discovery complete!")


if __name__ == "__main__":
    discovery = ContentDiscovery()
    discovery.run()
