# Quick Start / Démarrage rapide

---

## English - 5 Minutes Setup

### Step 1: Clone (1 min)
```bash
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial
```

### Step 2: Install (2 min)
```bash
pip install -r requirements.txt
```

### Step 3: Configure (1 min)
```bash
cp .env.example .env
# Edit .env and add: ULTRAVOX_API_KEY=your_key_here
```

### Step 4: Test (1 min)
```bash
python src/server.py
# Should show: "MCP Server running"
# Press Ctrl+C to stop
```

### Step 5: Use in Claude Desktop

**Windows:**
Edit: `C:\Users\YOU\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\path\\to\\ultravox-mcp-unofficial\\src\\server.py"],
      "env": {"ULTRAVOX_API_KEY": "your_key"}
    }
  }
}
```

**Mac:**
Edit: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": ["/path/to/ultravox-mcp-unofficial/src/server.py"],
      "env": {"ULTRAVOX_API_KEY": "your_key"}
    }
  }
}
```

Restart Claude Desktop → Done! 🎉

### Use It

In Claude:
```
"List my Ultravox agents"
"Get details for call xyz"
"Download the recording"
"Create a webhook for my agent"
```

---

## Français - Configuration en 5 minutes

### Étape 1: Cloner (1 min)
```bash
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial
```

### Étape 2: Installer (2 min)
```bash
pip install -r requirements.txt
```

### Étape 3: Configurer (1 min)
```bash
cp .env.example .env
# Éditer .env et ajouter: ULTRAVOX_API_KEY=votre_clé
```

### Étape 4: Tester (1 min)
```bash
python src/server.py
# Devrait afficher: "MCP Server running"
# Appuyez sur Ctrl+C pour arrêter
```

### Étape 5: Utiliser dans Claude Desktop

**Windows:**
Éditer: `C:\Users\VOUS\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\chemin\\vers\\ultravox-mcp-unofficial\\src\\server.py"],
      "env": {"ULTRAVOX_API_KEY": "votre_clé"}
    }
  }
}
```

**Mac:**
Éditer: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": ["/chemin/vers/ultravox-mcp-unofficial/src/server.py"],
      "env": {"ULTRAVOX_API_KEY": "votre_clé"}
    }
  }
}
```

Redémarrer Claude Desktop → C'est fait! 🎉

### L'utiliser

Dans Claude:
```
"Lister mes agents Ultravox"
"Obtenir les détails de l'appel xyz"
"Télécharger l'enregistrement"
"Créer un webhook pour mon agent"
```

---

## Docker Quick Start

```bash
# Build
docker build -t ultravox-mcp .

# Run
docker run -e ULTRAVOX_API_KEY="your_key" -p 8000:8000 ultravox-mcp

# Or with docker-compose
docker-compose up -d
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| "API key invalid" | Check .env file has correct key |
| "Server not responding" | Make sure server.py is running |
| "Permission denied" | Run `chmod +x src/server.py` (Linux) |
| "Port 8000 in use" | Change port in docker-compose.yml |

---

## Next Steps

- 📖 [Full Installation Guide](./docs/CLAUDE_DESKTOP_INSTALLATION.md)
- 🔧 [Configuration Guide](./docs/CONFIGURATION.md)
- 📚 [API Reference](./docs/API_REFERENCE.md)
- 🐳 [Docker Setup](./docs/LINUX_DOCKER_INSTALLATION.md)
- 🔗 [n8n Integration](./docs/N8N_INTEGRATION.md)

---

## API Key Tips

1. **Get your key**: https://console.ultravox.ai
2. **Store in .env**: `.env` is in `.gitignore` (safe!)
3. **Never commit**: Don't put key in code or GitHub
4. **Rotate regularly**: For security

---

## Support

- 📧 Email: hello@mak3it.org
- 🌐 Website: https://mak3it.org
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

---

**Made with ❤️ by Mak3it.org**
