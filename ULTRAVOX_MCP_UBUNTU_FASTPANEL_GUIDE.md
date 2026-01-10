# 🚀 ULTRAVOX MCP SUR UBUNTU FASTPANEL - GUIDE COMPLET

**Pour un serveur MCP public accessible à tous!**

---

## 📋 PRÉREQUIS

✅ Ubuntu 20.04+ (sur ton serveur Contabo/Fastpanel)
✅ Python 3.8+
✅ Fastpanel installé
✅ Accès SSH/Terminal
✅ Port disponible (ex: 8000, 9000)
✅ API key Ultravox


---

## 🎯 ARCHITECTURE

```
┌─────────────────────────────────┐
│   Clients (Claude, n8n, etc.)   │
│   http://ton-serveur.com:8000   │
└────────────────┬────────────────┘
                 │ HTTP Requests
┌────────────────▼────────────────┐
│   HTTP Wrapper (Flask/FastAPI)  │
│   Port: 8000                    │
└────────────────┬────────────────┘
                 │ JSON RPC
┌────────────────▼────────────────┐
│   Ultravox MCP Server (stdio)   │
│   29 Ultravox Tools             │
└────────────────┬────────────────┘
                 │
┌────────────────▼────────────────┐
│   Ultravox API                  │
│   api.ultravox.ai               │
└─────────────────────────────────┘
```

---

## 📥 ÉTAPE 1: TÉLÉCHARGER LE PROJET

```bash
# Connexion SSH à ton serveur
ssh root@ton-serveur-ip

# Aller dans le répertoire web (ou autre)
cd /home/user

# Cloner le projet
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Vérifier la structure
ls -la
```

---

## ⚙️ ÉTAPE 2: INSTALLATION PYTHON

### Option A: Installation globale (Simple)

```bash
# Update apt
sudo apt update
sudo apt upgrade -y

# Installer Python & pip
sudo apt install python3 python3-pip python3-venv git -y

# Vérifier les versions
python3 --version
pip3 --version
```

### Option B: Virtual Environment (Recommandé pour Fastpanel)

```bash
# Créer un venv dans le dossier du projet
cd /home/user/ultravox-mcp-unofficial
python3 -m venv venv

# Activer
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
pip install flask flask-cors  # Pour HTTP wrapper

echo "✅ Virtual environment prêt!"
```

---

## 🔑 ÉTAPE 3: CONFIGURER LA CLÉ API

```bash
# Créer le fichier .env
cp .env.example .env

# Éditer et ajouter ta clé
nano .env

# Ajouter:
ULTRAVOX_API_KEY=ta_clé_api_ici
DEBUG=false
LOG_LEVEL=INFO

# Sauvegarder: Ctrl+X, Y, Enter
```

**⚠️ IMPORTANT - Sécurité:**
```bash
# Protéger le fichier
chmod 600 .env

# Vérifier (.env ne doit pas être lisible par tous)
ls -la .env
```

---

## 🌐 ÉTAPE 4: CRÉER UN HTTP WRAPPER

Le MCP parle en JSON-RPC via stdin/stdout. On a besoin d'un wrapper HTTP pour que les clients puissent y accéder.

**Créer le fichier: `http_wrapper.py`**

```bash
nano /home/user/ultravox-mcp-unofficial/http_wrapper.py
```

**Coller ce code:**

