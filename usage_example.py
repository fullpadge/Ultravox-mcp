#!/usr/bin/env python3
"""
Ultravox MCP - Python Usage Examples

This script demonstrates how to use the Ultravox MCP server.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the server
from src.server import UltravoxMCPServer

def example_1_initialize_server():
    """Example 1: Initialize the MCP Server"""
    print("\n" + "="*50)
    print("Example 1: Initialize Server")
    print("="*50)
    
    api_key = os.getenv('ULTRAVOX_API_KEY')
    server = UltravoxMCPServer()
    print(f"✅ Server initialized")
    return server

def example_2_list_agents(server):
    """Example 2: List all agents"""
    print("\n" + "="*50)
    print("Example 2: List Agents")
    print("="*50)
    
    try:
        agents = server.list_agents(limit=5)
        print(f"✅ Found {len(agents)} agents")
        for agent in agents:
            print(f"  - {agent.get('name', 'Unknown')}: {agent.get('agentId')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_3_get_agent_details(server, agent_id=None):
    """Example 3: Get specific agent details"""
    print("\n" + "="*50)
    print("Example 3: Get Agent Details")
    print("="*50)
    
    # First, get an agent ID
    agents = server.list_agents(limit=1)
    if not agents:
        print("No agents found. Create one first!")
        return
    
    agent_id = agents[0]['agentId']
    
    try:
        agent = server.get_agent(agent_id)
        print(f"✅ Agent Details:")
        print(f"  Name: {agent.get('name')}")
        print(f"  ID: {agent.get('agentId')}")
        print(f"  Model: {agent.get('model')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_4_list_calls(server):
    """Example 4: List all calls"""
    print("\n" + "="*50)
    print("Example 4: List Calls")
    print("="*50)
    
    try:
        calls = server.list_calls(limit=10)
        print(f"✅ Found {len(calls)} calls")
        for call in calls:
            print(f"  - Call {call['callId']}: {call.get('created')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_5_get_call_details(server):
    """Example 5: Get specific call details"""
    print("\n" + "="*50)
    print("Example 5: Get Call Details")
    print("="*50)
    
    # First, get a call ID
    calls = server.list_calls(limit=1)
    if not calls:
        print("No calls found. Make a call first!")
        return
    
    call_id = calls[0]['callId']
    
    try:
        call = server.get_call(call_id)
        print(f"✅ Call Details:")
        print(f"  ID: {call.get('callId')}")
        print(f"  Created: {call.get('created')}")
        print(f"  Duration: {call.get('billedDuration')}")
        print(f"  Status: {call.get('endReason')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_6_get_call_messages(server):
    """Example 6: Get call messages/transcript"""
    print("\n" + "="*50)
    print("Example 6: Get Call Messages")
    print("="*50)
    
    # First, get a call ID
    calls = server.list_calls(limit=1)
    if not calls:
        print("No calls found. Make a call first!")
        return
    
    call_id = calls[0]['callId']
    
    try:
        messages = server.get_call_messages(call_id, limit=5)
        print(f"✅ Found {len(messages)} messages")
        for msg in messages:
            role = msg.get('role', 'unknown')
            content = msg.get('content', '')[:50]
            print(f"  - {role}: {content}...")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_7_get_call_recording(server):
    """Example 7: Get call recording URL"""
    print("\n" + "="*50)
    print("Example 7: Get Call Recording")
    print("="*50)
    
    # First, get a call with recording enabled
    calls = server.list_calls(limit=10)
    call_id = None
    for call in calls:
        if call.get('recordingEnabled'):
            call_id = call['callId']
            break
    
    if not call_id:
        print("No recorded calls found. Enable recording!")
        return
    
    try:
        recording = server.get_call_recording(call_id)
        print(f"✅ Recording found:")
        print(f"  URL: {recording.get('url')[:50]}...")
        print(f"  Size: {recording.get('size')} bytes")
        print(f"  Type: {recording.get('content_type')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_8_list_voices(server):
    """Example 8: List available voices"""
    print("\n" + "="*50)
    print("Example 8: List Voices")
    print("="*50)
    
    try:
        voices = server.list_voices(limit=10)
        print(f"✅ Found {len(voices)} voices")
        for voice in voices[:5]:
            print(f"  - {voice.get('name', 'Unknown')}: {voice.get('voiceId')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_9_list_models(server):
    """Example 9: List available models"""
    print("\n" + "="*50)
    print("Example 9: List Models")
    print("="*50)
    
    try:
        models = server.list_models()
        print(f"✅ Found {len(models)} models")
        for model in models[:5]:
            print(f"  - {model}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_10_list_webhooks(server):
    """Example 10: List webhooks"""
    print("\n" + "="*50)
    print("Example 10: List Webhooks")
    print("="*50)
    
    try:
        webhooks = server.list_webhooks()
        print(f"✅ Found {len(webhooks)} webhooks")
        for webhook in webhooks:
            print(f"  - {webhook.get('webhookId')}: {webhook.get('url')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def example_11_get_account_info(server):
    """Example 11: Get account information"""
    print("\n" + "="*50)
    print("Example 11: Account Information")
    print("="*50)
    
    try:
        info = server.get_account_info()
        print(f"✅ Account Info:")
        print(f"  Org ID: {info.get('orgId')}")
        print(f"  Name: {info.get('orgName')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all examples"""
    print("\n" + "="*50)
    print("Ultravox MCP - Python Examples")
    print("="*50)
    
    # Initialize server
    server = example_1_initialize_server()
    
    # Run examples (some depend on data)
    try:
        example_2_list_agents(server)
        example_3_get_agent_details(server)
        example_4_list_calls(server)
        example_5_get_call_details(server)
        example_6_get_call_messages(server)
        example_7_get_call_recording(server)
        example_8_list_voices(server)
        example_9_list_models(server)
        example_10_list_webhooks(server)
        example_11_get_account_info(server)
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*50)
    print("Examples Complete!")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
