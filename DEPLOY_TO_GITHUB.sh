#!/bin/bash
# ============================================================================
# Ultravox MCP - GitHub Deployment Script
# Automated setup and push to GitHub
# ============================================================================

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════════════╗"
echo "║                                                                    ║"
echo "║    ULTRAVOX MCP - GITHUB DEPLOYMENT AUTOMATION                   ║"
echo "║    Unofficial by Mak3it.org                                      ║"
echo "║                                                                    ║"
echo "╚════════════════════════════════════════════════════════════════════╝"
echo ""

# ============================================================================
# STEP 1: Collect Information
# ============================================================================

echo "📋 STEP 1: GitHub Configuration"
echo "════════════════════════════════════"
echo ""

read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter your GitHub email: " GITHUB_EMAIL
read -p "Enter repository name (default: ultravox-mcp-unofficial): " REPO_NAME
REPO_NAME=${REPO_NAME:-ultravox-mcp-unofficial}

read -p "Enter project directory path (default: ./ultravox-mcp-unofficial): " PROJECT_DIR
PROJECT_DIR=${PROJECT_DIR:-./ultravox-mcp-unofficial}

# Verify project exists
if [ ! -d "$PROJECT_DIR" ]; then
    echo "❌ Error: Directory '$PROJECT_DIR' not found!"
    exit 1
fi

echo ""
echo "✅ Configuration:"
echo "   GitHub User:    $GITHUB_USERNAME"
echo "   GitHub Email:   $GITHUB_EMAIL"
echo "   Repo Name:      $REPO_NAME"
echo "   Project Dir:    $PROJECT_DIR"
echo ""

# ============================================================================
# STEP 2: Setup Git Configuration
# ============================================================================

echo "⚙️  STEP 2: Git Setup"
echo "════════════════════════════════════"
echo ""

cd "$PROJECT_DIR"

# Check if git is already initialized
if [ -d ".git" ]; then
    echo "ℹ️  Git already initialized, skipping..."
else
    echo "Initializing Git repository..."
    git init
    echo "✅ Git initialized"
fi

# Configure git user
echo "Configuring Git user..."
git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_EMAIL"
echo "✅ Git user configured"

echo ""

# ============================================================================
# STEP 3: Security Check
# ============================================================================

echo "🔒 STEP 3: Security Verification"
echo "════════════════════════════════════"
echo ""

# Check if .env exists (should NOT!)
if [ -f ".env" ]; then
    echo "⚠️  WARNING: .env file found in repository!"
    echo "   This file will NOT be committed (protected by .gitignore)"
    read -p "   Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Aborted!"
        exit 1
    fi
fi

# Verify .gitignore exists
if [ ! -f ".gitignore" ]; then
    echo "⚠️  WARNING: .gitignore not found!"
    echo "   Creating .gitignore..."
    cat > .gitignore << 'GITIGNORE'
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
ENV/
env/

# Testing
.pytest_cache/
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
GITIGNORE
    echo "✅ .gitignore created"
else
    echo "✅ .gitignore found"
    if grep -q ".env" ".gitignore"; then
        echo "✅ .env is protected in .gitignore"
    else
        echo "⚠️  WARNING: .env not in .gitignore!"
    fi
fi

echo ""

# ============================================================================
# STEP 4: Check for Secrets
# ============================================================================

echo "🔍 STEP 4: Secret Scanning"
echo "════════════════════════════════════"
echo ""

echo "Scanning for potential secrets..."

FOUND_SECRETS=0

# Check Python files
if grep -r "ULTRAVOX_API_KEY\s*=" src/ --include="*.py" 2>/dev/null | grep -v "os.getenv\|environ" | grep -v ".env"; then
    echo "⚠️  WARNING: Potential hardcoded API key in Python files!"
    FOUND_SECRETS=1
fi

# Check for common secret patterns
if grep -r "api_key\|API_KEY\|password\|PASSWORD\|secret\|SECRET" . \
    --include="*.py" --include="*.json" --include="*.yml" --include="*.yaml" \
    --exclude-dir=.git --exclude-dir=venv --exclude=".env*" 2>/dev/null | \
    grep -v "^\s*#\|os.getenv\|environ\|\.env\.example\|CONTRIBUTING\|README\|LICENSE"; then
    echo "⚠️  Found potential secrets. Review manually."
    FOUND_SECRETS=1
fi

if [ $FOUND_SECRETS -eq 0 ]; then
    echo "✅ No hardcoded secrets detected!"
else
    echo "⚠️  Please review secrets before pushing!"
    read -p "   Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Aborted!"
        exit 1
    fi
fi

echo ""

# ============================================================================
# STEP 5: Stage Files
# ============================================================================

echo "📦 STEP 5: Staging Files"
echo "════════════════════════════════════"
echo ""

# Check git status
echo "Current git status:"
git status --short | head -20

echo ""
echo "Adding all files..."
git add .

