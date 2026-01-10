#!/usr/bin/env python3
"""
Serveur MCP Ultravox - Version STDLIB ONLY (zéro dépendances)
Utilise uniquement urllib (Python standard library)
"""

import json
import sys
import os
import urllib.request
import urllib.error

# Configuration
API_KEY = os.getenv("ULTRAVOX_API_KEY", "VJtcPzQd.t3wzaodHSgEtGHVUasa09LpnVWHQCfjh")
API_BASE = "https://api.ultravox.ai/api"

def make_request(endpoint, method="GET"):
    """Fait une requête HTTP à l'API Ultravox"""
    url = f"{API_BASE}{endpoint}"
    
    try:
        req = urllib.request.Request(
            url,
            method=method,
            headers={
                "X-API-Key": API_KEY,
                "Content-Type": "application/json"
            }
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP Error {e.code}"}
    except Exception as e:
        return {"error": str(e)}

def handle_tool(name, arguments):
    """Exécute un tool"""
    
    if name == "get_account_info":
        return make_request("/accounts/me")
    
    elif name == "list_agents":
        limit = arguments.get("limit", 20)
        return make_request(f"/agents?limit={limit}")
    
    elif name == "get_agent":
        agent_id = arguments.get("agent_id")
        return make_request(f"/agents/{agent_id}")
    
    elif name == "list_calls":
        limit = arguments.get("limit", 20)
        return make_request(f"/calls?limit={limit}")
    
    elif name == "get_call":
        call_id = arguments.get("call_id")
        return make_request(f"/calls/{call_id}")
    
    elif name == "get_call_messages":
        call_id = arguments.get("call_id")
        return make_request(f"/calls/{call_id}/messages")
    
    elif name == "get_call_recording":
        call_id = arguments.get("call_id")
        return make_request(f"/calls/{call_id}/recording")
    
    elif name == "get_call_tools":
        call_id = arguments.get("call_id")
        return make_request(f"/calls/{call_id}/tools")
    
    elif name == "get_call_stages":
        call_id = arguments.get("call_id")
        return make_request(f"/calls/{call_id}/stages")
    
    elif name == "list_voices":
        limit = arguments.get("limit", 20)
        return make_request(f"/voices?limit={limit}")
    
    elif name == "list_models":
        return make_request("/models")
    
    elif name == "list_webhooks":
        return make_request("/webhooks")
    
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
            method = request.get("jsonrpc")
            
            if request.get("method") == "initialize":
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {},
                        "serverInfo": {
                            "name": "ultravox-mcp",
                            "version": "1.0.0"
                        }
                    }
                }
            
            elif request.get("method") == "tools/list":
                tools = [
                    {"name": "get_account_info", "description": "Get account info"},
                    {"name": "list_agents", "description": "List agents"},
                    {"name": "get_agent", "description": "Get agent details"},
                    {"name": "list_calls", "description": "List calls"},
                    {"name": "get_call", "description": "Get call details"},
                    {"name": "get_call_messages", "description": "Get call messages"},
                    {"name": "get_call_recording", "description": "Get recording"},
                    {"name": "get_call_tools", "description": "Get tools used"},
                    {"name": "get_call_stages", "description": "Get call stages"},
                    {"name": "list_voices", "description": "List voices"},
                    {"name": "list_models", "description": "List models"},
                    {"name": "list_webhooks", "description": "List webhooks"}
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
