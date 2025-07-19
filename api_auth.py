from flask import Flask, request, jsonify
from functools import wraps
import jwt
import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Simulierte Benutzerdatenbank
users_db = {
    'admin@ak-pro.com': {
        'password': generate_password_hash('admin123'),
        'role': 'admin',
        'name': 'A. Koc'
    }
}

# Simulierte API-Schlüssel
api_keys = {
    'ak-pro-api-key-2024': {
        'user': 'admin@ak-pro.com',
        'permissions': ['read', 'write', 'admin']
    }
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token fehlt!'}), 401
        
        try:
            token = token.split(' ')[1]  # Bearer token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = users_db.get(data['email'])
            
            if not current_user:
                return jsonify({'message': 'Ungültiger Token!'}), 401
                
        except:
            return jsonify({'message': 'Ungültiger Token!'}), 401
            
        return f(current_user, *args, **kwargs)
    
    return decorated

def api_key_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            return jsonify({'message': 'API-Schlüssel fehlt!'}), 401
        
        if api_key not in api_keys:
            return jsonify({'message': 'Ungültiger API-Schlüssel!'}), 401
            
        return f(api_keys[api_key], *args, **kwargs)
    
    return decorated

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'E-Mail und Passwort erforderlich!'}), 400
    
    user = users_db.get(data['email'])
    
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'message': 'Ungültige Anmeldedaten!'}), 401
    
    token = jwt.encode({
        'email': data['email'],
        'role': user['role'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({
        'token': token,
        'user': {
            'email': data['email'],
            'name': user['name'],
            'role': user['role']
        }
    })

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'E-Mail und Passwort erforderlich!'}), 400
    
    if data['email'] in users_db:
        return jsonify({'message': 'Benutzer existiert bereits!'}), 400
    
    users_db[data['email']] = {
        'password': generate_password_hash(data['password']),
        'role': 'user',
        'name': data.get('name', '')
    }
    
    return jsonify({'message': 'Benutzer erfolgreich registriert!'}), 201

@app.route('/api/prompts', methods=['GET'])
@api_key_required
def get_prompts(api_key_data):
    # Simulierte Prompt-Daten
    prompts = [
        {
            'id': 1,
            'title': 'Content Creation Prompt',
            'description': 'Erstellt hochwertige Inhalte',
            'platform': 'ChatGPT',
            'category': 'Content Creation',
            'prompt': 'Erstelle einen Artikel über...',
            'rating': 4.5,
            'usage_count': 1250
        },
        {
            'id': 2,
            'title': 'Code Generation Prompt',
            'description': 'Generiert sauberen Code',
            'platform': 'Gemini',
            'category': 'Programming',
            'prompt': 'Schreibe eine Funktion, die...',
            'rating': 4.8,
            'usage_count': 890
        }
    ]
    
    return jsonify({
        'prompts': prompts,
        'total': len(prompts),
        'api_user': api_key_data['user']
    })

@app.route('/api/prompts', methods=['POST'])
@token_required
def create_prompt(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Keine Berechtigung!'}), 403
    
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('prompt'):
        return jsonify({'message': 'Titel und Prompt erforderlich!'}), 400
    
    # Hier würde normalerweise die Datenbank gespeichert werden
    new_prompt = {
        'id': 3,
        'title': data['title'],
        'description': data.get('description', ''),
        'platform': data.get('platform', 'All'),
        'category': data.get('category', 'General'),
        'prompt': data['prompt'],
        'rating': 0,
        'usage_count': 0,
        'created_by': current_user['name'],
        'created_at': datetime.datetime.utcnow().isoformat()
    }
    
    return jsonify({
        'message': 'Prompt erfolgreich erstellt!',
        'prompt': new_prompt
    }), 201

@app.route('/api/analytics', methods=['GET'])
@token_required
def get_analytics(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Keine Berechtigung!'}), 403
    
    # Simulierte Analytics-Daten
    analytics = {
        'total_visitors': 15420,
        'unique_visitors': 8920,
        'page_views': 45680,
        'avg_session_duration': '4m 32s',
        'bounce_rate': '23.4%',
        'top_pages': [
            {'page': '/', 'views': 12500},
            {'page': '/grundlagen', 'views': 8900},
            {'page': '/techniken', 'views': 7200}
        ],
        'top_prompts': [
            {'prompt': 'Content Creation', 'usage': 1250},
            {'prompt': 'Code Generation', 'usage': 890},
            {'prompt': 'Data Analysis', 'usage': 650}
        ]
    }
    
    return jsonify(analytics)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001) 