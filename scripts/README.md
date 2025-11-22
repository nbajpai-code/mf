# scripts/

This directory contains automation scripts for the Mental Food repository.

## Files

### `discover_content.py`
Main content discovery script that:
- Searches YouTube for technical talks
- Queries arXiv for research papers
- Scrapes Hacker News for trending content
- Filters by quality criteria
- Updates `mf.md` with new content

### `requirements.txt`
Python dependencies needed for content discovery:
- `google-api-python-client` - YouTube API
- `arxiv` - arXiv API wrapper
- `requests` - HTTP requests
- `beautifulsoup4` - Web scraping
- `python-dotenv` - Environment variables
- `PyYAML` - Configuration parsing

### `config.yaml`
Configuration file for content discovery:
- Search keywords by category
- Quality thresholds (views, citations, scores)
- Trusted sources (channels, authors)
- Content limits per run

## Usage

### Local Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export YOUTUBE_API_KEY="your-key-here"

# Run discovery
python discover_content.py
```

### GitHub Actions
The script runs automatically via `.github/workflows/update-content.yml`:
- Scheduled: Every Monday at 9 AM UTC
- Manual: Via GitHub Actions UI

## Configuration

Edit `config.yaml` to customize:

```yaml
keywords:
  ai_ml:
    - "artificial intelligence"
    - "machine learning"
    # Add your keywords

quality:
  youtube:
    min_views: 10000
    max_age_days: 90
```

## Output

The script:
1. Discovers content from multiple sources
2. Filters by quality criteria
3. Formats as markdown
4. Appends to `mf.md`
5. Updates "Last Updated" timestamp

## Error Handling

- Gracefully handles API failures
- Skips sources if API keys missing
- Logs all operations
- Returns non-zero exit code on critical errors
