# Linux & Docker Installation Guide / Guide d'installation Linux & Docker

---

## English

### Linux Installation (Ubuntu/Debian)

#### Step 1: Install Python

```bash
# Update package manager
sudo apt update
sudo apt upgrade -y

# Install Python 3.8+
sudo apt install python3 python3-pip python3-venv git -y

# Verify Python version
python3 --version
# Should be 3.8 or higher
```

#### Step 2: Clone and Setup

```bash
# Clone repository
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

#### Step 3: Configure API Key

```bash
# Create .env file
cp .env.example .env

# Edit with your preferred editor (nano, vim, etc.)
nano .env

# Add your API key:
# ULTRAVOX_API_KEY=your_actual_key_here

# Save and exit: Ctrl+X, Y, Enter
```

#### Step 4: Test Installation

```bash
# Make script executable
chmod +x src/server.py

# Test the server
python src/server.py

# You should see:
# MCP Server running on stdio
# Ready to receive commands...

# Press Ctrl+C to stop
```

#### Step 5: Create Systemd Service (Optional)

For automatic startup and management:

**File: `/etc/systemd/system/ultravox-mcp.service`**

```ini
[Unit]
Description=Ultravox MCP Server
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/home/your_username/ultravox-mcp-unofficial
Environment="PATH=/home/your_username/ultravox-mcp-unofficial/venv/bin"
Environment="ULTRAVOX_API_KEY=your_api_key_here"
ExecStart=/home/your_username/ultravox-mcp-unofficial/venv/bin/python src/server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Install and manage:**

```bash
# Copy service file (requires sudo)
sudo cp ultravox-mcp.service /etc/systemd/system/

# Enable service (auto-start on boot)
sudo systemctl enable ultravox-mcp

# Start service
sudo systemctl start ultravox-mcp

# Check status
sudo systemctl status ultravox-mcp

# View logs
sudo journalctl -u ultravox-mcp -f

# Stop service
sudo systemctl stop ultravox-mcp
```

---

### Docker Installation

#### Step 1: Install Docker

```bash
# Install Docker (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to docker group (optional)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
```

#### Step 2: Clone Repository

```bash
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial
```

#### Step 3: Build Docker Image

```bash
# Build image with tag
docker build -t ultravox-mcp:latest .

# Verify build
docker images | grep ultravox-mcp
```

#### Step 4: Run Container

**Option A: Simple run**

```bash
docker run \
  -e ULTRAVOX_API_KEY="your_api_key_here" \
  -p 8000:8000 \
  ultravox-mcp:latest
```

**Option B: Run with .env file**

```bash
docker run \
  --env-file .env \
  -p 8000:8000 \
  ultravox-mcp:latest
```

**Option C: Run in background (daemon mode)**

```bash
docker run -d \
  --name ultravox-mcp \
  --env-file .env \
  -p 8000:8000 \
  ultravox-mcp:latest

# View logs
docker logs -f ultravox-mcp

# Stop container
docker stop ultravox-mcp

# Remove container
docker rm ultravox-mcp
```

---

### Docker Compose (Recommended)

For easier management with multiple services:

**File: `docker-compose.yml`**

```yaml
version: '3.8'

services:
  ultravox-mcp:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: ultravox-mcp
    environment:
      - ULTRAVOX_API_KEY=${ULTRAVOX_API_KEY}
      - DEBUG=${DEBUG:-false}
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
    ports:
      - "8000:8000"
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

**Usage:**

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild image
docker-compose up -d --build
```

---

### Kubernetes Deployment (Advanced)

**File: `k8s/deployment.yaml`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ultravox-mcp
  labels:
    app: ultravox-mcp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ultravox-mcp
  template:
    metadata:
      labels:
        app: ultravox-mcp
    spec:
      containers:
      - name: ultravox-mcp
        image: ultravox-mcp:latest
        ports:
        - containerPort: 8000
        env:
        - name: ULTRAVOX_API_KEY
          valueFrom:
            secretKeyRef:
              name: ultravox-secret
              key: api-key
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
---
apiVersion: v1
kind: Secret
metadata:
  name: ultravox-secret
