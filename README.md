# Prompt Engineering Guide - Webseite

Eine moderne, responsive Webseite für den umfassenden Leitfaden zur optimalen Prompt-Formulierung für KI-Modelle.

## 👨‍💻 **Entwickler & Betreuung**

**Hauptentwickler:** A. Koc (AK Systems)
- **GitHub:** [@ak-hosting](https://github.com/ak-hosting/)
- **E-Mail:** abdullah.koc@ak-systems.de
- **Website:** [ak-pro.com](https://ak-pro.com)

**Entwickelt mit Unterstützung von:**
- KI-gestützte Entwicklung (Claude, GPT-4, Gemini)
- Eigenes Fachwissen im Prompt Engineering
- Community-Feedback und Beiträge

## 🚀 **Features**

- **Moderne Webseite** mit Flask und Bootstrap 5
- **Responsive Design** für alle Geräte
- **Docker-Integration** für einfache Bereitstellung
- **Markdown-Rendering** für alle Inhalte
- **Interaktive Elemente** mit JavaScript
- **SEO-optimiert** mit Meta-Tags
- **Kostenlose Bilder** von Unsplash
- **Mobile-optimiert** für beste Benutzerfreundlichkeit
- **Prompt-Datenbank** (in Entwicklung) - Getestete Prompts für verschiedene Bereiche

## 📋 **Voraussetzungen**

- Python 3.8+
- Docker (optional)
- Git

## 🛠️ **Installation**

### Option 1: Lokale Installation

1. **Repository klonen:**
```bash
git clone https://github.com/ak-hosting/prompt-engineering-guide
cd prompt-engineering-guide
```

2. **Virtuelle Umgebung erstellen:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate  # Windows
```

3. **Abhängigkeiten installieren:**
```bash
pip install -r requirements.txt
```

4. **Anwendung starten:**
```bash
python app.py
```

Die Webseite ist dann unter `http://localhost:5000` erreichbar.

### Option 2: Docker Installation

1. **Docker Compose verwenden:**
```bash
docker-compose up --build
```

2. **Oder Docker direkt:**
```bash
docker build -t prompt-guide .
docker run -p 5000:5000 prompt-guide
```

## 📁 **Projektstruktur**

```
prompt-engineering-guide/
├── app.py                 # Flask-Hauptanwendung
├── requirements.txt       # Python-Abhängigkeiten
├── Dockerfile            # Docker-Konfiguration
├── docker-compose.yml    # Docker Compose-Konfiguration
├── README.md             # Projekt-Dokumentation
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Beitragsrichtlinien
├── CODE_OF_CONDUCT.md    # Verhaltenskodex
├── templates/            # HTML-Templates
│   ├── base.html         # Basis-Template
│   ├── index.html        # Startseite
│   ├── content.html      # Inhaltsseiten
│   ├── about.html        # Über uns
│   └── contact.html      # Kontakt
├── static/               # Statische Dateien
│   ├── css/
│   │   └── style.css     # Custom CSS
│   └── js/
│       └── script.js     # Custom JavaScript
├── data/                 # Datenbank-Dateien
│   ├── prompts.json      # Prompt-Datenbank
│   └── categories.json   # Kategorien
└── *.md                  # Markdown-Inhalte
```

## 🎨 **Design-Features**

- **Bootstrap 5** für modernes, responsives Design
- **Bootstrap Icons** für konsistente Iconographie
- **Custom CSS** für einzigartige Styling-Anpassungen
- **Smooth Animations** für bessere UX
- **Dark/Light Mode** Unterstützung
- **Mobile-First** Design-Ansatz

## 🔧 **Technologie-Stack**

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Framework:** Bootstrap 5
- **Markdown:** Python Markdown mit Extensions
- **Container:** Docker & Docker Compose
- **Icons:** Bootstrap Icons
- **Bilder:** Unsplash (kostenlos)
- **Datenbank:** JSON-basiert (erweiterbar auf SQLite/PostgreSQL)

## 📱 **Responsive Design**

Die Webseite ist vollständig responsive und optimiert für:
- **Desktop** (1200px+)
- **Tablet** (768px - 1199px)
- **Mobile** (< 768px)

## 🚀 **Deployment**

### Heroku
```bash
heroku create prompt-engineering-guide
git push heroku main
```

### DigitalOcean App Platform
```bash
doctl apps create --spec app.yaml
```

### AWS Elastic Beanstalk
```bash
eb init
eb create
eb deploy
```

## 🔍 **SEO-Optimierung**

- Meta-Tags für alle Seiten
- Open Graph Tags für Social Media
- Strukturierte Daten (Schema.org)
- Sitemap-Generierung
- Robots.txt Konfiguration

## 📊 **Performance**

- **Lazy Loading** für Bilder
- **Minifizierte Assets** (CSS/JS)
- **CDN-Integration** für Bootstrap
- **Caching-Strategien**
- **Gzip-Kompression**

## 🔒 **Sicherheit**

- **HTTPS-Erzwingung**
- **Content Security Policy**
- **XSS-Schutz**
- **CSRF-Token**
- **Input-Validierung**

## 📈 **Analytics**

Die Webseite ist vorbereitet für:
- Google Analytics
- Google Search Console
- Hotjar für Heatmaps
- Custom Event Tracking

## 🤝 **Beitragen**

Wir freuen uns über Beiträge! Bitte lesen Sie unsere [Contributing Guidelines](CONTRIBUTING.md) und [Code of Conduct](CODE_OF_CONDUCT.md).

### Schneller Start für Beiträge:

1. **Fork das Repository**
2. **Erstelle einen Feature-Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Committe deine Änderungen**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push zum Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Erstelle einen Pull Request**

## 📄 **Lizenz**

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für Details.

## 📞 **Support**

Bei Fragen oder Problemen:
- Erstelle ein Issue auf GitHub
- Kontaktiere uns über das Kontaktformular
- E-Mail: abdullah.koc@ak-systems.de

## 🎯 **Roadmap**

### Version 1.1 (Aktuell)
- [x] Grundlegende Webseite
- [x] Markdown-Rendering
- [x] Responsive Design
- [x] Docker-Integration

### Version 1.2 (Geplant)
- [ ] Prompt-Datenbank
- [ ] Benutzer-Accounts
- [ ] Prompt-Submission System
- [ ] Kategorisierung
- [ ] Bewertungssystem

### Version 1.3 (Zukunft)
- [ ] API für externe Integrationen
- [ ] Mehrsprachige Unterstützung
- [ ] Progressive Web App (PWA)
- [ ] Dark Mode Toggle
- [ ] Erweiterte Suchfunktion

## 🙏 **Danksagungen**

- **Bootstrap Team** für das großartige Framework
- **Unsplash** für kostenlose Bilder
- **Bootstrap Icons** für die Icon-Sammlung
- **Flask Community** für das Web-Framework
- **KI-Community** für kontinuierliches Feedback

## 📊 **Projekt-Status**

![GitHub stars](https://img.shields.io/github/stars/ak-hosting/prompt-engineering-guide)
![GitHub forks](https://img.shields.io/github/forks/ak-hosting/prompt-engineering-guide)
![GitHub issues](https://img.shields.io/github/issues/ak-hosting/prompt-engineering-guide)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ak-hosting/prompt-engineering-guide)
![GitHub license](https://img.shields.io/github/license/ak-hosting/prompt-engineering-guide)

---

**Entwickelt mit ❤️ von A. Koc (AK Systems) für die KI-Community** 