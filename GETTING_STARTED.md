# Guide de Démarrage - Serveur MCP Ultravox

## 🚀 Démarrage rapide (5 minutes)

### Étape 1: Configurer la clé API
- Ouvre le fichier `.env` dans le dossier `ultravox-mcp`
- Remplace `REMPLACE_PAR_TA_CLE_API_ULTRAVOX` par ta vraie clé
- Sauvegarde (Ctrl + S)

### Étape 2: Ajouter à Claude Desktop
- Voir le fichier `CLAUDE_DESKTOP_CONFIG.md`

### Étape 3: Utiliser dans Claude
Écris à Claude:
```
Récupère mes appels Ultravox
```

---

## 📂 Structure du projet

```
ultravox-mcp/
├── ultravox_mcp.py           # Code principal du serveur MCP
├── .env                        # Ta clé API (SECRET - ne pas partager)
├── .gitignore                  # Fichiers à exclure de Git
├── README.md                   # Documentation
├── SETUP.md                    # Configuration détaillée
├── CLAUDE_DESKTOP_CONFIG.md    # Config Claude Desktop
├── GETTING_STARTED.md          # Ce fichier
└── .git/                       # Historique Git
```

---

## 🔧 Outils disponibles

### `list_calls(limit=20)`
Récupère les appels Ultravox
- **Paramètre**: `limit` (nombre d''appels, défaut 20)
- **Retour**: Liste des appels avec ID, date, durée, statut

### `get_call(call_id)`
Récupère les détails d''un appel
- **Paramètre**: `call_id` (ID de l''appel)
- **Retour**: Détails complets de l''appel (transcription, URL, etc)

### `list_voices()`
Récupère les voix disponibles
- **Paramètre**: Aucun
- **Retour**: Liste des voix avec ID et langue

---

## 🧪 Tests

Pour tester que tout fonctionne:

1. Ouvre une conversation Claude
2. Écris:
   ```
   Utilise le tool list_calls avec limit=5
   ```
3. Claude devrait retourner la liste de tes appels

---

## 📖 Documentation complète

Voir `README.md` et `SETUP.md` pour plus de détails.

---

## ❓ Besoin d''aide?

Regarde le fichier `SETUP.md` - section "Troubleshooting"
