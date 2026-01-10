# n8n Integration Guide / Guide d'intégration n8n

---

## English

### Method 1: Local MCP Server (Recommended)

This method runs the Ultravox MCP server locally and connects n8n via HTTP.

#### Step 1: Setup Ultravox MCP Server

```bash
# Clone and setup (follow Claude Desktop guide first)
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your API key

# Run the server
export ULTRAVOX_API_KEY=$(grep ULTRAVOX_API_KEY .env | cut -d '=' -f2)
python src/server.py

# Server should be running on stdin/stdout
# For HTTP mode, you can use a wrapper (see Method 2)
```

#### Step 2: Create n8n HTTP Wrapper

Create a simple HTTP wrapper to expose the MCP server:

**File: `src/http_wrapper.py`**

```python
#!/usr/bin/env python3
"""
HTTP wrapper for Ultravox MCP server
Allows n8n to call MCP tools via HTTP requests
"""

import os
import json
import sys
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            request = json.loads(body)
            # Parse tool name and arguments
            tool_name = request.get('tool')
            args = request.get('args', {})
            
            # Call the server (implementation depends on your server)
            result = call_tool(tool_name, args)
            
            # Return result
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'result': result
            }).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': False,
                'error': str(e)
            }).encode())
    
    def log_message(self, format, *args):
        # Suppress logging
        pass

def call_tool(tool_name, args):
    # Implementation to call your MCP server
    # This is a placeholder
    return {"tool": tool_name, "args": args}

if __name__ == '__main__':
    port = int(os.getenv('HTTP_PORT', 8000))
    server = HTTPServer(('localhost', port), MCPHandler)
    print(f"HTTP wrapper running on http://localhost:{port}")
    server.serve_forever()
```

#### Step 3: Configure n8n HTTP Node

In your n8n workflow:

1. **Add HTTP Request node**
2. **Configure:**
   - Method: POST
   - URL: `http://localhost:8000/tool`
   - Headers: `Content-Type: application/json`
   - Body:
     ```json
     {
       "tool": "list_agents",
       "args": {
         "limit": 10
       }
     }
     ```

3. **Test:** Click Execute

---

### Method 2: Docker Container

Run Ultravox MCP in Docker for better isolation.

#### Step 1: Create Dockerfile

**File: `Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source
COPY src/ ./src/

# Expose port for HTTP wrapper
EXPOSE 8000

# Set environment
ENV PYTHONUNBUFFERED=1

# Run server
CMD ["python", "src/server.py"]
```

#### Step 2: Build and Run

```bash
# Build image
docker build -t ultravox-mcp .

# Run container with API key
docker run -e ULTRAVOX_API_KEY="your_key" -p 8000:8000 ultravox-mcp

# Run with .env file
docker run --env-file .env -p 8000:8000 ultravox-mcp
```

#### Step 3: Connect n8n

In n8n, configure HTTP node to connect to:
- URL: `http://host.docker.internal:8000/tool` (if n8n is also in Docker)
- Or: `http://localhost:8000/tool` (if n8n is on host)

---

### Method 3: n8n Custom Node

Create a custom n8n node (advanced).

**File: `n8n/Ultravox.node.ts`**

```typescript
import {
  IExecuteFunctions,
  INodeExecutionData,
  INodeType,
  INodeTypeDescription,
  NodeOperationError,
} from 'n8n-workflow';

export class Ultravox implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'Ultravox',
    name: 'ultravox',
    group: ['transform'],
    version: 1,
    description: 'Call Ultravox MCP tools',
    inputs: ['main'],
    outputs: ['main'],
    properties: [
      {
        displayName: 'Tool',
        name: 'tool',
        type: 'options',
        options: [
          { name: 'List Agents', value: 'list_agents' },
          { name: 'Get Agent', value: 'get_agent' },
          { name: 'List Calls', value: 'list_calls' },
          { name: 'Get Call', value: 'get_call' },
          // ... add all tools
        ],
        required: true,
        default: 'list_agents',
      },
      {
        displayName: 'Arguments',
        name: 'arguments',
        type: 'json',
        required: false,
        default: '{}',
      },
    ],
  };

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    const items = this.getInputData();
    const tool = this.getNodeParameter('tool', 0) as string;
    const args = this.getNodeParameter('arguments', 0) as object;

    const results = [];
    for (let i = 0; i < items.length; i++) {
      try {
        // Call MCP server
        const result = await callUltravoxTool(tool, args);
        results.push({ json: result });
      } catch (error) {
        throw new NodeOperationError(this.getNode(), error);
      }
    }

    return [results];
  }
}

async function callUltravoxTool(tool: string, args: any): Promise<any> {
  // Implementation to call MCP server
  const response = await fetch('http://localhost:8000/tool', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tool, args }),
  });
  return await response.json();
}
```

---

### Usage Examples in n8n

#### Example 1: List All Agents

```
1. Start node → Ultravox node
2. Tool: "list_agents"
3. Arguments: {"limit": 10}
4. Next node processes the results
```

#### Example 2: Get Call Details and Download Recording

```
1. HTTP node to get call ID from webhook
2. Ultravox node: get_call (with call ID)
3. Ultravox node: get_call_recording
4. Save recording to file
```

---

## Français

### Méthode 1 : Serveur MCP local (Recommandé)

#### Étape 1 : Configuration du serveur Ultravox MCP

```bash
# Cloner et configurer
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Installer les dépendances
pip install -r requirements.txt

# Créer un fichier .env
cp .env.example .env
# Éditer .env et ajouter votre clé API

# Exécuter le serveur
export ULTRAVOX_API_KEY=$(grep ULTRAVOX_API_KEY .env | cut -d '=' -f2)
python src/server.py
```

#### Étape 2 : Configurer n8n

Dans votre workflow n8n:

1. **Ajouter un nœud HTTP Request**
2. **Configurer :**
   - Méthode: POST
   - URL: `http://localhost:8000/tool`
   - En-têtes: `Content-Type: application/json`
   - Corps:
     ```json
     {
       "tool": "list_agents",
       "args": {"limit": 10}
     }
     ```

3. **Tester:** Cliquez sur Exécuter

---

### Méthode 2 : Conteneur Docker

#### Étape 1 : Créer le Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le code source
COPY src/ ./src/

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "src/server.py"]
```

#### Étape 2 : Construire et exécuter

```bash
# Construire l'image
docker build -t ultravox-mcp .

# Exécuter avec la clé API
docker run -e ULTRAVOX_API_KEY="votre_clé" -p 8000:8000 ultravox-mcp
```

---

### Exemples d'utilisation dans n8n

#### Exemple 1 : Lister tous les agents

```
1. Nœud de démarrage → Nœud Ultravox
2. Outil: "list_agents"
3. Arguments: {"limit": 10}
4. Nœud suivant traite les résultats
```

---

## Troubleshooting

### Connection refused

**Solution:**
```bash
# Verify server is running
ps aux | grep server.py

# Check port is accessible
netstat -an | grep 8000

# Test directly
curl -X POST http://localhost:8000/tool \
  -H "Content-Type: application/json" \
  -d '{"tool":"list_agents","args":{}}'
```

### API Key not recognized

```bash
# Verify .env file
cat .env

# Check n8n workflow has correct API key in headers
```

### CORS errors in n8n

**Solution:** Add CORS headers to HTTP wrapper

```python
self.send_header('Access-Control-Allow-Origin', '*')
self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
```

---

## Further Reading

- [API Reference](../docs/API_REFERENCE.md)
- [Configuration Guide](../docs/CONFIGURATION.md)
- [Deployment Guide](../docs/DEPLOYMENT.md)
