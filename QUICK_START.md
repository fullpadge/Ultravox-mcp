# 🚀 Quick Start Guide - 5 Minutes

Get Ultravox MCP running in less than 5 minutes!

## Prerequisites

- Python 3.8 or higher
- An Ultravox API key (get one at [api.ultravox.ai](https://api.ultravox.ai))
- pip (Python package manager)

## Step 1: Clone the Repository (1 min)

```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

## Step 2: Install Dependencies (1 min)

```bash
pip install -r requirements.txt
```

## Step 3: Configure API Key (1 min)

```bash
# Copy the example env file
cp .env.example .env

# Edit it with your API key
# On macOS/Linux:
nano .env

# On Windows:
notepad .env
```

Add your Ultravox API key:
```env
ULTRAVOX_API_KEY=your_api_key_here
```

## Step 4: Set up Claude Desktop (2 min)

### macOS/Linux

1. Edit Claude Desktop config:
```bash
nano ~/.claude/claude_desktop_config.json
```

2. Add this configuration:
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/absolute/path/to/Ultravox-mcp/src/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/` with your actual path!

### Windows

1. Open File Explorer
2. Navigate to: `%APPDATA%\Claude\claude_desktop_config.json`
3. Edit the file and add:
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\path\\to\\Ultravox-mcp\\src\\server.py"]
    }
  }
}
```

3. Save and close
4. Restart Claude Desktop

## Step 5: Test It! (30 sec)

Restart Claude Desktop and try:
- "List my agents"
- "Show me my latest calls"
- "Get call details for [call_id]"

## ✅ You're Done!

Claude Desktop can now access all 29 Ultravox tools!

## 🐳 Docker Alternative (2 min)

If you prefer Docker:

```bash
docker build -t ultravox-mcp .
docker run -e ULTRAVOX_API_KEY="your_key" ultravox-mcp
```

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named..."
```bash
# Make sure you installed dependencies
pip install -r requirements.txt
```

### "ULTRAVOX_API_KEY not found"
```bash
# Make sure .env file exists and has your key
cat .env
```

### Claude Desktop not connecting
```bash
# Make sure you used the ABSOLUTE path in config
# Restart Claude Desktop after editing the config
# Check that Python is in your PATH: python --version
```

## 📚 What's Next?

- Read [CONTRIBUTING.md](./CONTRIBUTING.md) to contribute
- Check [docs/](./docs/) for detailed guides
- See [examples/](./examples/) for code samples

---

---

## 🌐 About Mak3it

Built by [**Mak3it.org**](https://mak3it.org) - AI-Powered Legal Tech Solutions

---

## Guide Rapide Français - 5 Minutes

### Étape 1: Cloner le dépôt (1 min)
```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

### Étape 2: Installer les dépendances (1 min)
```bash
pip install -r requirements.txt
```

### Étape 3: Configurer la clé API (1 min)
```bash
cp .env.example .env
nano .env  # ou notepad .env sur Windows
```

Ajoutez votre clé API Ultravox.

### Étape 4: Configurer Claude Desktop (2 min)

**macOS/Linux:**
```bash
nano ~/.claude/claude_desktop_config.json
```

**Windows:**
Ouvrez: `%APPDATA%\Claude\claude_desktop_config.json`

Ajoutez:
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/chemin/vers/Ultravox-mcp/src/server.py"]
    }
  }
}
```

### Étape 5: Tester! (30 sec)

Redémarrez Claude Desktop et essayez:
- "Liste mes agents"
- "Montre-moi mes derniers appels"

## ✅ C'est fait!

Claude Desktop a accès à tous les 29 outils Ultravox!
