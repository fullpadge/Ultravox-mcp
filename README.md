# Serveur MCP Ultravox

Serveur Model Context Protocol (MCP) pour l'API Ultravox. Permet à Claude d'accéder directement aux appels et voix Ultravox.

## Installation

### Pré-requis
- Python 3.10+
- Une clé API Ultravox (disponible à https://ultravox.ai)

### Étapes

1. **Configure ta clé API** : Ouvre le fichier `.env` et remplace `REMPLACE_PAR_TA_CLE_API_ULTRAVOX` par ta vraie clé.

2. **Lance le serveur** :
   ```
   python ultravox_mcp.py
   ```

## Outils disponibles

- `list_calls(limit=20)` : Récupère les appels Ultravox
- `get_call(call_id)` : Récupère les détails d'un appel
- `list_voices()` : Récupère les voix disponibles

## Utilisation avec Claude Desktop

Voir le guide SETUP.md pour la configuration complète.

## Structure du projet

- `ultravox_mcp.py` : Code principal du serveur MCP
- `.env` : Fichier de configuration (contient ta clé API)
- `.gitignore` : Fichiers à exclure de Git
- `README.md` : Ce fichier
