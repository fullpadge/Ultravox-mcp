import os
import httpx
from dotenv import load_dotenv

# Charge la clé depuis .env
load_dotenv()
api_key = os.getenv('ULTRAVOX_API_KEY')

if not api_key:
    print('❌ ERREUR: Clé API non définie!')
    exit(1)

print(f'🔑 Clé API trouvée: {api_key[:15]}...')
print(f'Longueur: {len(api_key)} caractères')

headers = {
    'X-API-Key': api_key,
    'Content-Type': 'application/json',
}

# Test 1: Appels
print('\n' + '='*50)
print('📞 TEST 1: Récupération des appels')
print('='*50)
try:
    with httpx.Client() as client:
        response = client.get(
            'https://api.ultravox.ai/api/calls',
            headers=headers,
            params={'limit': 3},
            timeout=10.0
        )
    
    print(f'✅ Statut HTTP: {response.status_code}')
    
    if response.status_code == 200:
        data = response.json()
        calls = data.get('data', data) if isinstance(data, dict) else data
        
        if isinstance(calls, list):
            print(f'✅ {len(calls)} appels trouvés')
            for i, call in enumerate(calls[:3], 1):
                call_id = call.get('id', 'N/A')
                status = call.get('status', 'N/A')
                created = call.get('createdAt', call.get('created_at', 'N/A'))
                print(f'  [{i}] ID: {call_id} | Status: {status} | Date: {created}')
        else:
            print(f'Format: {type(calls)}')
            
    elif response.status_code == 401:
        print('❌ Erreur 401: Clé API invalide ou expirée')
    else:
        print(f'❌ Erreur {response.status_code}')
        print(f'Réponse: {response.text[:200]}')
        
except httpx.TimeoutException:
    print('❌ Timeout: Connexion trop lente')
except Exception as e:
    print(f'❌ Erreur: {type(e).__name__}: {str(e)}')

# Test 2: Voix
print('\n' + '='*50)
print('🎤 TEST 2: Récupération des voix')
print('='*50)
try:
    with httpx.Client() as client:
        response = client.get(
            'https://api.ultravox.ai/api/voices',
            headers=headers,
            timeout=10.0
        )
    
    print(f'✅ Statut HTTP: {response.status_code}')
    
    if response.status_code == 200:
        data = response.json()
        voices = data.get('data', data) if isinstance(data, dict) else data
        
        if isinstance(voices, list):
            print(f'✅ {len(voices)} voix trouvées')
            for i, voice in enumerate(voices[:3], 1):
                name = voice.get('name', voice.get('voiceName', voice.get('id', 'N/A')))
                lang = voice.get('language', 'N/A')
                print(f'  [{i}] {name} (lang: {lang})')
        else:
            print(f'Format: {type(voices)}')
            
    elif response.status_code == 401:
        print('❌ Erreur 401: Clé API invalide')
    else:
        print(f'❌ Erreur {response.status_code}')
        print(f'Réponse: {response.text[:200]}')
        
except Exception as e:
    print(f'❌ Erreur: {type(e).__name__}: {str(e)}')

print('\n' + '='*50)
print('✅ Tests terminés!')
print('='*50)