echo "✅ Files staged"
echo ""

# ============================================================================
# STEP 6: Create Initial Commit
# ============================================================================

echo "💾 STEP 6: Initial Commit"
echo "════════════════════════════════════"
echo ""

COMMIT_MSG="Initial commit: Ultravox MCP v1.0.0 - Unofficial by Mak3it.org"

echo "Creating commit with message:"
echo "  '$COMMIT_MSG'"
echo ""

git commit -m "$COMMIT_MSG"

echo "✅ Commit created"
echo ""

# ============================================================================
# STEP 7: GitHub Instructions
# ============================================================================

echo "🔗 STEP 7: GitHub Setup Instructions"
echo "════════════════════════════════════"
echo ""

echo "⚠️  IMPORTANT: You must create the repository on GitHub first!"
echo ""
echo "Follow these steps:"
echo ""
echo "1️⃣  Go to: https://github.com/new"
echo ""
echo "2️⃣  Fill in the form:"
echo "   Repository name: $REPO_NAME"
echo "   Description: Unofficial Ultravox MCP Server by Mak3it.org"
echo "   Public: ✓"
echo "   Initialize with README: ✗ (leave unchecked)"
echo ""
echo "3️⃣  Click 'Create repository'"
echo ""
echo "4️⃣  Copy the repository URL from GitHub"
echo ""
echo "5️⃣  Come back here and run:"
echo "   git remote add origin <YOUR_GITHUB_URL>"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

read -p "Have you created the repository on GitHub? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Please create the repository first: https://github.com/new"
    exit 1
fi

echo ""

# ============================================================================
# STEP 8: Add Remote
# ============================================================================

echo "🔌 STEP 8: Add GitHub Remote"
echo "════════════════════════════════════"
echo ""

read -p "Enter your GitHub repository URL (https://github.com/...): " GITHUB_URL

if [ -z "$GITHUB_URL" ]; then
    echo "❌ Error: Repository URL cannot be empty!"
    exit 1
fi

# Remove existing remote if it exists
if git remote get-url origin &>/dev/null; then
    echo "Removing existing remote..."
    git remote remove origin
fi

echo "Adding remote origin..."
git remote add origin "$GITHUB_URL"

echo "Verifying remote..."
git remote -v

echo "✅ Remote added"
echo ""

# ============================================================================
# STEP 9: Push to GitHub
# ============================================================================

echo "🚀 STEP 9: Push to GitHub"
echo "════════════════════════════════════"
echo ""

echo "Setting main branch..."
git branch -M main

echo "Pushing to GitHub..."
echo "(This may prompt you to authenticate)"
echo ""

git push -u origin main

echo ""
echo "✅ Repository pushed to GitHub!"
echo ""

# ============================================================================
# STEP 10: Verification
# ============================================================================

echo "✔️  STEP 10: Verification"
echo "════════════════════════════════════"
echo ""

echo "Repository Details:"
echo "  URL:       $GITHUB_URL"
echo "  Branch:    main"
echo "  Commits:   $(git rev-list --count HEAD)"
echo ""

echo "Verify on GitHub:"
echo "  1. Visit: $GITHUB_URL"
echo "  2. Check files are there"
echo "  3. README.md should show on main page"
echo "  4. Star the repository! ⭐"
echo ""

# ============================================================================
# STEP 11: Next Steps
# ============================================================================

echo "🎉 STEP 11: Next Steps"
echo "════════════════════════════════════"
echo ""

echo "Your repository is live! Next steps:"
echo ""
echo "1. 📋 Configure GitHub Settings:"
echo "   - Go to Settings → General"
echo "   - Enable Issues ✓"
echo "   - Enable Discussions ✓"
echo "   - Add Topics: mcp, ultravox, ai, voice"
echo ""
echo "2. 📖 Documentation:"
echo "   - README.md shows installation"
echo "   - Check docs/ folder"
echo "   - View QUICK_START.md"
echo ""
echo "3. 🔧 CI/CD:"
echo "   - GitHub Actions configured"
echo "   - Tests run on every push"
echo "   - Check Actions tab"
echo ""
echo "4. 🌟 Share Your Project:"
echo "   - Tweet about it!"
echo "   - Post on Reddit"
echo "   - Submit to Awesome lists"
echo "   - Share in communities"
echo ""
echo "5. 💬 Community:"
echo "   - Monitor Issues"
echo "   - Respond to Discussions"
echo "   - Merge Pull Requests"
echo "   - Help users!"
echo ""

echo "═════════════════════════════════════════════════════════════════════"
echo ""
echo "✅ DEPLOYMENT COMPLETE!"
echo ""
echo "Repository: $GITHUB_URL"
echo "Branch: main"
echo "Status: Live on GitHub ✅"
echo ""
echo "Made with ❤️ by Mak3it.org"
echo ""
echo "═════════════════════════════════════════════════════════════════════"
