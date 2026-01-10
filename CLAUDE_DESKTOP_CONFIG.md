# Configuration de Claude Desktop pour le serveur MCP Ultravox

## 🔧 Configuration manuelle (Windows)

1. **Ouvre Claude Desktop**
2. Clique sur les **trois points** (menu) en bas à gauche
3. Sélectionne **Settings**
4. Clique sur l''onglet **Developer**
5. Cherche **MCP Servers**
6. Clique sur **Add Server**

### Remplis les champs comme ceci:

| Champ | Valeur |
|-------|--------|
| **Name** | `ultravox` |
| **Type** | `command` |
| **Command** | `python C:\Users\Bloody\Documents\ultravox-mcp\ultravox_mcp.py` |
| **Environment Variables** | (laisser vide - on utilise .env) |

7. Clique **Save**
8. **Redémarre Claude Desktop complètement**

---

## ✅ Vérification

Après le redémarrage, ouvre une conversation Claude.

En bas à droite, tu devrais voir une petite pastille **"ultravox"** qui indique que le serveur MCP est connecté.

---

## 🎯 Utilisation

Une fois connecté, tu peux utiliser les outils directement:

### Exemples:

**Récupérer les appels:**
```
Montre-moi les 10 derniers appels Ultravox
```

**Récupérer les voix:**
```
Quelles sont les voix disponibles?
```

**Détails d''un appel:**
```
Donne-moi les détails de l''appel avec l''ID: call_abc123
```

---

## 🔍 Troubleshooting

### Le serveur MCP ne se lance pas

1. Ouvre une **Invite de commandes** (cmd)
2. Va dans le dossier:
   ```
   cd C:\Users\Bloody\Documents\ultravox-mcp
   ```
3. Lance le serveur manuellement:
   ```
   python ultravox_mcp.py
   ```
4. Regarde les erreurs affichées

### Erreur "ULTRAVOX_API_KEY n''est pas définie"

1. Vérifie que le fichier `.env` existe dans le dossier
2. Vérifie qu''il contient ta clé:
   ```
   ULTRAVOX_API_KEY=ta_clé_ici
   ```
3. Redémarre Claude Desktop

### Erreur "401 - Authentification échouée"

- Ta clé API est **invalide** ou **expirée**
- Vérifie dans le fichier `.env` (pas d''espaces inutiles)
- Copie une nouvelle clé depuis https://ultravox.ai

---

## 📝 Note importante

Ne mets JAMAIS ta clé API directement dans le code!
Utilise toujours le fichier `.env` pour la sécurité.
