# 🎤 Ultravox MCP - Unofficial

[![Mak3it][(https://mak3it.org/wp-content/uploads/2025/08/logo-mak3it-white-scaled.png)](https://mak3it.org)

**A powerful, unofficial Model Context Protocol (MCP) server for Ultravox Voice AI**

**Built with ❤️ by [Mak3it.org](https://mak3it.org)**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/fullpadge/Ultravox-mcp.svg)](https://github.com/fullpadge/Ultravox-mcp)

**[English](#english) | [Français](#français)**

---

## English

### 🚀 Features

- **29 Ultravox API Tools** - Full access to Ultravox's voice AI capabilities
- **MCP Protocol** - Works with Claude Desktop, n8n, and any MCP-compatible application
- **Multi-Platform** - Linux, macOS, Windows, Docker
- **Production-Ready** - Fully tested, documented, and secure
- **Easy Integration** - Integrates seamlessly with Claude AI, n8n workflows, and more
- **Comprehensive Documentation** - Full guides for all platforms
- **CI/CD Ready** - GitHub Actions workflow included

### 🛠️ Quick Installation

#### Claude Desktop (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
# Edit .env and add your ULTRAVOX_API_KEY
nano .env
```

4. Configure Claude Desktop. Edit `~/.claude/claude_desktop_config.json`:

**macOS/Linux:**
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/path/to/Ultravox-mcp/src/server.py"]
    }
  }
}
```

**Windows (PowerShell):**
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

5. Restart Claude Desktop - Done! ✅

### 📚 Available Tools

The server exposes 29 Ultravox API tools:

**Calls Management:**
- `list_calls` - List all voice calls
- `get_call` - Get call details and metadata
- `get_call_messages` - Get call transcript and messages
- `get_call_recording` - Get call audio recording
- `get_call_tools` - Get tools used in a call
- `get_call_stages` - Get call conversation stages
- `delete_call` - Delete a call

**Agent Management:**
- `list_agents` - List all AI agents
- `get_agent` - Get agent configuration
- `list_agent_calls` - List calls for an agent
- `update_agent_prompt` - Update agent prompt/system message
- `delete_agent` - Delete an agent

**Voice & Models:**
- `list_voices` - List available voice models
- `get_voice` - Get voice details
- `list_models` - List available AI models

**Webhooks:**
- `list_webhooks` - List all webhooks
- `get_webhook` - Get webhook details
- `create_webhook` - Create a new webhook
- `delete_webhook` - Delete a webhook

**Deleted Calls:**
- `get_deleted_calls` - List deleted calls
- `get_deleted_call` - Get deleted call details
- `list_deleted_calls_stream` - Stream deleted calls

**Resources & Account:**
- `get_tools_list` - List available tools
- `get_tool` - Get tool details
- `get_account_info` - Get account information

### 💻 Usage Examples

#### Python
```python
from src.server import UltravoxMCPServer

# Initialize
server = UltravoxMCPServer()

# List agents
agents = server.list_agents(limit=10)

# Get agent details
agent = server.get_agent(agent_id="agent_123")

# List calls
calls = server.list_calls(limit=20)

# Get call recording
recording = server.get_call_recording(call_id="call_456")
```

#### Via Claude AI
Simply ask Claude to use the Ultravox tools:
- "List all my agents"
- "Get the last 10 calls and their recordings"
- "Create a new webhook for call events"
- "Show me the transcripts of today's calls"

#### Via n8n
1. Add an HTTP Request node
2. Configure POST request to your MCP server
3. Select the tool and parameters
4. Connect to other workflows

### 🐳 Docker Installation

```bash
# Build image
docker build -t ultravox-mcp .

# Run container
docker run -e ULTRAVOX_API_KEY="your_key" -p 8000:8000 ultravox-mcp

# Or with Docker Compose
docker-compose up
```

### 🔧 Configuration

Create a `.env` file:
```env
ULTRAVOX_API_KEY=your_api_key_here
DEBUG=false
LOG_LEVEL=INFO
```

### 📖 Full Documentation

- [QUICK_START.md](./QUICK_START.md) - 5-minute setup guide
- [Installation Guides](./docs/) - Platform-specific installation
- [API Reference](./docs/API_REFERENCE.md) - Complete API documentation
- [Configuration](./docs/CONFIGURATION.md) - Advanced configuration
- [Troubleshooting](./docs/TROUBLESHOOTING.md) - Common issues and solutions

### 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### 📝 License

MIT License - see [LICENSE](./LICENSE) file for details

### 🙏 Acknowledgments

- Built for the Ultravox community
- Unofficial project - not affiliated with Ultravox
- Special thanks to all contributors

### 📞 Support

- GitHub Issues: [Report bugs](https://github.com/fullpadge/Ultravox-mcp/issues)
- Discussions: [Ask questions](https://github.com/fullpadge/Ultravox-mcp/discussions)

---

## Français

### 🚀 Caractéristiques

- **29 Outils API Ultravox** - Accès complet aux capacités vocales d'Ultravox
- **Protocole MCP** - Fonctionne avec Claude Desktop, n8n et toute application compatible
- **Multi-Plateforme** - Linux, macOS, Windows, Docker
- **Production Ready** - Complètement testé, documenté et sécurisé
- **Intégration Facile** - S'intègre parfaitement avec Claude AI, n8n, et plus
- **Documentation Complète** - Guides complets pour toutes les plateformes
- **CI/CD Prêt** - Workflow GitHub Actions inclus

### 🛠️ Installation Rapide

#### Claude Desktop (Recommandé)

1. Clonez le dépôt:
```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

2. Installez les dépendances:
```bash
pip install -r requirements.txt
```

3. Créez le fichier `.env`:
```bash
cp .env.example .env
# Éditez .env et ajoutez votre ULTRAVOX_API_KEY
nano .env
```

4. Configurez Claude Desktop. Éditez `~/.claude/claude_desktop_config.json`:

**macOS/Linux:**
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

**Windows (PowerShell):**
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\chemin\\vers\\Ultravox-mcp\\src\\server.py"]
    }
  }
}
```

5. Redémarrez Claude Desktop - C'est fait! ✅

### 📚 Outils Disponibles

Le serveur expose 29 outils API Ultravox (voir section English pour la liste complète).

### 💻 Exemples d'Utilisation

#### Python
```python
from src.server import UltravoxMCPServer

# Initialiser
server = UltravoxMCPServer()

# Lister les agents
agents = server.list_agents(limit=10)

# Obtenir les détails d'un agent
agent = server.get_agent(agent_id="agent_123")
```

#### Avec Claude AI
Demandez simplement à Claude d'utiliser les outils Ultravox:
- "Liste tous mes agents"
- "Récupère les 10 derniers appels avec leurs enregistrements"
- "Crée un nouveau webhook pour les événements d'appel"
- "Montre-moi les transcriptions d'aujourd'hui"

#### Via n8n
1. Ajoutez un nœud HTTP Request
2. Configurez une requête POST vers votre serveur MCP
3. Sélectionnez l'outil et les paramètres
4. Connectez à d'autres workflows

### 🐳 Installation Docker

```bash
# Construire l'image
docker build -t ultravox-mcp .

# Exécuter le conteneur
docker run -e ULTRAVOX_API_KEY="votre_clé" -p 8000:8000 ultravox-mcp

# Ou avec Docker Compose
docker-compose up
```

### 🔧 Configuration

Créez un fichier `.env`:
```env
ULTRAVOX_API_KEY=votre_clé_api_ici
DEBUG=false
LOG_LEVEL=INFO
```

### 📖 Documentation Complète

- [QUICK_START.md](./QUICK_START.md) - Guide de 5 minutes
- [Guides d'Installation](./docs/) - Installation spécifique à la plateforme
- [Référence API](./docs/API_REFERENCE.md) - Documentation API complète
- [Configuration](./docs/CONFIGURATION.md) - Configuration avancée
- [Dépannage](./docs/TROUBLESHOOTING.md) - Problèmes courants et solutions

### 🤝 Contribution

Les contributions sont bienvenues! Voir [CONTRIBUTING.md](./CONTRIBUTING.md) pour les directives.

### 📝 Licence

Licence MIT - voir le fichier [LICENSE](./LICENSE) pour les détails.

### 📞 Support

- Issues GitHub: [Signaler un bug](https://github.com/fullpadge/Ultravox-mcp/issues)
- Discussions: [Poser une question](https://github.com/fullpadge/Ultravox-mcp/discussions)

---

## 🎯 Next Steps

1. Choose your platform (Claude Desktop, Docker, Linux, etc.)
2. Follow the installation guide for your platform
3. Configure your API key
4. Start using Ultravox tools!

---

**Made with ❤️ by the community**

---

## 🌐 About Mak3it

[**Mak3it.org**](https://mak3it.org) - AI-Powered Legal Technology Solutions

This project is maintained by the Mak3it team, specialists in building cutting-edge AI solutions for Quebec's legal tech ecosystem.

**Website:** https://mak3it.org  
**Email:** hello@mak3it.org  
**GitHub:** https://github.com/fullpadge
