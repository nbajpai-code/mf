# 🚀 Quick Start: Enable Automated Content Discovery

Follow these steps to enable weekly automated content updates for your Mental Food repository.

## Step 1: Get YouTube API Key (5 minutes)

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create or Select Project**
   - Click the project dropdown at the top
   - Click "New Project" or select existing
   - Name it "mental-food" (or any name)

3. **Enable YouTube Data API v3**
   - Click "☰" menu → "APIs & Services" → "Library"
   - Search for "YouTube Data API v3"
   - Click on it, then click "Enable"

4. **Create API Key**
   - Go to "APIs & Services" → "Credentials"
   - Click "+ CREATE CREDENTIALS" → "API key"
   - Copy the API key (starts with `AIza...`)
   - Click "Restrict Key" (recommended)
     - Under "API restrictions", select "Restrict key"
     - Choose "YouTube Data API v3"
     - Click "Save"

## Step 2: Add Secret to GitHub (2 minutes)

1. **Go to Repository Settings**
   - Navigate to: https://github.com/nbajpai-code/mf
   - Click "Settings" tab

2. **Add Secret**
   - Click "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `YOUTUBE_API_KEY`
   - Secret: Paste your API key from Step 1
   - Click "Add secret"

## Step 3: Test the Workflow (1 minute)

1. **Manual Trigger**
   - Go to "Actions" tab
   - Click "Update Mental Food Content" workflow
   - Click "Run workflow" dropdown
   - Click green "Run workflow" button

2. **Monitor Progress**
   - Watch the workflow run in real-time
   - Should complete in 1-2 minutes
   - Check for any errors

3. **Review Results**
   - If content found, a PR will be created
   - Review the PR titled "🧠 Weekly Mental Food Update"
   - Merge if quality looks good!

## ✅ You're Done!

The workflow will now run automatically every Monday at 9 AM UTC.

## 📊 What to Expect

- **Weekly PRs**: New content suggestions every Monday
- **Quality Filtered**: Only high-quality content from trusted sources
- **Manual Review**: You approve before merging
- **Zero Maintenance**: Runs automatically in the background

## 🔧 Customization (Optional)

Edit `scripts/config.yaml` to customize:

```yaml
# Adjust quality thresholds
quality:
  youtube:
    min_views: 5000  # Lower for more content
    max_age_days: 180  # Older content

# Add your favorite channels
trusted_channels:
  - "Your Favorite Channel"
```

## ❓ Troubleshooting

### No PR Created
- Workflow might not have found new content meeting criteria
- Check workflow logs in Actions tab
- Try lowering quality thresholds in config

### API Quota Exceeded
- YouTube API has 10,000 units/day (plenty for weekly runs)
- If exceeded, wait 24 hours or reduce search keywords

### Workflow Failed
- Check if `YOUTUBE_API_KEY` secret is set correctly
- Verify API key is valid and not restricted incorrectly
- Check workflow logs for specific error

## 📞 Need Help?

Open an issue on GitHub with:
- Workflow run URL
- Error message (if any)
- What you've tried

---

**Ready to go!** 🎉 Your Mental Food repository is now a living, self-updating knowledge base!
