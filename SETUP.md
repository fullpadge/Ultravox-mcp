# Configuration du Serveur MCP Ultravox dans Claude Desktop

## Étape 1 : Mettre ta clé API

1. Ouvre le dossier `C:\Users\Bloody\Documents\ultravox-mcp`
2. Double-clique sur le fichier `.env`
3. Remplace `REMPLACE_PAR_TA_CLE_API_ULTRAVOX` par ta vraie clé API Ultravox
4. Sauvegarde (Ctrl + S)

**Exemple** :
```
ULTRAVOX_API_KEY=sk_live_abc123def456xyz789
```

## Étape 2 : Ajouter à Claude Desktop

### Windows

1. Ouvre Claude Desktop
2. En bas à gauche, clique sur les **trois points** (menu)
3. Sélectionne « Settings »
4. Clique sur l'onglet « Developer »
5. Cherche « MCP Servers »
6. Clique sur « Add Server »

Remplis les champs :
- **Name** : `ultravox`
- **Type** : `command`
- **Command** : 
  ```
  python C:\Users\Bloody\Documents\ultravox-mcp\ultravox_mcp.py
  ```

Laisse les autres champs vides et clique « Save ».

7. Redémarre Claude Desktop

## Étape 3 : Vérifier que ça marche

Une fois Claude redémarré, ouvre une conversation.

En bas à droite, tu devrais voir une petite pastille « ultravox » qui indique que le serveur est connecté.

## Étape 4 : Utiliser dans Claude

Écris simplement à Claude :

```
Récupère la liste de mes 10 derniers appels Ultravox
```

Claude utilisera automatiquement le tool `list_calls`.

Autres exemples :
- "Quelles sont les voix disponibles?"
- "Donne-moi les détails de l'appel call_abc123"

## Troubleshooting

### Erreur "ULTRAVOX_API_KEY n'est pas définie"
- Vérifie que tu as bien rempli le fichier `.env`
- Redémarre Claude Desktop

### Erreur "401 - Authentification échouée"
- Ta clé API est incorrecte
- Vérifie dans le fichier `.env` (pas d'espaces inutiles)

### Le serveur ne démarre pas
- Ouvre une CMD dans `C:\Users\Bloody\Documents\ultravox-mcp`
- Tape : `python ultravox_mcp.py`
- Regarde les erreurs affichées
