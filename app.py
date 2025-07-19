from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import markdown
import os
from datetime import datetime
from api_routes import create_api_routes
# from celery import Celery

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Celery Konfiguration (temporär deaktiviert)
# app.config['CELERY_BROKER_URL'] = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
# app.config['CELERY_RESULT_BACKEND'] = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

# celery = Celery('ai_guide', broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# API Routes registrieren
create_api_routes(app)

# Markdown-Dateien laden und parsen
def load_markdown_content():
    content = {}
    markdown_files = {
        'intro': 'README.md',
        'grundlagen': '01-grundlegende-prinzipien.md',
        'techniken': '02-fortgeschrittene-techniken.md',
        'anwendungen': '03-anwendungsfaelle.md',
        'plattformen': '04-plattform-optimierung.md',
        'best-practices': '05-best-practices.md',
        'beispiele': '06-praktische-beispiele.md',
        'fazit': 'fazit.md'
    }
    
    for key, filename in markdown_files.items():
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content[key] = markdown.markdown(file.read(), extensions=['tables', 'fenced_code', 'codehilite'])
        except FileNotFoundError:
            content[key] = f"<p>Datei {filename} nicht gefunden.</p>"
    
    return content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grundlagen')
def grundlagen():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Grundlegende Prinzipien", 
                         content=content.get('grundlagen', ''),
                         active_page='grundlagen')

@app.route('/techniken')
def techniken():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Fortgeschrittene Techniken", 
                         content=content.get('techniken', ''),
                         active_page='techniken')

@app.route('/anwendungen')
def anwendungen():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Anwendungsfälle", 
                         content=content.get('anwendungen', ''),
                         active_page='anwendungen')

@app.route('/plattformen')
def plattformen():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Plattform-Optimierung", 
                         content=content.get('plattformen', ''),
                         active_page='plattformen')

@app.route('/best-practices')
def best_practices():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Best Practices", 
                         content=content.get('best-practices', ''),
                         active_page='best-practices')

@app.route('/beispiele')
def beispiele():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Praktische Beispiele", 
                         content=content.get('beispiele', ''),
                         active_page='beispiele')

@app.route('/fazit')
def fazit():
    content = load_markdown_content()
    return render_template('content.html', 
                         title="Fazit", 
                         content=content.get('fazit', ''),
                         active_page='fazit')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

@app.route('/sw.js')
def service_worker():
    return app.send_static_file('sw.js')

@app.route('/offline')
def offline():
    return render_template('offline.html')

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': os.environ.get('APP_VERSION', '1.0.0'),
        'app_name': os.environ.get('APP_NAME', 'AI Guide')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 