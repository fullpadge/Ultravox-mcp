#!/usr/bin/env python3
"""
Serveur MCP Ultravox - VERSION COMPLÈTE AVEC 30 TOOLS
Fonctionne avec OU SANS FastMCP + httpx
"""

import json
import sys
import os

# Configuration
API_KEY = os.getenv("ULTRAVOX_API_KEY", "VJtcPzQd.t3wzaodHSgEtGHVUasa09LpnVWHQCfjh")
API_BASE = "https://api.ultravox.ai/api"

# Essayer d'importer les modules
try:
    from fastmcp import FastMCP
    import httpx
    USE_FASTMCP = True
except ImportError:
    import urllib.request
    import urllib.error
    USE_FASTMCP = False

# ==== VERSION FASTMCP ====
if USE_FASTMCP:
    try:
        mcp = FastMCP("ultravox")
        
        HEADERS = {
            "X-API-Key": API_KEY,
            "Content-Type": "application/json",
        }

        # ===== ACCOUNT & SYSTEM (2) =====
        @mcp.tool()
        def get_account_info() -> dict:
            """Récupère les infos du compte Ultravox"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/accounts/me", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_open_api_schema() -> dict:
            """Récupère le schéma OpenAPI de l'API Ultravox"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/openapi.json", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return {"success": True, "paths_count": len(response.json().get("paths", {}))}
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== CALLS (9) =====
        @mcp.tool()
        def list_calls(limit: int = 20) -> dict:
            """Liste les appels"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call(call_id: str) -> dict:
            """Récupère les détails d'un appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_messages(call_id: str, limit: int = 20) -> dict:
            """Récupère les messages d'un appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/messages", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_recording(call_id: str) -> dict:
            """Récupère l'enregistrement d'un appel"""
            try:
                with httpx.Client(follow_redirects=True) as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/recording", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        # Retourner l'URL de redirection ou le contenu
                        return {
                            "success": True,
                            "call_id": call_id,
                            "url": str(response.url),
                            "content_type": response.headers.get("content-type"),
                            "size": len(response.content)
                        }
                    elif response.status_code == 302:
                        # Récupérer le header Location du redirect
                        location = response.headers.get("location")
                        return {
                            "success": True,
                            "call_id": call_id,
                            "recording_url": location,
                            "message": "Enregistrement trouvé"
                        }
                    return {"error": f"Erreur ({response.status_code})", "status_code": response.status_code}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_tools(call_id: str) -> dict:
            """Récupère les outils utilisés dans un appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/tools", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        tools_list = response.json()
                        return {
                            "call_id": call_id,
                            "tools": tools_list if isinstance(tools_list, list) else [tools_list],
                            "count": len(tools_list) if isinstance(tools_list, list) else 1
                        }
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_stages(call_id: str) -> dict:
            """Récupère les étapes d'un appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/stages", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_stage(call_id: str, stage_id: str) -> dict:
            """Récupère les détails d'une étape d'appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/stages/{stage_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_stage_messages(call_id: str, stage_id: str, limit: int = 20) -> dict:
            """Récupère les messages d'une étape d'appel"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/calls/{call_id}/stages/{stage_id}/messages", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def delete_call(call_id: str) -> dict:
            """Supprime un appel (DESTRUCTIF)"""
            try:
                with httpx.Client() as client:
                    response = client.delete(f"{API_BASE}/calls/{call_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code in [200, 204]:
                        return {"success": True, "message": "Appel supprimé"}
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== AGENTS (5) =====
        @mcp.tool()
        def list_agents(limit: int = 20) -> dict:
            """Liste les agents"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/agents", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_agent(agent_id: str) -> dict:
            """Récupère les détails d'un agent"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/agents/{agent_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def list_agent_calls(agent_id: str, limit: int = 20) -> dict:
            """Liste les appels d'un agent"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/agents/{agent_id}/calls", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def update_agent_prompt(agent_id: str, prompt: str) -> dict:
            """Met à jour le prompt d'un agent"""
            try:
                with httpx.Client() as client:
                    response = client.patch(f"{API_BASE}/agents/{agent_id}", headers=HEADERS, json={"systemPrompt": prompt}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def delete_agent(agent_id: str) -> dict:
            """Supprime un agent (DESTRUCTIF)"""
            try:
                with httpx.Client() as client:
                    response = client.delete(f"{API_BASE}/agents/{agent_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code in [200, 204]:
                        return {"success": True, "message": "Agent supprimé"}
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== VOICES (2) =====
        @mcp.tool()
        def list_voices(limit: int = 20) -> dict:
            """Liste les voix disponibles"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/voices", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_voice(voice_id: str) -> dict:
            """Récupère les détails d'une voix"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/voices/{voice_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== MODELS (1) =====
        @mcp.tool()
        def list_models() -> dict:
            """Liste les modèles disponibles"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/models", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== WEBHOOKS (4) =====
        @mcp.tool()
        def list_webhooks() -> dict:
            """Liste les webhooks"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/webhooks", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_webhook(webhook_id: str) -> dict:
            """Récupère les détails d'un webhook"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/webhooks/{webhook_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def create_webhook(agent_id: str, url: str, events: list) -> dict:
            """Crée un webhook"""
            try:
                with httpx.Client() as client:
                    response = client.post(f"{API_BASE}/webhooks", headers=HEADERS, json={"agentId": agent_id, "url": url, "events": events}, timeout=10.0)
                    if response.status_code in [200, 201]:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def delete_webhook(webhook_id: str) -> dict:
            """Supprime un webhook (DESTRUCTIF)"""
            try:
                with httpx.Client() as client:
                    response = client.delete(f"{API_BASE}/webhooks/{webhook_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code in [200, 204]:
                        return {"success": True, "message": "Webhook supprimé"}
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== DELETED CALLS (3) =====
        @mcp.tool()
        def get_deleted_calls(limit: int = 20) -> dict:
            """Récupère la liste des appels supprimés"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/deleted_calls", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_deleted_call(call_id: str) -> dict:
            """Récupère les détails d'un appel supprimé"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/deleted_calls/{call_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def list_deleted_calls_stream(limit: int = 20) -> dict:
            """Liste les appels supprimés avec streaming"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/deleted_calls", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        # ===== RESOURCES (2) =====
        @mcp.tool()
        def get_tools_list(limit: int = 20) -> dict:
            """Récupère la liste des outils disponibles"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/tools", headers=HEADERS, params={"limit": limit}, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_tool(tool_id: str) -> dict:
            """Récupère les détails d'un outil"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/tools/{tool_id}", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        @mcp.tool()
        def get_call_usage() -> dict:
            """Récupère l'utilisation des appels"""
            try:
                with httpx.Client() as client:
                    response = client.get(f"{API_BASE}/accounts/me/call_usage", headers=HEADERS, timeout=10.0)
                    if response.status_code == 200:
                        return response.json()
                    return {"error": f"Erreur ({response.status_code})"}
            except Exception as e:
                return {"error": str(e)}

        if __name__ == "__main__":
            mcp.run()
    
    except Exception as e:
        print(f"ERREUR FastMCP: {e}", file=sys.stderr)
        sys.exit(1)

# ==== VERSION FALLBACK (SANS DÉPENDANCES) ====
else:
    def make_request(endpoint, method="GET", json_data=None):
        """Fait une requête HTTP à l'API Ultravox"""
        url = f"{API_BASE}{endpoint}"
        
        try:
            body = json.dumps(json_data).encode('utf-8') if json_data else None
            req = urllib.request.Request(url, data=body, method=method, headers={"X-API-Key": API_KEY, "Content-Type": "application/json"})
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')
                return json.loads(data)
        except urllib.error.HTTPError as e:
            return {"error": f"HTTP Error {e.code}", "status_code": e.code}
        except Exception as e:
            return {"error": str(e)}

    def handle_tool(name, arguments):
        """Exécute un tool"""
        
        # ACCOUNT & SYSTEM
        if name == "get_account_info":
            return make_request("/accounts/me")
        elif name == "get_open_api_schema":
            return make_request("/openapi.json")
        
        # CALLS
        elif name == "list_calls":
            limit = arguments.get("limit", 20)
            return make_request(f"/calls?limit={limit}")
        elif name == "get_call":
            call_id = arguments.get("call_id")
            return make_request(f"/calls/{call_id}")
        elif name == "get_call_messages":
            call_id = arguments.get("call_id")
            limit = arguments.get("limit", 20)
            return make_request(f"/calls/{call_id}/messages?limit={limit}")
        elif name == "get_call_recording":
            call_id = arguments.get("call_id")
            # Créer une requête avec suivi des redirects
            url = f"{API_BASE}/calls/{call_id}/recording"
            try:
                req = urllib.request.Request(url, method="GET", headers={"X-API-Key": API_KEY, "Content-Type": "application/json"})
                # urllib suit les redirects par défaut, mais on capture l'URL finale
                with urllib.request.urlopen(req, timeout=10) as response:
                    data = response.read().decode('utf-8')
                    return {
                        "success": True,
                        "call_id": call_id,
                        "url": response.url,
                        "content_type": response.headers.get("content-type"),
                        "message": "Enregistrement récupéré"
                    }
            except urllib.error.HTTPError as e:
                if e.code == 302:
                    location = e.headers.get("Location")
                    return {"success": True, "call_id": call_id, "recording_url": location, "message": "Redirect vers l'enregistrement"}
                return {"error": f"HTTP Error {e.code}", "status_code": e.code}
            except Exception as e:
                return {"error": str(e)}
        elif name == "get_call_tools":
            call_id = arguments.get("call_id")
            try:
                req = urllib.request.Request(f"{API_BASE}/calls/{call_id}/tools", method="GET", headers={"X-API-Key": API_KEY, "Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=10) as response:
                    data = response.read().decode('utf-8')
                    tools_list = json.loads(data)
                    return {
                        "call_id": call_id,
                        "tools": tools_list if isinstance(tools_list, list) else [tools_list],
                        "count": len(tools_list) if isinstance(tools_list, list) else 1
                    }
            except urllib.error.HTTPError as e:
                return {"error": f"HTTP Error {e.code}", "status_code": e.code}
            except Exception as e:
                return {"error": str(e)}
        elif name == "get_call_stages":
            call_id = arguments.get("call_id")
            return make_request(f"/calls/{call_id}/stages")
        elif name == "get_call_stage":
            call_id = arguments.get("call_id")
            stage_id = arguments.get("stage_id")
            return make_request(f"/calls/{call_id}/stages/{stage_id}")
        elif name == "get_stage_messages":
            call_id = arguments.get("call_id")
            stage_id = arguments.get("stage_id")
            limit = arguments.get("limit", 20)
            return make_request(f"/calls/{call_id}/stages/{stage_id}/messages?limit={limit}")
        elif name == "delete_call":
            call_id = arguments.get("call_id")
            return make_request(f"/calls/{call_id}", method="DELETE")
        
        # AGENTS
        elif name == "list_agents":
            limit = arguments.get("limit", 20)
            return make_request(f"/agents?limit={limit}")
        elif name == "get_agent":
            agent_id = arguments.get("agent_id")
            return make_request(f"/agents/{agent_id}")
        elif name == "list_agent_calls":
            agent_id = arguments.get("agent_id")
            limit = arguments.get("limit", 20)
            return make_request(f"/agents/{agent_id}/calls?limit={limit}")
        elif name == "update_agent_prompt":
            agent_id = arguments.get("agent_id")
            prompt = arguments.get("prompt")
            return make_request(f"/agents/{agent_id}", method="PATCH", json_data={"systemPrompt": prompt})
        elif name == "delete_agent":
            agent_id = arguments.get("agent_id")
            return make_request(f"/agents/{agent_id}", method="DELETE")
        
        # VOICES
        elif name == "list_voices":
            limit = arguments.get("limit", 20)
            return make_request(f"/voices?limit={limit}")
        elif name == "get_voice":
            voice_id = arguments.get("voice_id")
            return make_request(f"/voices/{voice_id}")
        
        # MODELS
        elif name == "list_models":
            return make_request("/models")
        
        # WEBHOOKS
        elif name == "list_webhooks":
            return make_request("/webhooks")
        elif name == "get_webhook":
            webhook_id = arguments.get("webhook_id")
            return make_request(f"/webhooks/{webhook_id}")
        elif name == "create_webhook":
            agent_id = arguments.get("agent_id")
            url = arguments.get("url")
            events = arguments.get("events", [])
            return make_request("/webhooks", method="POST", json_data={"agentId": agent_id, "url": url, "events": events})
        elif name == "delete_webhook":
            webhook_id = arguments.get("webhook_id")
            return make_request(f"/webhooks/{webhook_id}", method="DELETE")
        
        # DELETED CALLS
        elif name == "get_deleted_calls":
            limit = arguments.get("limit", 20)
            return make_request(f"/deleted_calls?limit={limit}")
        elif name == "get_deleted_call":
            call_id = arguments.get("call_id")
            return make_request(f"/deleted_calls/{call_id}")
        elif name == "list_deleted_calls_stream":
            limit = arguments.get("limit", 20)
            return make_request(f"/deleted_calls?limit={limit}")
        
        # RESOURCES
        elif name == "get_tools_list":
            limit = arguments.get("limit", 20)
            return make_request(f"/tools?limit={limit}")
        elif name == "get_tool":
            tool_id = arguments.get("tool_id")
            return make_request(f"/tools/{tool_id}")
        elif name == "get_call_usage":
            return make_request("/accounts/me/call_usage")
        
        else:
            return {"error": f"Tool '{name}' not found"}

    def main():
        """Main loop"""
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                request = json.loads(line)
                
                if request.get("method") == "initialize":
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {},
                            "serverInfo": {
                                "name": "ultravox-mcp",
                                "version": "30.0.0"
                            }
                        }
                    }
                
                elif request.get("method") == "tools/list":
                    tools = [
                        {"name": "get_account_info", "description": "Get account info"},
                        {"name": "get_open_api_schema", "description": "Get OpenAPI schema"},
                        {"name": "list_calls", "description": "List calls"},
                        {"name": "get_call", "description": "Get call details"},
                        {"name": "get_call_messages", "description": "Get call messages"},
                        {"name": "get_call_recording", "description": "Get call recording"},
                        {"name": "get_call_tools", "description": "Get call tools"},
                        {"name": "get_call_stages", "description": "Get call stages"},
                        {"name": "get_call_stage", "description": "Get call stage details"},
                        {"name": "get_stage_messages", "description": "Get stage messages"},
                        {"name": "delete_call", "description": "Delete a call"},
                        {"name": "list_agents", "description": "List agents"},
                        {"name": "get_agent", "description": "Get agent details"},
                        {"name": "list_agent_calls", "description": "List agent calls"},
                        {"name": "update_agent_prompt", "description": "Update agent prompt"},
                        {"name": "delete_agent", "description": "Delete an agent"},
                        {"name": "list_voices", "description": "List voices"},
                        {"name": "get_voice", "description": "Get voice details"},
                        {"name": "list_models", "description": "List models"},
                        {"name": "list_webhooks", "description": "List webhooks"},
                        {"name": "get_webhook", "description": "Get webhook details"},
                        {"name": "create_webhook", "description": "Create a webhook"},
                        {"name": "delete_webhook", "description": "Delete a webhook"},
                        {"name": "get_deleted_calls", "description": "Get deleted calls"},
                        {"name": "get_deleted_call", "description": "Get deleted call details"},
                        {"name": "list_deleted_calls_stream", "description": "List deleted calls stream"},
                        {"name": "get_tools_list", "description": "Get tools list"},
                        {"name": "get_tool", "description": "Get tool details"},
                        {"name": "get_call_usage", "description": "Get call usage"},
                    ]
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": {"tools": tools}
                    }
                
                elif request.get("method") == "tools/call":
                    tool_name = request.get("params", {}).get("name")
                    arguments = request.get("params", {}).get("arguments", {})
                    result = handle_tool(tool_name, arguments)
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": {"content": [{"type": "text", "text": json.dumps(result)}]}
                    }
                
                else:
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "error": {"code": -32601, "message": "Method not found"}
                    }
                
                print(json.dumps(response))
                sys.stdout.flush()
            
            except Exception as e:
                try:
                    print(json.dumps({
                        "jsonrpc": "2.0",
                        "error": {"code": -32700, "message": str(e)}
                    }))
                    sys.stdout.flush()
                except:
                    pass

    if __name__ == "__main__":
        main()