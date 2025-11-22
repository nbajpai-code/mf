# Mental Food - Setup Guide

## Automated Content Discovery Setup

### Prerequisites
- GitHub repository with Actions enabled
- YouTube Data API v3 key (free tier)

### Step 1: Get YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to "APIs & Services" → "Library"
4. Search for "YouTube Data API v3"
5. Click "Enable"
6. Go to "Credentials" → "Create Credentials" → "API Key"
7. Copy your API key
8. (Optional) Restrict the key to YouTube Data API v3 only

### Step 2: Add GitHub Secret

1. Go to your repository on GitHub
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. Name: `YOUTUBE_API_KEY`
5. Value: Paste your YouTube API key
6. Click "Add secret"

### Step 3: Verify Workflow

1. Go to "Actions" tab in your repository
2. You should see "Update Mental Food Content" workflow
3. Click "Run workflow" to test manually
4. Check the workflow run for any errors

### Step 4: Review Pull Requests

When the workflow finds new content:
1. It will create a PR titled "🧠 Weekly Mental Food Update"
2. Review the suggested content
3. Merge if quality is good
4. Close if not relevant

## Configuration

Edit `scripts/config.yaml` to customize:

```yaml
keywords:
  ai_ml:
    - "your custom keywords"
  
quality:
  youtube:
    min_views: 10000  # Adjust threshold
    max_age_days: 90  # How recent
```

## Troubleshooting

### Workflow Not Running
- Check if GitHub Actions are enabled
- Verify cron schedule in `.github/workflows/update-content.yml`

### API Quota Exceeded
- YouTube API has daily quota (10,000 units)
- Reduce search frequency or keywords in config

### No Content Found
- Lower quality thresholds in `config.yaml`
- Add more search keywords
- Increase `max_age_days`

## Manual Run

To run the discovery script locally:

```bash
cd scripts
pip install -r requirements.txt
export YOUTUBE_API_KEY="your-key-here"
python discover_content.py
```

## API Costs

All APIs used are **FREE**:
- YouTube Data API v3: 10,000 units/day (plenty for weekly runs)
- arXiv API: No limits
- Hacker News API: No limits
