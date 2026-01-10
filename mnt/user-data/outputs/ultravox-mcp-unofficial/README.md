# Ultravox MCP - Unofficial

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)

**[English](#english) | [Français](#français)**

</div>

---

# English

## Overview

An **unofficial** Model Context Protocol (MCP) server for Anthropic's **Ultravox AI** voice API.

This server provides seamless integration between Ultravox voice AI capabilities and MCP-compatible clients like **Claude Desktop**, **n8n**, and custom applications.

### Features ✨

- ✅ **29 Ultravox API Tools** - Full coverage of calls, agents, voices, webhooks, and more
- ✅ **Dual Mode** - Works with or without FastMCP (automatic fallback to stdlib)
- ✅ **Multi-Platform** - Claude Desktop, n8n, Linux servers, Docker-ready
- ✅ **Secure** - API key protection via environment variables
- ✅ **Production Ready** - 27/29 tools tested and validated
- ✅ **Comprehensive Docs** - English & French guides included

### Tools Included (29 Total)

**Calls (10):** list_calls, get_call, get_call_messages, get_call_recording, get_call_tools, get_call_stages, get_call_stage, get_stage_messages, delete_call

**Agents (5):** list_agents, get_agent, list_agent_calls, update_agent_prompt, delete_agent

**Voices (2):** list_voices, get_voice

**Models (1):** list_models

**Webhooks (4):** list_webhooks, get_webhook, create_webhook, delete_webhook

**Deleted Calls (3):** get_deleted_calls, get_deleted_call, list_deleted_calls_stream

**Resources (3):** get_tools_list, get_tool, get_call_usage

---

## Quick Start

### 1. Prerequisites

- Python 3.8+
- Ultravox API key (get at [console.ultravox.ai](https://console.ultravox.ai))
- Claude Desktop / n8n / Linux environment

### 2. Installation

#### Claude Desktop (Windows/Mac)

```bash
# 1. Clone repository
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key
cp .env.example .env
# Edit .env and add your ULTRAVOX_API_KEY

# 4. Update Claude Desktop config
# Windows: C:\Users\[YOU]\AppData\Roaming\Claude\claude_desktop_config.json
# Mac: ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Add this to your config:
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/path/to/ultravox-mcp-unofficial/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}

# 5. Restart Claude Desktop
```

#### n8n

```bash
# 1. In n8n, add new HTTP Request node
# 2. Configure for local MCP server
# 3. Use POST requests to http://localhost:8000/tools
```

#### Linux/Docker

```bash
# Clone and setup
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Install
pip install -r requirements.txt

# Run
export ULTRAVOX_API_KEY="your_key_here"
python src/server.py

# Docker
docker build -t ultravox-mcp .
docker run -e ULTRAVOX_API_KEY="your_key" -p 8000:8000 ultravox-mcp
```

---

## Configuration

### Environment Variables

Create `.env` file:

```bash
# Required
ULTRAVOX_API_KEY=your_api_key_here

# Optional
ULTRAVOX_API_BASE=https://api.ultravox.ai/api
DEBUG=false
LOG_LEVEL=INFO
```

### Claude Desktop Config Example

**Windows:** `C:\Users\YourUsername\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": ["C:\\Path\\To\\ultravox-mcp-unofficial\\src\\server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Mac:** `~/Library/Application\ Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": ["/Users/yourname/path/to/ultravox-mcp-unofficial/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

---

## Usage Examples

### Claude Desktop

```
You: "List all my Ultravox agents"
Claude: Uses list_agents tool to fetch your agents

You: "Get details about call xyz"
Claude: Uses get_call tool with the call ID

You: "Download the recording from the latest call"
Claude: Uses get_call_recording to retrieve the audio
```

### Python Script

```python
import json
import subprocess
import os

os.environ['ULTRAVOX_API_KEY'] = 'your_key'

# Start the MCP server
process = subprocess.Popen(['python', 'src/server.py'])

# Call MCP tools via stdin/stdout
tool_request = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "list_agents",
        "arguments": {"limit": 10}
    }
}

# Send request and get response
result = json.loads(response)
print(result)
```

---

## Documentation

- 📖 [Installation Guide](./docs/INSTALLATION.md) - Detailed setup for all platforms
- 🔧 [Configuration Guide](./docs/CONFIGURATION.md) - Environment and API setup
- 📚 [API Reference](./docs/API_REFERENCE.md) - Complete tool documentation
- 🚀 [Deployment Guide](./docs/DEPLOYMENT.md) - Production deployment
- 🐛 [Troubleshooting](./docs/TROUBLESHOOTING.md) - Common issues

---

## Testing

```bash
# Run test suite
python -m pytest tests/

# Test specific tool
python -m pytest tests/test_calls.py::test_list_calls

# Validation report
python tests/validation_report.py
```

**Test Coverage:** 27/29 tools (93.1%) ✅

---

## Architecture

```
ultravox-mcp-unofficial/
├── src/
│   ├── server.py              # Main MCP server
│   ├── fastmcp_version.py     # FastMCP implementation
│   └── stdlib_version.py      # Stdlib fallback
├── docs/
│   ├── INSTALLATION.md
│   ├── API_REFERENCE.md
│   └── DEPLOYMENT.md
├── install/
│   ├── claude_desktop.sh
│   ├── n8n_setup.md
│   └── linux_docker.md
├── tests/
│   └── test_tools.py
├── examples/
│   └── usage_example.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Requirements

### Minimal
- Python 3.8+
- urllib (included in Python)
- Your Ultravox API key

### Recommended
- FastMCP (auto-installs)
- httpx (for better performance)
- pytest (for testing)

See [requirements.txt](./requirements.txt) for full list.

---

## Security & API Keys

⚠️ **IMPORTANT:**
- Never commit `.env` file to GitHub
- Use environment variables for API keys
- Rotate keys regularly
- Use separate keys for dev/prod

Example secure setup:
```bash
# Don't do this:
export ULTRAVOX_API_KEY="xxx"  # ❌ Visible in history

# Do this:
# 1. Create .env file (in .gitignore)
# 2. Load at runtime
source .env && python src/server.py
```

---

## Troubleshooting

### Issue: "Server disconnected" in Claude Desktop

**Solution:** Check `.env` file exists and API key is set

```bash
# Verify
echo $ULTRAVOX_API_KEY
cat .env
```

### Issue: "Module not found: fastmcp"

**Solution:** Server automatically falls back to stdlib. No action needed.

### Issue: API Key shows in logs

**Solution:** Check LOG_LEVEL isn't set to DEBUG

```bash
export LOG_LEVEL=INFO
```

---

## Limitations

- ⚠️ 2 endpoints not implemented by Ultravox API:
  - `get_open_api_schema` (404)
  - `get_call_usage` (404)

- ✅ All other 27 tools are fully functional and tested

---

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

---

## License

MIT License - See [LICENSE](./LICENSE) for details

---

## Disclaimer

**This is an UNOFFICIAL implementation** not affiliated with Ultravox/Fixie AI.

Use at your own risk. Respect Ultravox's API Terms of Service.

---

## Support & Community

- 📧 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 🐛 Bugs: Report via GitHub Issues

---

## Credits

Created by **Mak3it.org**

- 🌐 Website: [mak3it.org](https://mak3it.org)
- 📧 Contact: [contact@mak3it.org](mailto:contact@mak3it.org)

---

---

# Français

## Vue d'ensemble

Un serveur **non officiel** du Model Context Protocol (MCP) pour l'API vocale **Ultravox AI** d'Anthropic.

Ce serveur fournit une intégration transparente entre les capacités vocales d'Ultravox et les clients compatibles MCP comme **Claude Desktop**, **n8n** et les applications personnalisées.

### Caractéristiques ✨

- ✅ **29 outils Ultravox** - Couverture complète des appels, agents, voix, webhooks et plus
- ✅ **Mode double** - Fonctionne avec ou sans FastMCP (fallback automatique)
- ✅ **Multi-plateforme** - Claude Desktop, n8n, serveurs Linux, Docker-ready
- ✅ **Sécurisé** - Protection de la clé API via variables d'environnement
- ✅ **Prêt pour la production** - 27/29 outils testés et validés
- ✅ **Documentation complète** - Guides en anglais et français inclus

### Outils inclus (29 total)

**Appels (10):** list_calls, get_call, get_call_messages, get_call_recording, get_call_tools, get_call_stages, get_call_stage, get_stage_messages, delete_call

**Agents (5):** list_agents, get_agent, list_agent_calls, update_agent_prompt, delete_agent

**Voix (2):** list_voices, get_voice

**Modèles (1):** list_models

**Webhooks (4):** list_webhooks, get_webhook, create_webhook, delete_webhook

**Appels supprimés (3):** get_deleted_calls, get_deleted_call, list_deleted_calls_stream

**Ressources (3):** get_tools_list, get_tool, get_call_usage

---

## Démarrage rapide

### 1. Prérequis

- Python 3.8+
- Clé API Ultravox (obtenir sur [console.ultravox.ai](https://console.ultravox.ai))
- Environnement Claude Desktop / n8n / Linux

### 2. Installation

#### Claude Desktop (Windows/Mac)

```bash
# 1. Cloner le dépôt
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer la clé API
cp .env.example .env
# Éditer .env et ajouter votre ULTRAVOX_API_KEY

# 4. Mettre à jour la config Claude Desktop
# Windows: C:\Users\[YOU]\AppData\Roaming\Claude\claude_desktop_config.json
# Mac: ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Ajouter ceci à votre config:
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/chemin/vers/ultravox-mcp-unofficial/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "VOTRE_CLÉ_API"
      }
    }
  }
}

