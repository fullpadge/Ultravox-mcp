# Claude Desktop Installation Guide / Guide d'installation Claude Desktop

---

## English

### Windows Installation

#### Step 1: Download and Setup

```bash
# 1. Clone the repository
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Create Python virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

#### Step 2: Configure API Key

```bash
# 1. Create .env file from template
copy .env.example .env

# 2. Edit .env and add your Ultravox API key
# Open .env in your editor and update:
# ULTRAVOX_API_KEY=your_actual_api_key_here
```

**Important:** Never share your `.env` file!

#### Step 3: Update Claude Desktop Config

1. **Find the config file:**
   - Path: `C:\Users\YourUsername\AppData\Roaming\Claude\claude_desktop_config.json`
   - If it doesn't exist, create it

2. **Edit the config:**

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": [
        "C:\\Users\\YourUsername\\path\\to\\ultravox-mcp-unofficial\\src\\server.py"
      ],
      "env": {
        "ULTRAVOX_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Replace:**
- `YourUsername` with your Windows username
- `path\\to` with the actual path
- `your_api_key_here` with your Ultravox API key

#### Step 4: Verify Installation

```bash
# Test the server locally
python src/server.py

# You should see:
# MCP Server running on stdio
# Ultravox tools loaded: 29
```

#### Step 5: Restart Claude Desktop

1. Close Claude Desktop completely
2. Reopen Claude Desktop
3. You should now see the Ultravox tools available

---

### Mac Installation

#### Step 1: Download and Setup

```bash
# 1. Clone the repository
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Create Python virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

#### Step 2: Configure API Key

```bash
# 1. Create .env file from template
cp .env.example .env

# 2. Edit .env with your API key
nano .env
# Add: ULTRAVOX_API_KEY=your_api_key_here
# Save: Ctrl+X, Y, Enter
```

#### Step 3: Update Claude Desktop Config

1. **Find the config file:**
   - Path: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

2. **Edit the config:**

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": [
        "/Users/yourname/path/to/ultravox-mcp-unofficial/src/server.py"
      ],
      "env": {
        "ULTRAVOX_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

#### Step 4: Restart Claude Desktop

```bash
# Kill and restart Claude Desktop
killall "Claude"
open /Applications/Claude.app
```

---

## Français

### Installation Windows

#### Étape 1 : Télécharger et configurer

```bash
# 1. Cloner le dépôt
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Créer un environnement virtuel Python
python -m venv venv

# 3. Activer l'environnement virtuel
venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

#### Étape 2 : Configurer la clé API

```bash
# 1. Créer un fichier .env à partir du modèle
copy .env.example .env

# 2. Éditer .env et ajouter votre clé Ultravox
# Ouvrez .env dans un éditeur et mettez à jour:
# ULTRAVOX_API_KEY=votre_clé_api_ici
```

**Important :** Ne partagez jamais votre fichier `.env` !

#### Étape 3 : Mettre à jour la configuration Claude Desktop

1. **Trouver le fichier de configuration :**
   - Chemin: `C:\Users\VotreNom\AppData\Roaming\Claude\claude_desktop_config.json`
   - S'il n'existe pas, créez-le

2. **Éditer la configuration :**

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": [
        "C:\\Users\\VotreNom\\chemin\\vers\\ultravox-mcp-unofficial\\src\\server.py"
      ],
      "env": {
        "ULTRAVOX_API_KEY": "votre_clé_api_ici"
      }
    }
  }
}
```

**Remplacer :**
- `VotreNom` par votre nom d'utilisateur Windows
- `chemin\\vers` par le chemin réel
- `votre_clé_api_ici` par votre clé Ultravox

#### Étape 4 : Vérifier l'installation

```bash
# Tester le serveur localement
python src/server.py

# Vous devriez voir:
# MCP Server running on stdio
# Ultravox tools loaded: 29
```

#### Étape 5 : Redémarrer Claude Desktop

1. Fermer Claude Desktop complètement
2. Rouvrir Claude Desktop
3. Vous devriez maintenant voir les outils Ultravox disponibles

---

### Installation Mac

#### Étape 1 : Télécharger et configurer

```bash
# 1. Cloner le dépôt
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# 2. Créer un environnement virtuel Python
python3 -m venv venv

# 3. Activer l'environnement virtuel
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

#### Étape 2 : Configurer la clé API

```bash
# 1. Créer un fichier .env à partir du modèle
cp .env.example .env

# 2. Éditer .env avec votre clé API
nano .env
# Ajouter: ULTRAVOX_API_KEY=votre_clé_api_ici
# Sauvegarder: Ctrl+X, Y, Entrée
```

#### Étape 3 : Mettre à jour la configuration Claude Desktop

1. **Trouver le fichier de configuration :**
   - Chemin: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

2. **Éditer la configuration :**

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python3",
      "args": [
        "/Users/votrenomd'utilisateur/chemin/vers/ultravox-mcp-unofficial/src/server.py"
      ],
      "env": {
        "ULTRAVOX_API_KEY": "votre_clé_api_ici"
      }
    }
  }
}
```

#### Étape 4 : Redémarrer Claude Desktop

```bash
# Terminer et redémarrer Claude Desktop
killall "Claude"
open /Applications/Claude.app
```

---

## Troubleshooting / Dépannage

### Problem: "Server not responding"

**Solution:**
```bash
# 1. Check .env file exists
cat .env

# 2. Verify API key is set
echo $ULTRAVOX_API_KEY

# 3. Test server directly
python src/server.py

# 4. Check file path in config is correct
# It must be an absolute path, not relative
```

### Problem: "Module not found: fastmcp"

**Solution:**
This is normal! The server includes a fallback. Just ensure you've installed:
```bash
pip install -r requirements.txt
```

### Problem: "Permission denied" on Mac/Linux

**Solution:**
```bash
# Make script executable
chmod +x src/server.py

# Update config to use full path
# And ensure Python path is absolute
```

---

## Next Steps

- Read the [API Reference](../docs/API_REFERENCE.md)
- Check [Usage Examples](../examples/)
- See [Configuration Guide](../docs/CONFIGURATION.md) for advanced options
