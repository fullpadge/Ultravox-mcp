#!/usr/bin/env python3
"""
Ultravox MCP - Python Usage Examples
Demonstrates how to use the Ultravox MCP server
"""

import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Example 1: Import and use the server directly
# (This is more for testing/debugging)

def example_1_list_agents():
    """Example 1: List all agents"""
    print("Example 1: List All Agents")
    print("-" * 50)
    
    # You would typically use the MCP protocol (stdio or HTTP)
    # For this example, we'll show the structure
    
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "list_agents",
            "arguments": {
                "limit": 10
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print("\nThis request would be sent to the MCP server")
    print("Server responds with list of agents in JSON format")
    print()

def example_2_get_call_details():
    """Example 2: Get details of a specific call"""
    print("Example 2: Get Call Details")
    print("-" * 50)
    
    call_id = "your_call_id_here"
    
    request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "get_call",
            "arguments": {
                "call_id": call_id
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print(f"\nFetches all details for call: {call_id}")
    print()

def example_3_list_voices():
    """Example 3: List available voices"""
    print("Example 3: List Available Voices")
    print("-" * 50)
    
    request = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "list_voices",
            "arguments": {
                "limit": 20
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print("\nServer returns 162+ available voices")
    print("Each with provider, language, and preview URL")
    print()

def example_4_create_webhook():
    """Example 4: Create a webhook"""
    print("Example 4: Create a Webhook")
    print("-" * 50)
    
    request = {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {
            "name": "create_webhook",
            "arguments": {
                "agent_id": "your_agent_id",
                "url": "https://your-webhook-url.com/webhook",
                "events": ["call.started", "call.ended"]
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print("\nServer creates new webhook and returns:")
    print("- webhookId")
    print("- secret (for authentication)")
    print("- status")
    print()

def example_5_download_recording():
    """Example 5: Download call recording"""
    print("Example 5: Download Call Recording")
    print("-" * 50)
    
    call_id = "your_call_id"
    
    # Step 1: Get call recording URL
    request1 = {
        "jsonrpc": "2.0",
        "id": 5,
        "method": "tools/call",
        "params": {
            "name": "get_call_recording",
            "arguments": {
                "call_id": call_id
            }
        }
    }
    
    print("Step 1: Get recording URL")
    print(f"Request: {json.dumps(request1, indent=2)}")
    print("\nServer returns: recordingUrl (Google Cloud Storage URL)")
    print("\nStep 2: Download the audio file")
    print("import urllib.request")
    print("urllib.request.urlretrieve(recording_url, 'call_recording.wav')")
    print()

def example_6_update_agent_prompt():
    """Example 6: Update agent system prompt"""
    print("Example 6: Update Agent System Prompt")
    print("-" * 50)
    
    agent_id = "your_agent_id"
    new_prompt = "You are a helpful customer service assistant..."
    
    request = {
        "jsonrpc": "2.0",
        "id": 6,
        "method": "tools/call",
        "params": {
            "name": "update_agent_prompt",
            "arguments": {
                "agent_id": agent_id,
                "prompt": new_prompt
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print("\nServer updates agent prompt and returns:")
    print("- updated agentId")
    print("- new publishedRevisionId")
    print("- callTemplate with new systemPrompt")
    print()

def example_7_get_call_messages():
    """Example 7: Get conversation messages from call"""
    print("Example 7: Get Call Messages (Conversation)")
    print("-" * 50)
    
    call_id = "your_call_id"
    
    request = {
        "jsonrpc": "2.0",
        "id": 7,
        "method": "tools/call",
        "params": {
            "name": "get_call_messages",
            "arguments": {
                "call_id": call_id,
                "limit": 50
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print("\nServer returns all messages in the call:")
    print("- User messages")
    print("- Assistant responses")
    print("- Tool invocations")
    print("- Timestamps and durations")
    print()

def example_8_delete_call():
    """Example 8: Delete a call (archive)"""
    print("Example 8: Delete a Call")
    print("-" * 50)
    print("⚠️  WARNING: DESTRUCTIVE OPERATION")
    
    call_id = "your_call_id"
    
    request = {
        "jsonrpc": "2.0",
        "id": 8,
        "method": "tools/call",
        "params": {
            "name": "delete_call",
            "arguments": {
                "call_id": call_id
            }
        }
    }
    
    print(f"Request: {json.dumps(request, indent=2)}")
    print(f"\nPermanently deletes call: {call_id}")
    print("Call is moved to deleted calls archive")
    print()

def example_9_using_with_claude():
    """Example 9: Using with Claude"""
    print("Example 9: Using with Claude Desktop")
    print("-" * 50)
    
    print("""
In Claude Desktop, you can simply ask:

"List my Ultravox agents"
→ Claude calls list_agents tool automatically

"Get details for call abc123"
→ Claude calls get_call with call_id

"Download the recording from that call"
→ Claude calls get_call_recording

"Create a webhook for my agent to receive updates"
→ Claude calls create_webhook with your parameters

Claude intelligently maps natural language to the right tools!
    """)

def example_10_error_handling():
    """Example 10: Error handling"""
    print("Example 10: Error Handling")
    print("-" * 50)
    
    print("""
Common errors and solutions:

1. 401 Unauthorized
   → API key missing or invalid
   → Check .env file and ULTRAVOX_API_KEY

2. 404 Not Found
   → Agent/Call ID doesn't exist
   → Verify ID is correct

3. 422 Validation Error
   → Invalid parameters
   → Check argument types and values

4. 500 Server Error
   → Ultravox server issue
   → Retry after a few seconds

5. Connection refused
   → MCP server not running
   → Ensure server.py is executing
    """)

def show_api_key_security():
    """Show security best practices"""
    print("Security Best Practices")
    print("=" * 50)
    print("""
⚠️  API KEY SECURITY:

✅ DO:
  • Store API key in .env file
  • Add .env to .gitignore (it's already there)
  • Use environment variables in production
  • Rotate keys regularly
  • Use separate keys for dev/prod

❌ DON'T:
  • Commit .env file to GitHub
  • Hard-code API keys in code
  • Share API key in Slack, email, etc.
  • Log API keys in debug output
  • Use same key for multiple projects

PRODUCTION:
  • Use secrets manager (AWS Secrets, HashiCorp Vault, etc.)
  • Enable API key rotation
  • Monitor API usage
  • Set up alerts for suspicious activity
    """)

if __name__ == "__main__":
    print("=" * 50)
    print("Ultravox MCP - Usage Examples")
    print("=" * 50)
    print()
    
    examples = [
        example_1_list_agents,
        example_2_get_call_details,
        example_3_list_voices,
        example_4_create_webhook,
        example_5_download_recording,
        example_6_update_agent_prompt,
        example_7_get_call_messages,
        example_8_delete_call,
        example_9_using_with_claude,
        example_10_error_handling,
    ]
    
    for example in examples:
        example()
    
    print("\n" + "=" * 50)
    show_api_key_security()
    print("=" * 50)
    print("\nFor more information, see:")
    print("- docs/API_REFERENCE.md")
    print("- docs/CONFIGURATION.md")
    print("- docs/TROUBLESHOOTING.md")