# 5. Redémarrer Claude Desktop
```

#### n8n

```bash
# 1. Dans n8n, ajouter un nouveau nœud HTTP Request
# 2. Configurer pour le serveur MCP local
# 3. Utiliser les requêtes POST vers http://localhost:8000/tools
```

#### Linux/Docker

```bash
# Cloner et configurer
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Installer
pip install -r requirements.txt

# Exécuter
export ULTRAVOX_API_KEY="votre_clé"
python src/server.py

# Docker
docker build -t ultravox-mcp .
docker run -e ULTRAVOX_API_KEY="votre_clé" -p 8000:8000 ultravox-mcp
```

---

## Configuration

### Variables d'environnement

Créer un fichier `.env`:

```bash
# Requis
ULTRAVOX_API_KEY=votre_clé_api

# Optionnel
ULTRAVOX_API_BASE=https://api.ultravox.ai/api
DEBUG=false
LOG_LEVEL=INFO
```

### Exemple de config Claude Desktop

**Windows:** `C:\Users\VotreNom\AppData\Roaming\Claude\claude_desktop_config.json`

**Mac:** `~/Library/Application\ Support/Claude/claude_desktop_config.json`

Voir la section anglaise pour les exemples JSON.

---

## Exemples d'utilisation

### Claude Desktop

```
Vous: "Lister tous mes agents Ultravox"
Claude: Utilise l'outil list_agents pour récupérer vos agents

