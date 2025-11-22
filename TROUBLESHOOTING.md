# Fixing GitHub Actions PR Creation Permission Issue

## The Problem
GitHub Actions workflows using `GITHUB_TOKEN` cannot create pull requests due to security restrictions. This prevents the automated content discovery workflow from creating PRs.

## The Solution
We have two options:

### Option 1: Use Personal Access Token (PAT) - Recommended
1. Create a fine-grained PAT with PR permissions
2. Add it as a repository secret
3. Workflow will use PAT to create PRs

### Option 2: Enable Workflow Permissions (Simpler but less secure)
1. Go to repository Settings → Actions → General
2. Under "Workflow permissions", select "Read and write permissions"
3. Check "Allow GitHub Actions to create and approve pull requests"
4. Save

## Quick Fix Steps (Option 2 - Recommended for personal repos)

1. **Go to Repository Settings**
   - Navigate to: https://github.com/nbajpai-code/mf/settings/actions

2. **Update Workflow Permissions**
   - Scroll to "Workflow permissions"
   - Select: ✅ "Read and write permissions"
   - Check: ✅ "Allow GitHub Actions to create and approve pull requests"
   - Click "Save"

3. **Re-run the Workflow**
   - Go to Actions tab
   - Click "Update Mental Food Content"
   - Click "Re-run all jobs"

## Alternative: Create PAT (Option 1 - More secure)

If you prefer using a PAT:

1. **Create Fine-Grained PAT**
   - Go to: https://github.com/settings/tokens?type=beta
   - Click "Generate new token"
   - Name: "Mental Food Automation"
   - Repository access: Only select repositories → nbajpai-code/mf
   - Permissions:
     - Contents: Read and write
     - Pull requests: Read and write
   - Generate token and copy it

2. **Add as Repository Secret**
   - Go to: https://github.com/nbajpai-code/mf/settings/secrets/actions
   - Click "New repository secret"
   - Name: `PAT_TOKEN`
   - Value: Paste your PAT
   - Click "Add secret"

3. **Workflow Already Updated**
   - The workflow now tries PAT_TOKEN first, falls back to GITHUB_TOKEN
   - No additional changes needed

## Which Option to Choose?

- **Option 2 (Workflow Permissions)**: Simpler, good for personal repositories
- **Option 1 (PAT)**: More secure, better for team/organization repositories

For your personal repo, **Option 2 is recommended** - just enable the permissions in settings.