```python
#!/usr/bin/env python3
"""
HTTP Wrapper pour Ultravox MCP
Expose le serveur MCP via HTTP REST API
"""

import os
import json
import subprocess
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Configuration
API_KEY = os.getenv('ULTRAVOX_API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
PORT = int(os.getenv('MCP_PORT', 8000))

# Vérifier la clé API
if not API_KEY:
    print("❌ ERROR: ULTRAVOX_API_KEY not set in .env")
    sys.exit(1)

# Processus MCP (démarré une seule fois)
mcp_process = None

def start_mcp_server():
    """Démarrer le serveur MCP"""
    global mcp_process
    
    if mcp_process:
        return
    
    env = os.environ.copy()
    env['ULTRAVOX_API_KEY'] = API_KEY
    
    try:
        mcp_process = subprocess.Popen(
            ['python3', 'src/server.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print("✅ MCP Server started")
    except Exception as e:
        print(f"❌ Failed to start MCP: {e}")
        sys.exit(1)

def call_mcp_tool(tool_name, arguments):
    """Appeler un outil MCP"""
    if not mcp_process:
        start_mcp_server()
    
    try:
        # Construire la requête JSON-RPC
        request_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        # Envoyer au serveur MCP
        request_json = json.dumps(request_data) + "\n"
        mcp_process.stdin.write(request_json)
        mcp_process.stdin.flush()
        
        # Lire la réponse
        response_line = mcp_process.stdout.readline()
        if response_line:
            response = json.loads(response_line)
            return response
        else:
            return {"error": "No response from MCP server"}
    
    except Exception as e:
        return {"error": str(e)}

# Routes HTTP

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Ultravox MCP HTTP Wrapper",
        "version": "1.0.0"
    })

@app.route('/tools', methods=['GET'])
def list_tools():
    """Lister tous les outils disponibles"""
    tools_list = [
        # CALLS
        {"name": "list_calls", "description": "List all calls"},
        {"name": "get_call", "description": "Get call details"},
        {"name": "get_call_messages", "description": "Get call messages"},
        {"name": "get_call_recording", "description": "Get call recording"},
        {"name": "get_call_tools", "description": "Get tools used in call"},
        {"name": "get_call_stages", "description": "Get call stages"},
        {"name": "get_call_stage", "description": "Get specific stage"},
        {"name": "get_stage_messages", "description": "Get stage messages"},
        {"name": "delete_call", "description": "Delete a call"},
        
        # AGENTS
        {"name": "list_agents", "description": "List all agents"},
        {"name": "get_agent", "description": "Get agent details"},
        {"name": "list_agent_calls", "description": "List agent calls"},
        {"name": "update_agent_prompt", "description": "Update agent prompt"},
        {"name": "delete_agent", "description": "Delete agent"},
        
        # VOICES
        {"name": "list_voices", "description": "List available voices"},
        {"name": "get_voice", "description": "Get voice details"},
        
        # MODELS
        {"name": "list_models", "description": "List available models"},
        
        # WEBHOOKS
        {"name": "list_webhooks", "description": "List webhooks"},
        {"name": "get_webhook", "description": "Get webhook details"},
        {"name": "create_webhook", "description": "Create webhook"},
        {"name": "delete_webhook", "description": "Delete webhook"},
        
        # DELETED CALLS
        {"name": "get_deleted_calls", "description": "Get deleted calls"},
        {"name": "get_deleted_call", "description": "Get deleted call details"},
        {"name": "list_deleted_calls_stream", "description": "List deleted calls"},
        
        # RESOURCES
        {"name": "get_tools_list", "description": "Get system tools"},
        {"name": "get_tool", "description": "Get tool details"},
        {"name": "get_account_info", "description": "Get account info"},
    ]
    return jsonify({"tools": tools_list, "total": len(tools_list)})

@app.route('/call', methods=['POST'])
def call_tool():
    """Endpoint pour appeler un outil MCP"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        tool_name = data.get('tool')
        arguments = data.get('args', {})
        
        if not tool_name:
            return jsonify({"error": "Tool name required"}), 400
        
        # Appeler l'outil
        result = call_mcp_tool(tool_name, arguments)
        
        return jsonify({
            "success": True,
            "tool": tool_name,
            "result": result
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/agents', methods=['GET'])
def get_agents_shortcut():
    """Shortcut: GET /agents = list_agents"""
    result = call_mcp_tool("list_agents", {"limit": 10})
    return jsonify(result)

@app.route('/calls', methods=['GET'])
def get_calls_shortcut():
    """Shortcut: GET /calls = list_calls"""
    result = call_mcp_tool("list_calls", {"limit": 10})
    return jsonify(result)

@app.route('/voices', methods=['GET'])
def get_voices_shortcut():
    """Shortcut: GET /voices = list_voices"""
    result = call_mcp_tool("list_voices", {"limit": 20})
    return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == '__main__':
    print("╔════════════════════════════════════════╗")
    print("║  Ultravox MCP - HTTP Wrapper          ║")
    print("╚════════════════════════════════════════╝")
    print(f"\n🚀 Starting on http://0.0.0.0:{PORT}")
    print(f"\n📊 Available endpoints:")
    print(f"   GET  /health      - Health check")
    print(f"   GET  /tools       - List all tools")
    print(f"   POST /call        - Call a tool")
    print(f"   GET  /agents      - List agents")
    print(f"   GET  /calls       - List calls")
    print(f"   GET  /voices      - List voices")
    print(f"\n💡 Example call:")
    print(f'   curl -X POST http://localhost:{PORT}/call \\')
    print(f'     -H "Content-Type: application/json" \\')
    print(f'     -d \'{{"tool":"list_agents","args":{{"limit":10}}}}\'')
    print(f"\n⚠️  Log level: {LOG_LEVEL}\n")
    
    # Démarrer le serveur Flask
    app.run(
        host='0.0.0.0',
        port=PORT,
        debug=(LOG_LEVEL == 'DEBUG')
    )
```

