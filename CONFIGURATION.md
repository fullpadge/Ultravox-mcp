# ⚙️ Configuration Guide

Advanced configuration options for Ultravox MCP.

## Environment Variables

Create a `.env` file in the project root:

```env
# Required
ULTRAVOX_API_KEY=your_api_key_here

# Optional
DEBUG=false
LOG_LEVEL=INFO
MCP_PORT=8000
```

### ULTRAVOX_API_KEY

Your Ultravox API key. Get one at: https://api.ultravox.ai

```env
ULTRAVOX_API_KEY=abc123def456...
```

### DEBUG

Enable debug mode for detailed logging:

```env
DEBUG=true  # Enable debug mode
DEBUG=false # Disable debug mode (default)
```

### LOG_LEVEL

Set logging verbosity:

```env
LOG_LEVEL=DEBUG   # Most verbose
LOG_LEVEL=INFO    # Normal (default)
LOG_LEVEL=WARNING # Only warnings
LOG_LEVEL=ERROR   # Only errors
```

### MCP_PORT

Port for the HTTP wrapper (if using):

```env
MCP_PORT=8000  # Default port
```

## Claude Desktop Configuration

Edit `~/.claude/claude_desktop_config.json`:

### Minimal Configuration

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

### With Environment Variables

```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/path/to/Ultravox-mcp/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "your_key",
        "LOG_LEVEL": "INFO",
        "DEBUG": "false"
      }
    }
  }
}
```

### Multiple Instances

```json
{
  "mcpServers": {
    "ultravox-prod": {
      "command": "python",
      "args": ["/path/to/prod/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "prod_key",
        "DEBUG": "false"
      }
    },
    "ultravox-dev": {
      "command": "python",
      "args": ["/path/to/dev/src/server.py"],
      "env": {
        "ULTRAVOX_API_KEY": "dev_key",
        "DEBUG": "true"
      }
    }
  }
}
```

## Docker Configuration

### Basic Docker Run

```bash
docker run \
  -e ULTRAVOX_API_KEY="your_key" \
  -e LOG_LEVEL="INFO" \
  -p 8000:8000 \
  ultravox-mcp:latest
```

### Docker Compose

Edit `docker-compose.yml`:

```yaml
version: '3.8'

services:
  ultravox-mcp:
    build: .
    environment:
      ULTRAVOX_API_KEY: ${ULTRAVOX_API_KEY}
      LOG_LEVEL: INFO
      DEBUG: "false"
    ports:
      - "8000:8000"
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

Usage:

```bash
# Create .env with your API key
echo "ULTRAVOX_API_KEY=your_key" > .env

# Start
docker-compose up

# Stop
docker-compose down
```

## Python Configuration

Import and configure programmatically:

```python
import os
from dotenv import load_dotenv
from src.server import UltravoxMCPServer

# Load environment variables
load_dotenv()

# Configure
api_key = os.getenv('ULTRAVOX_API_KEY')
debug = os.getenv('DEBUG', 'false').lower() == 'true'
log_level = os.getenv('LOG_LEVEL', 'INFO')

# Initialize server
server = UltravoxMCPServer(
    api_key=api_key,
    debug=debug,
    log_level=log_level
)

# Use the server
agents = server.list_agents()
```

## Security Best Practices

### 1. Keep API Keys Secret

Never commit `.env` to git:

```bash
# .gitignore
.env
.env.local
*.key
```

### 2. Use Environment Variables

Instead of hardcoding:

```python
# Bad
API_KEY = "abc123"

# Good
API_KEY = os.getenv('ULTRAVOX_API_KEY')
```

### 3. Rotate Keys Regularly

Change your API key periodically in the Ultravox dashboard.

### 4. Use .env.example

Commit a safe template:

```env
# .env.example (safe to commit)
ULTRAVOX_API_KEY=your_api_key_here
LOG_LEVEL=INFO
DEBUG=false
```

### 5. Restrict File Permissions

```bash
chmod 600 .env  # Only user can read
```

## Performance Tuning

### Connection Pooling

```python
# For high-volume scenarios
server = UltravoxMCPServer(
    api_key=api_key,
    max_connections=10,
    timeout=30
)
```

### Caching

```python
# Cache agent list for 5 minutes
agents = server.list_agents(cache_ttl=300)
```

### Batch Operations

```python
# Get multiple calls at once
call_ids = ["call1", "call2", "call3"]
calls = server.get_calls_batch(call_ids)
```

## Logging

### View Logs

```bash
# Python logging
python -c "import logging; logging.basicConfig(level=logging.DEBUG)"

# Docker logs
docker logs -f <container_id>

# Systemd logs
sudo journalctl -u ultravox-mcp -f
```

### Log Files

```bash
# Create a log file
export LOG_FILE=/var/log/ultravox-mcp.log

# View tail
tail -f /var/log/ultravox-mcp.log
```

## Advanced Configuration

### Custom Timeouts

```python
# In src/server.py or your config
REQUEST_TIMEOUT = 30  # seconds
CONNECT_TIMEOUT = 10  # seconds
```

### Rate Limiting

```env
RATE_LIMIT=100  # requests per minute
RATE_LIMIT_WINDOW=60  # seconds
```

### Proxy Configuration

```env
HTTP_PROXY=http://proxy.example.com:8080
HTTPS_PROXY=https://proxy.example.com:8080
NO_PROXY=localhost,127.0.0.1
```

## Troubleshooting Configuration

### Configuration not loading

```bash
# Check if .env exists
ls -la .env

# Print current environment
printenv | grep ULTRAVOX

# Verify path
pwd
```

### Wrong API key

```bash
# Test the key
curl -H "Authorization: Bearer YOUR_KEY" \
  https://api.ultravox.ai/v1/agents
```

### Port conflicts

```bash
# Find process using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or use different port
export MCP_PORT=9000
```

---

**Need help? Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)**
