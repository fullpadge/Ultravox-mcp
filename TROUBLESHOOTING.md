# 🆘 Troubleshooting Guide

Solutions to common issues.

## Installation Issues

### "Python not found" or "command: python: not found"

**Solution:**
```bash
# Check if Python is installed
python3 --version

# If not found, install:
# macOS: brew install python@3.11
# Ubuntu: sudo apt install python3 python3-pip
# Windows: Download from python.org

# Use python3 instead of python
python3 -m venv venv
python3 -r install requirements.txt
```

### "pip: command not found"

**Solution:**
```bash
# pip should come with Python
python3 -m pip --version

# Install pip if missing
python3 -m ensurepip --upgrade

# Or use:
python3 -m pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named..."

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\Activate  # Windows

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# Check installed packages
pip list
```

### "Permission denied" on script execution

**Solution:**
```bash
# Make script executable
chmod +x src/server.py

# Or run with python explicitly
python src/server.py
```

---

## Configuration Issues

### "ULTRAVOX_API_KEY not found"

**Solution:**
```bash
# Check if .env exists
ls -la .env

# Check file content
cat .env

# Make sure it has:
# ULTRAVOX_API_KEY=your_actual_key

# Not this:
# ULTRAVOX_API_KEY=your_api_key_here (that's just a placeholder!)

# Set environment variable directly if needed
export ULTRAVOX_API_KEY="your_actual_key"
```

### API Key invalid or rejected

**Solution:**
```bash
# Get a new key from https://api.ultravox.ai
# Make sure key doesn't have extra whitespace

# Test the key
curl -H "Authorization: Bearer YOUR_KEY" \
  https://api.ultravox.ai/v1/agents

# If it doesn't work, regenerate in the dashboard
```

### .env file not loading

**Solution:**
```bash
# Make sure you use python-dotenv
pip install python-dotenv

# Check that your code loads it
from dotenv import load_dotenv
load_dotenv()

# Verify it's in the right directory
# Should be in: /path/to/Ultravox-mcp/.env
```

---

## Claude Desktop Issues

### MCP not connecting to Claude

**Solution:**

1. Check config file path:
   ```bash
   # macOS/Linux
   cat ~/.claude/claude_desktop_config.json
   
   # Windows
   type %APPDATA%\Claude\claude_desktop_config.json
   ```

2. Verify absolute path is correct:
   ```bash
   # Get your absolute path
   pwd  # macOS/Linux
   # cd to folder and copy the path
   ```

3. Check syntax of JSON:
   ```bash
   # Use an online JSON validator or:
   python -m json.tool claude_desktop_config.json
   ```

4. Restart Claude Desktop completely:
   - Close all Claude windows
   - Wait 10 seconds
   - Reopen Claude

### "Failed to connect to MCP server"

**Solution:**
```bash
# Make sure server is running
python src/server.py

# Check for errors in output

# Try with absolute paths in config:
/home/user/Ultravox-mcp/src/server.py
# Not relative paths:
./Ultravox-mcp/src/server.py
```

### Tools not appearing in Claude

**Solution:**
```bash
# 1. Verify server is running
python src/server.py
# Should see: "MCP Server started successfully"

# 2. Check for errors in terminal
# If you see errors, fix them first

# 3. Restart Claude Desktop after fixing

# 4. Ask Claude: "What MCP tools do you have access to?"
```

---

## Runtime Issues

### Server crashes immediately

**Solution:**
```bash
# Run with explicit error output
python src/server.py

# Look for the error message
# Common issues:
# - Wrong API key
# - Python version too old
# - Missing dependencies

# Fix and restart
```

### Server hangs/freezes

**Solution:**
```bash
# Press Ctrl+C to stop
# Check for:
# - Network issues
# - API key invalid
# - Too many concurrent requests

# Restart and try again
python src/server.py
```

### API calls timeout