**Sauvegarder:** Ctrl+X, Y, Enter

---

## 🔧 ÉTAPE 5: TESTER LOCALEMENT

```bash
# Activer le venv (si utilisé)
source venv/bin/activate

# Installer Flask (si pas déjà)
pip install flask flask-cors

# Lancer le wrapper
python3 http_wrapper.py
```

**Vous devriez voir:**
```
╔════════════════════════════════════════╗
║  Ultravox MCP - HTTP Wrapper          ║
╚════════════════════════════════════════╝

🚀 Starting on http://0.0.0.0:8000
```

**Tester dans un autre terminal:**

```bash
# Test 1: Health check
curl http://localhost:8000/health

# Test 2: List agents
curl http://localhost:8000/agents

# Test 3: Call a tool
curl -X POST http://localhost:8000/call \
  -H "Content-Type: application/json" \
  -d '{"tool":"list_voices","args":{"limit":5}}'
```

---

## 🐧 ÉTAPE 6: CONFIGURER AVEC FASTPANEL

### Via Fastpanel WebUI:

1. **Aller à Fastpanel → Applications**
2. **Créer nouvelle application:**
   - Nom: `ultravox-mcp`
   - Port: `8000`
   - Type: `Custom/Python`
   - Path: `/home/user/ultravox-mcp-unofficial`

3. **Ou via SSH (plus direct):**

```bash
# Créer un script de démarrage
sudo nano /etc/systemd/system/ultravox-mcp.service
```

**Coller:**

```ini
[Unit]
Description=Ultravox MCP HTTP Server
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/home/user/ultravox-mcp-unofficial
Environment="PATH=/home/user/ultravox-mcp-unofficial/venv/bin"
Environment="ULTRAVOX_API_KEY=ta_clé_api"
ExecStart=/home/user/ultravox-mcp-unofficial/venv/bin/python3 http_wrapper.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Configurer:**

```bash
# Recharger systemd
sudo systemctl daemon-reload

# Activer au démarrage
sudo systemctl enable ultravox-mcp

# Démarrer le service
sudo systemctl start ultravox-mcp

# Vérifier le statut
sudo systemctl status ultravox-mcp

# Voir les logs
sudo journalctl -u ultravox-mcp -f
```

---

## 🌍 ÉTAPE 7: EXPOSER PUBLIQUEMENT (Nginx/Apache)

### Via Nginx (Fastpanel):

**1. Créer la config:**

```bash
sudo nano /etc/nginx/sites-available/ultravox-mcp
```

**2. Ajouter:**

```nginx
server {
    listen 80;
    server_name ton-domaine.com;
    
    # Rediriger HTTP → HTTPS (optionnel)
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name ton-domaine.com;
    
    # Certificats SSL (Let's Encrypt via Fastpanel)
    ssl_certificate /etc/letsencrypt/live/ton-domaine.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ton-domaine.com/privkey.pem;
    
    # Proxy vers le serveur MCP
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Logs
    access_log /var/log/nginx/ultravox-mcp-access.log;
    error_log /var/log/nginx/ultravox-mcp-error.log;
}
```

**3. Activer:**

```bash
sudo ln -s /etc/nginx/sites-available/ultravox-mcp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 🔐 ÉTAPE 8: SÉCURITÉ

