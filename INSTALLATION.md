# 📦 Installation Guide

Complete installation guide for all platforms.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Claude Desktop](#claude-desktop)
3. [Docker](#docker)
4. [Linux](#linux)
5. [macOS](#macos)
6. [Windows](#windows)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required

- Python 3.8 or higher (check: `python --version`)
- pip (Python package manager)
- Ultravox API key ([Get one here](https://api.ultravox.ai))
- Git (for cloning the repository)

### Optional

- Docker (for containerized setup)
- Virtual environment tool (venv - included with Python)

---

## Claude Desktop

The recommended way to use Ultravox MCP.

### Step 1: Clone Repository

```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

### Step 2: Install Dependencies

```bash
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key

```bash
# Copy example env file
cp .env.example .env

# Edit it
nano .env  # or your preferred editor
```

Add your API key:
```env
ULTRAVOX_API_KEY=your_api_key_here
DEBUG=false
LOG_LEVEL=INFO
```

### Step 5: Configure Claude Desktop

#### macOS/Linux

1. Edit the config file:
```bash
nano ~/.claude/claude_desktop_config.json
```

2. Add this configuration:
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["/absolute/path/to/Ultravox-mcp/src/server.py"]
    }
  }
}
```

**Important:** Use the ABSOLUTE path to your directory!

To get your absolute path:
```bash
pwd  # macOS/Linux
# Copy the output and use it in the config
```

#### Windows

1. Open File Explorer
2. Navigate to: `%APPDATA%\Claude`
3. Edit `claude_desktop_config.json` (create if doesn't exist)
4. Add:
```json
{
  "mcpServers": {
    "ultravox": {
      "command": "python",
      "args": ["C:\\absolute\\path\\to\\Ultravox-mcp\\src\\server.py"]
    }
  }
}
```

To get absolute path in Windows:
1. Open Command Prompt
2. Navigate to your directory
3. Type: `cd` (shows current directory)
4. Copy the path

### Step 6: Restart Claude Desktop

Close and reopen Claude Desktop. The MCP should now be connected!

### Step 7: Test

Ask Claude:
- "List my agents"
- "Show me my latest calls"
- "What tools are available?"

---

## Docker

### Step 1: Clone Repository

```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
```

### Step 2: Build Image

```bash
docker build -t ultravox-mcp:latest .
```

### Step 3: Run Container

```bash
docker run \
  -e ULTRAVOX_API_KEY="your_api_key_here" \
  -p 8000:8000 \
  ultravox-mcp:latest
```

The server will be available at `http://localhost:8000`

### Using Docker Compose

```bash
# Edit docker-compose.yml with your API key
nano docker-compose.yml

# Start the service
docker-compose up

# In another terminal, test:
curl http://localhost:8000/health
```

### View Logs

```bash
# See logs from the running container
docker logs -f <container_id>

# Or with docker-compose
docker-compose logs -f
```

---

## Linux

### Using systemd (Recommended)

1. **Prepare the environment:**
```bash
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Create systemd service:**
```bash
sudo nano /etc/systemd/system/ultravox-mcp.service
```

Add:
```ini
[Unit]
Description=Ultravox MCP Server
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/Ultravox-mcp
Environment="PATH=/home/ubuntu/Ultravox-mcp/venv/bin"
Environment="ULTRAVOX_API_KEY=your_api_key"
ExecStart=/home/ubuntu/Ultravox-mcp/venv/bin/python src/server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. **Enable and start:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable ultravox-mcp
sudo systemctl start ultravox-mcp

# Check status
sudo systemctl status ultravox-mcp

# View logs
sudo journalctl -u ultravox-mcp -f
```

---

## macOS

### Using Homebrew

```bash
# Install Python if needed
brew install python@3.11

# Clone repository
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
nano .env

# Test
python src/server.py
```

### Using LaunchAgent (Auto-start)

Create `~/Library/LaunchAgents/com.ultravox.mcp.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.ultravox.mcp</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/venv/bin/python</string>
        <string>/path/to/Ultravox-mcp/src/server.py</string>
    </array>
    <key>StandardOutPath</key>
    <string>/var/log/ultravox-mcp.log</string>
    <key>StandardErrorPath</key>
    <string>/var/log/ultravox-mcp.log</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

Then:
```bash
launchctl load ~/Library/LaunchAgents/com.ultravox.mcp.plist
```

---

## Windows

### Using PowerShell

```powershell
# Clone repository
git clone https://github.com/fullpadge/Ultravox-mcp.git
cd Ultravox-mcp

# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Configure
copy .env.example .env
notepad .env

# Test
python src/server.py
```

### Using Windows Task Scheduler

1. Create a batch file `run-ultravox.bat`:
```batch
@echo off
cd C:\path\to\Ultravox-mcp
call venv\Scripts\activate.bat
python src/server.py
```

2. Open Task Scheduler
3. Create Basic Task
4. Set trigger: "At startup"
5. Set action: Run `run-ultravox.bat`

---

## Troubleshooting

### Python not found

```bash
# Check Python installation
python --version

# If not found, install from python.org
# Or use: python3 instead of python
python3 --version
```

### Permission denied (macOS/Linux)

```bash
# Make the script executable
chmod +x src/server.py

# Or run with python explicitly
python src/server.py
```

### API Key not recognized

```bash
# Check .env file exists
cat .env

# Make sure API key is correct
# Regenerate if needed at https://api.ultravox.ai
```

### Port already in use

```bash
# Find what's using the port (Linux/macOS)
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
export MCP_PORT=9000
python src/server.py
```

### Module import errors

```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall

# Or upgrade pip first
pip install --upgrade pip
```

---

## Verify Installation

Test your installation:

```bash
# Check Python
python --version

# Check virtual environment is active
which python  # Should show /path/to/venv/bin/python

# Check API key
echo $ULTRAVOX_API_KEY

# Run the server (Ctrl+C to stop)
python src/server.py

# In another terminal, test the connection
curl http://localhost:8000/health
```

---

## Next Steps

1. Read [QUICK_START.md](../QUICK_START.md)
2. Check [CONFIGURATION.md](./CONFIGURATION.md)
3. See [examples/](../examples/)
4. Join the community in [Discussions](https://github.com/fullpadge/Ultravox-mcp/discussions)

---

**Installation complete! 🎉**