**Solution:**
```bash
# Increase timeout in code
# In src/server.py or your config:
REQUEST_TIMEOUT = 60  # seconds instead of 30

# Or check:
# - Internet connection
# - Ultravox API status
# - API quota limits
```

### Memory issues

**Solution:**
```bash
# Monitor memory usage
python -m memory_profiler src/server.py

# Issues:
# - Large number of calls stored in memory
# - Caching not working properly
# - Memory leak in loop

# Solution: Implement pagination
calls = server.list_calls(limit=100)  # Not all at once
```

---

## Docker Issues

### "docker: command not found"

**Solution:**
```bash
# Install Docker from https://docker.com
# On Linux:
sudo apt install docker.io

# Check installation
docker --version
```

### Container exits immediately

**Solution:**
```bash
# Check logs
docker logs <container_id>

# Common issues:
# - Missing API key: -e ULTRAVOX_API_KEY="..."
# - Port already in use: -p 9000:8000
# - Invalid base image

# Run with more details
docker run --it ultravox-mcp:latest
```

### "port 8000 is already allocated"

**Solution:**
```bash
# Use different port
docker run -p 9000:8000 ultravox-mcp:latest

# Or kill the other container
docker stop <container_id>
docker rm <container_id>

# Or find what's using port 8000
lsof -i :8000
kill -9 <PID>
```

### Docker Compose not starting

**Solution:**
```bash
# Check syntax
docker-compose config

# See the error
docker-compose up --no-detach

# Check .env file exists
ls -la .env

# Rebuild image
docker-compose build --no-cache
```

---

## Network Issues

### "Connection refused"

**Solution:**
```bash
# Make sure server is running
ps aux | grep "python.*server.py"

# Start it if not running
python src/server.py

# Check if it's listening on port 8000
netstat -tlnp | grep 8000
# or
ss -tlnp | grep 8000
```

### "Host unreachable"

**Solution:**
```bash
# Check Internet connection
ping google.com

# Check API endpoint is reachable
curl https://api.ultravox.ai/v1/agents

# If it fails, Ultravox API might be down
# Check: https://status.ultravox.ai
```

### Slow responses

**Solution:**
```bash
# 1. Check your internet speed
# 2. Reduce request size (use limit parameter)
calls = server.list_calls(limit=10)  # not limit=1000

# 3. Add caching
# 4. Check Ultravox API status
# 5. Use fewer concurrent requests
```

---

## Platform-Specific Issues

### macOS Specific

**Code Signing issues:**
```bash
# Allow unsigned Python scripts
xattr -d com.apple.quarantine src/server.py

# Or use brew Python
brew install python@3.11
```

**Permission issues:**
```bash
# Make sure you have permission to ~/. claude
chmod 755 ~/.claude
```

### Linux Specific

**systemd service not starting:**
```bash
# Check service status
sudo systemctl status ultravox-mcp

# See full error
sudo journalctl -u ultravox-mcp -n 50

# Common issues:
# - Wrong user in service file
# - Wrong path to venv
# - Missing environment variables
```

### Windows Specific

**PowerShell execution policy:**
```powershell
# If you get "cannot be loaded because running scripts is disabled"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Path with spaces:**
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\Users\\My User\\Ultravox-mcp\\src\\server.py"]
    }
  }
}
```

---

## Getting Help

### Before asking for help:

1. Check this guide
2. Read [CONFIGURATION.md](./CONFIGURATION.md)
3. Check server logs
4. Try with a simple test case
5. Search existing [GitHub Issues](https://github.com/fullpadge/Ultravox-mcp/issues)

### When asking for help:

Include:
- Your OS and Python version: `python --version`
- The full error message
- Steps to reproduce
- Relevant config (with API key removed!)
- What you've already tried

### Where to ask:

- [GitHub Issues](https://github.com/fullpadge/Ultravox-mcp/issues) - for bugs
- [GitHub Discussions](https://github.com/fullpadge/Ultravox-mcp/discussions) - for questions

---

**Still stuck? Create an issue with details!** 🆘