### Ajouter une clé API pour les clients:

**Modifier `http_wrapper.py` (ajouter après CORS):**

```python
from functools import wraps

# Liste des clés API valides
VALID_API_KEYS = {
    'key1_for_claude': 'claude-client',
    'key2_for_n8n': 'n8n-client',
}

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            return jsonify({"error": "API key required"}), 401
        
        if api_key not in VALID_API_KEYS:
            return jsonify({"error": "Invalid API key"}), 403
        
        return f(*args, **kwargs)
    return decorated_function

# Appliquer à toutes les routes sauf /health
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/tools', methods=['GET'])
@require_api_key
def list_tools():
    # ...
```

### Utiliser avec API key:

```bash
curl -H "X-API-Key: key1_for_claude" http://ton-domaine.com/health
```

---

## 📊 ÉTAPE 9: MONITORING

### Via Fastpanel:

1. **Dashboard** → Voir les ressources utilisées
2. **Logs** → `/var/log/nginx/ultravox-mcp-access.log`

### Depuis terminal:

```bash
# CPU & RAM
top
ps aux | grep http_wrapper

# Logs en temps réel
tail -f /var/log/nginx/ultravox-mcp-error.log

# Connexions
netstat -tlnp | grep 8000

# Redémarrer si crash
sudo systemctl restart ultravox-mcp
```

---

## 🎯 ÉTAPE 10: UTILISER DEPUIS CLAUDE/n8n

### Depuis Claude Desktop:

```json
{
  "mcpServers": {
    "ultravox-remote": {
      "command": "curl",
      "args": [
        "-X", "POST",
        "https://ton-domaine.com/call",
        "-H", "Content-Type: application/json",
        "-H", "X-API-Key: key1_for_claude",
        "-d", "@-"
      ]
    }
  }
}
```

### Depuis n8n:

1. **Ajouter HTTP Request node**
2. **URL:** `https://ton-domaine.com/call`
3. **Headers:** `X-API-Key: key2_for_n8n`
4. **Body:** 
```json
{
  "tool": "list_agents",
  "args": {"limit": 10}
}
```

---

## 📋 CHECKLIST FINAL

✅ Python installé
✅ Projet cloné
✅ .env configuré (clé API)
✅ http_wrapper.py créé
✅ Service systemd activé
✅ Nginx configuré
✅ SSL/HTTPS activé
✅ API keys ajoutées
✅ Testé localement
✅ Testé à distance
✅ Monitoring en place

---

## 🆘 TROUBLESHOOTING

### Erreur: "ULTRAVOX_API_KEY not set"

```bash
# Vérifier .env
cat .env

# Ou le passer directement
export ULTRAVOX_API_KEY="ta_clé"
python3 http_wrapper.py
```

### Port 8000 déjà utilisé

```bash
# Voir ce qui utilise le port
sudo lsof -i :8000

# Changer le port
export MCP_PORT=9000
python3 http_wrapper.py
```

### Erreur de connexion SSL

```bash
# Renouveler le certificat
sudo certbot renew

# Ou via Fastpanel (recommandé)
```

### Service ne démarre pas

```bash
# Voir l'erreur
sudo journalctl -u ultravox-mcp -n 50

# Redémarrer
sudo systemctl restart ultravox-mcp
```

---

## 🚀 COMMANDES UTILES

```bash
# Démarrer/arrêter
sudo systemctl start ultravox-mcp
sudo systemctl stop ultravox-mcp
sudo systemctl restart ultravox-mcp

# Logs
sudo journalctl -u ultravox-mcp -f
sudo tail -f /var/log/nginx/ultravox-mcp-error.log

# Status
sudo systemctl status ultravox-mcp

# Activer/désactiver au démarrage
sudo systemctl enable ultravox-mcp
sudo systemctl disable ultravox-mcp

# Tester
curl https://ton-domaine.com/health
```

---

## 📞 SUPPORT

- **Email:** hello@mak3it.org
- **Site:** https://mak3it.org
- **Docs:** Voir le dossier `/docs`

---

**Voilà! Tu as maintenant un serveur MCP Ultravox public et accessible à tous!** 🎉
