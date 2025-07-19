from flask import Flask, jsonify, request
import json
import os

def create_api_routes(app):
    """API Routes für die Prompt-Datenbank"""
    
    @app.route('/api/prompts', methods=['GET'])
    def get_prompts():
        """Alle Prompts abrufen mit Filter-Optionen"""
        try:
            with open('data/prompts.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Filter-Parameter
            category = request.args.get('category')
            platform = request.args.get('platform')
            difficulty = request.args.get('difficulty')
            author = request.args.get('author')
            search = request.args.get('search')
            
            prompts = data['prompts']
            
            # Filter anwenden
            if category:
                prompts = [p for p in prompts if p['category'] == category]
            if platform:
                prompts = [p for p in prompts if platform in p['platform']]
            if difficulty:
                prompts = [p for p in prompts if p['difficulty'] == difficulty]
            if author:
                prompts = [p for p in prompts if author.lower() in p['author'].lower()]
            if search:
                search_lower = search.lower()
                prompts = [p for p in prompts if 
                          search_lower in p['title'].lower() or 
                          search_lower in p['description'].lower() or 
                          search_lower in p['tags']]
            
            return jsonify({
                'success': True,
                'data': prompts,
                'count': len(prompts)
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/prompts/<prompt_id>', methods=['GET'])
    def get_prompt(prompt_id):
        """Einen spezifischen Prompt abrufen"""
        try:
            with open('data/prompts.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            prompt = next((p for p in data['prompts'] if p['id'] == prompt_id), None)
            
            if prompt:
                return jsonify({
                    'success': True,
                    'data': prompt
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Prompt nicht gefunden'
                }), 404
                
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/prompts', methods=['POST'])
    def create_prompt():
        """Neuen Prompt erstellen"""
        try:
            data = request.get_json()
            
            # Validierung
            required_fields = ['title', 'description', 'category', 'platform', 'prompt']
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'success': False,
                        'error': f'Feld "{field}" ist erforderlich'
                    }), 400
            
            # Neue ID generieren
            import uuid
            prompt_id = f"prompt-{uuid.uuid4().hex[:8]}"
            
            new_prompt = {
                'id': prompt_id,
                'title': data['title'],
                'description': data['description'],
                'category': data['category'],
                'subcategory': data.get('subcategory', ''),
                'platform': data['platform'],
                'prompt': data['prompt'],
                'example_output': data.get('example_output', ''),
                'tags': data.get('tags', []),
                'author': data.get('author', 'Community'),
                'rating': 0.0,
                'usage_count': 0,
                'created_date': datetime.now().strftime('%Y-%m-%d'),
                'last_updated': datetime.now().strftime('%Y-%m-%d'),
                'difficulty': data.get('difficulty', 'intermediate'),
                'estimated_time': data.get('estimated_time', '5-10 minutes')
            }
            
            # Zur Datenbank hinzufügen (hier vereinfacht)
            return jsonify({
                'success': True,
                'data': new_prompt,
                'message': 'Prompt erfolgreich erstellt'
            }), 201
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/categories', methods=['GET'])
    def get_categories():
        """Alle Kategorien abrufen"""
        try:
            with open('data/prompts.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return jsonify({
                'success': True,
                'data': data['categories']
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/platforms', methods=['GET'])
    def get_platforms():
        """Alle Plattformen abrufen"""
        try:
            with open('data/prompts.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return jsonify({
                'success': True,
                'data': data['platforms']
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/stats', methods=['GET'])
    def get_stats():
        """Statistiken abrufen"""
        try:
            with open('data/prompts.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            prompts = data['prompts']
            
            stats = {
                'total_prompts': len(prompts),
                'categories': len(data['categories']),
                'platforms': len(data['platforms']),
                'total_usage': sum(p['usage_count'] for p in prompts),
                'avg_rating': sum(p['rating'] for p in prompts) / len(prompts) if prompts else 0,
                'top_categories': {},
                'top_platforms': {}
            }
            
            # Top Kategorien
            for prompt in prompts:
                category = prompt['category']
                stats['top_categories'][category] = stats['top_categories'].get(category, 0) + 1
            
            # Top Plattformen
            for prompt in prompts:
                for platform in prompt['platform']:
                    stats['top_platforms'][platform] = stats['top_platforms'].get(platform, 0) + 1
            
            return jsonify({
                'success': True,
                'data': stats
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

# Import für datetime
from datetime import datetime 