Vous: "Obtenir les détails de l'appel xyz"
Claude: Utilise l'outil get_call avec l'ID de l'appel

Vous: "Télécharger l'enregistrement du dernier appel"
Claude: Utilise get_call_recording pour récupérer l'audio
```

---

## Documentation

- 📖 [Guide d'installation](./docs/INSTALLATION_FR.md) - Configuration détaillée
- 🔧 [Guide de configuration](./docs/CONFIGURATION_FR.md) - Environnement et API
- 📚 [Référence API](./docs/API_REFERENCE_FR.md) - Documentation complète des outils
- 🚀 [Guide de déploiement](./docs/DEPLOYMENT_FR.md) - Déploiement en production
- 🐛 [Dépannage](./docs/TROUBLESHOOTING_FR.md) - Problèmes courants

---

## Limitations

- ⚠️ 2 endpoints non implémentés par l'API Ultravox:
  - `get_open_api_schema` (404)
  - `get_call_usage` (404)

- ✅ Tous les 27 autres outils sont entièrement fonctionnels et testés

---

## Licence

Licence MIT - Voir [LICENSE](./LICENSE) pour les détails

---

## Clause de non-responsabilité

**Ceci est une implémentation NON OFFICIELLE** non affiliée à Ultravox/Fixie AI.

À utiliser à vos risques et périls. Respectez les conditions d'utilisation de l'API Ultravox.

---

## Créé par Mak3it.org

- 🌐 Site web: [mak3it.org](https://mak3it.org)
- 📧 Contact: [contact@mak3it.org](mailto:contact@mak3it.org)
