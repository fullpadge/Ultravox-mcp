#!/bin/bash
# ============================================================================
# QUICK GITHUB DEPLOY - Ultra Simple Version
# ============================================================================

clear
echo "╔════════════════════════════════════════════════════════════════════╗"
echo "║                                                                    ║"
echo "║        ULTRAVOX MCP → GITHUB DEPLOYMENT (QUICK VERSION)          ║"
echo "║                                                                    ║"
echo "╚════════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -f "src/server.py" ]; then
    echo "${RED}❌ Error: Run this script from the project directory!${NC}"
    echo ""
    echo "Usage:"
    echo "  cd /path/to/ultravox-mcp-unofficial"
    echo "  ./QUICK_DEPLOY.sh"
    exit 1
fi

echo "${BLUE}📋 Step 1: GitHub Information${NC}"
echo "─────────────────────────────────────"
echo ""
read -p "Your GitHub username: " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "${RED}❌ Username cannot be empty!${NC}"
    exit 1
fi

echo ""
echo "${BLUE}📋 Step 2: Git Configuration${NC}"
echo "─────────────────────────────────────"
echo ""

read -p "Your Git name (e.g., 'Sebastien'): " GIT_NAME
read -p "Your Git email: " GIT_EMAIL

if [ -z "$GIT_NAME" ] || [ -z "$GIT_EMAIL" ]; then
    echo "${RED}❌ Name and email cannot be empty!${NC}"
    exit 1
fi

echo ""
echo "${GREEN}✅ Configuration:${NC}"
echo "   GitHub User: $GITHUB_USER"
echo "   Git Name: $GIT_NAME"
echo "   Git Email: $GIT_EMAIL"
echo ""

# ============================================================================
# SECURITY CHECK
# ============================================================================

echo "${BLUE}🔒 Step 3: Security Check${NC}"
echo "─────────────────────────────────────"
echo ""

if [ -f ".env" ]; then
    echo "${RED}⚠️  WARNING: .env file found!${NC}"
    echo "   This WILL NOT be committed (protected by .gitignore)"
    echo "   But you should review it for security."
    echo ""
fi

if grep -r "api_key\|API_KEY" src/ --include="*.py" 2>/dev/null | grep -v "os.getenv\|environ" | grep -v ".env"; then
    echo "${RED}⚠️  WARNING: Potential hardcoded secrets found!${NC}"
    read -p "   Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "${RED}❌ Aborted!${NC}"
        exit 1
    fi
fi

echo "${GREEN}✅ Security check passed!${NC}"
echo ""

# ============================================================================
# GIT SETUP
# ============================================================================

echo "${BLUE}⚙️  Step 4: Git Setup${NC}"
echo "─────────────────────────────────────"
echo ""

if [ ! -d ".git" ]; then
    echo "Initializing Git..."
    git init
    echo "${GREEN}✅ Git initialized${NC}"
else
    echo "${GREEN}✅ Git already initialized${NC}"
fi

echo "Configuring Git user..."
git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"
echo "${GREEN}✅ Git configured${NC}"

echo ""

# ============================================================================
# STAGING
# ============================================================================

echo "${BLUE}📦 Step 5: Stage Files${NC}"
echo "─────────────────────────────────────"
echo ""

git add .
echo "${GREEN}✅ Files staged${NC}"

echo ""

# ============================================================================
# COMMIT
# ============================================================================

echo "${BLUE}💾 Step 6: Create Commit${NC}"
echo "─────────────────────────────────────"
echo ""

COMMIT_MSG="Initial commit: Ultravox MCP v1.0.0 - Unofficial by Mak3it.org"
git commit -m "$COMMIT_MSG"
echo "${GREEN}✅ Commit created${NC}"

echo ""

# ============================================================================
# GITHUB SETUP
# ============================================================================

echo "${BLUE}🔗 Step 7: GitHub Setup${NC}"
echo "─────────────────────────────────────"
echo ""

echo "You need to create the repository on GitHub first!"
echo ""
echo "Follow these steps:"
echo "  1. Go to: https://github.com/new"
echo "  2. Repository name: ultravox-mcp-unofficial"
echo "  3. Description: Unofficial Ultravox MCP Server by Mak3it.org"
echo "  4. Public: ✓ (check)"
echo "  5. Initialize with README: ✗ (uncheck)"
echo "  6. Click 'Create repository'"
echo ""

read -p "Press Enter when you're done creating the repository..."

echo ""

# ============================================================================
# GET GITHUB URL
# ============================================================================

echo "${BLUE}🔌 Step 8: Add Remote${NC}"
echo "─────────────────────────────────────"
echo ""

read -p "Paste your GitHub repository URL: " GITHUB_URL

if [ -z "$GITHUB_URL" ]; then
    echo "${RED}❌ URL cannot be empty!${NC}"
    exit 1
fi

echo "Adding remote..."
if git remote get-url origin &>/dev/null; then
    git remote remove origin
fi

git remote add origin "$GITHUB_URL"
echo "${GREEN}✅ Remote added${NC}"

echo ""

# ============================================================================
# PUSH
# ============================================================================

echo "${BLUE}🚀 Step 9: Push to GitHub${NC}"
echo "─────────────────────────────────────"
echo ""

echo "Setting main branch..."
git branch -M main

echo "Pushing to GitHub..."
echo "(You may be asked to authenticate)"
echo ""

if git push -u origin main; then
    echo ""
    echo "${GREEN}✅ Pushed successfully!${NC}"
else
    echo ""
    echo "${RED}❌ Push failed!${NC}"
    echo "Make sure you:"
    echo "  1. Created the repository on GitHub"
    echo "  2. Have the correct URL"
    echo "  3. Have GitHub authentication set up"
    exit 1
fi

echo ""

# ============================================================================
# SUCCESS
# ============================================================================

echo "╔════════════════════════════════════════════════════════════════════╗"
echo "║                                                                    ║"
echo "║                  🎉 SUCCESS! 🎉                                  ║"
echo "║                                                                    ║"
echo "║            Your GitHub Repository is Live!                       ║"
echo "║                                                                    ║"
echo "╚════════════════════════════════════════════════════════════════════╝"
echo ""

echo "${GREEN}Repository Details:${NC}"
echo "  URL:    $GITHUB_URL"
echo "  Branch: main"
echo "  Status: Live on GitHub ✅"
echo ""

echo "${GREEN}Next Steps:${NC}"
echo "  1. ⭐ Visit and Star your repository!"
echo "  2. 📢 Share on Twitter/Reddit"
echo "  3. 📖 Check that README looks good"
echo "  4. 🧪 Test the documentation"
echo "  5. 💬 Monitor Issues & Discussions"
echo ""

echo "${GREEN}Links:${NC}"
echo "  Repository: $GITHUB_URL"
echo "  Issues:     ${GITHUB_URL}/issues"
echo "  Docs:       ${GITHUB_URL}/tree/main/docs"
echo ""

echo "${BLUE}Questions? Contact:${NC}"
echo "  Email: hello@mak3it.org"
echo "  Website: https://mak3it.org"
echo ""

echo "═════════════════════════════════════════════════════════════════════"