type: Opaque
stringData:
  api-key: your_api_key_here
```

**Deploy:**

```bash
# Create secret
kubectl create secret generic ultravox-secret --from-literal=api-key=your_key

# Deploy
kubectl apply -f k8s/deployment.yaml

# Check deployment
kubectl get deployment ultravox-mcp

# View logs
kubectl logs deployment/ultravox-mcp
```

---

## Français

### Installation Linux (Ubuntu/Debian)

#### Étape 1 : Installer Python

```bash
# Mettre à jour le gestionnaire de paquets
sudo apt update
sudo apt upgrade -y

# Installer Python 3.8+
sudo apt install python3 python3-pip python3-venv git -y

# Vérifier la version de Python
python3 --version
```

#### Étape 2 : Cloner et configurer

```bash
# Cloner le dépôt
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

#### Étape 3 : Configurer la clé API

```bash
# Créer un fichier .env
cp .env.example .env

# Éditer avec votre éditeur préféré
nano .env

# Ajouter votre clé API:
# ULTRAVOX_API_KEY=votre_clé_ici

# Sauvegarder: Ctrl+X, Y, Entrée
```

#### Étape 4 : Tester l'installation

```bash
# Rendre le script exécutable
chmod +x src/server.py

# Tester le serveur
python src/server.py

# Vous devriez voir:
# MCP Server running on stdio
# Ready to receive commands...

# Arrêter avec Ctrl+C
```

#### Étape 5 : Créer un service Systemd (Optionnel)

Pour démarrage automatique:

```bash
# Créer le fichier de service
sudo nano /etc/systemd/system/ultravox-mcp.service

# Ajouter le contenu (voir exemple anglais)

# Activer le service
sudo systemctl enable ultravox-mcp
sudo systemctl start ultravox-mcp

# Vérifier le statut
sudo systemctl status ultravox-mcp
```

---

### Installation Docker

#### Étape 1 : Installer Docker

```bash
# Installer Docker (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Vérifier l'installation
docker --version
```

#### Étape 2 : Cloner le dépôt

```bash
git clone https://github.com/mak3it-org/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial
```

#### Étape 3 : Construire l'image Docker

```bash
docker build -t ultravox-mcp:latest .
```

#### Étape 4 : Exécuter le conteneur

**Avec variable d'environnement :**

```bash
docker run \
  -e ULTRAVOX_API_KEY="votre_clé" \
  -p 8000:8000 \
  ultravox-mcp:latest
```

**Avec fichier .env :**

```bash
docker run \
  --env-file .env \
  -p 8000:8000 \
  ultravox-mcp:latest
```

**Mode détaché (en arrière-plan) :**

```bash
docker run -d \
  --name ultravox-mcp \
  --env-file .env \
  -p 8000:8000 \
  ultravox-mcp:latest
```

---

### Docker Compose (Recommandé)

**Fichier: `docker-compose.yml`**

```yaml
version: '3.8'

services:
  ultravox-mcp:
    build: .
    container_name: ultravox-mcp
    environment:
      - ULTRAVOX_API_KEY=${ULTRAVOX_API_KEY}
    ports:
      - "8000:8000"
    restart: unless-stopped
```

**Utilisation:**

```bash
# Démarrer
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter
docker-compose down
```

---

## Troubleshooting

### Error: "Module not found"

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

### Error: "Permission denied"

**Solution:**
```bash
# Make script executable
chmod +x src/server.py

# For systemd service, ensure correct user/group
```

### Docker image build fails

**Solution:**
```bash
# Clean up old images
docker system prune -a

# Rebuild with verbose output
docker build -t ultravox-mcp --progress=plain .
```

### Port already in use

**Solution:**
```bash
# Find process on port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
docker run -p 8001:8000 ultravox-mcp:latest
```

---

## Next Steps

- [API Reference](../docs/API_REFERENCE.md)
- [Deployment Guide](../docs/DEPLOYMENT.md)
- [Configuration Options](../docs/CONFIGURATION.md)
