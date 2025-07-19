# Contributing Guidelines

Vielen Dank für Ihr Interesse am Prompt Engineering Guide! Wir freuen uns über alle Beiträge, die das Projekt verbessern.

## 🤝 **Wie Sie beitragen können**

### **1. Bug Reports**
- Verwenden Sie das GitHub Issue Template
- Beschreiben Sie das Problem klar und detailliert
- Fügen Sie Schritte zur Reproduktion hinzu
- Geben Sie Informationen über Ihr System an

### **2. Feature Requests**
- Erklären Sie das gewünschte Feature
- Begründen Sie, warum es nützlich wäre
- Schlagen Sie eine mögliche Implementierung vor
- Prüfen Sie, ob es bereits ein ähnliches Issue gibt

### **3. Code Contributions**
- Fork das Repository
- Erstellen Sie einen Feature-Branch
- Schreiben Sie sauberen, dokumentierten Code
- Testen Sie Ihre Änderungen
- Erstellen Sie einen Pull Request

## 🛠️ **Entwicklungsumgebung einrichten**

### **Voraussetzungen**
- Python 3.8+
- Git
- Docker (optional)

### **Setup**
```bash
# Repository klonen
git clone https://github.com/ak-hosting/prompt-engineering-guide
cd prompt-engineering-guide

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder venv\Scripts\activate  # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt

# Anwendung starten
python app.py
```

## 📝 **Code-Standards**

### **Python**
- Verwenden Sie PEP 8 Style Guide
- Maximale Zeilenlänge: 88 Zeichen
- Verwenden Sie Type Hints wo möglich
- Schreiben Sie Docstrings für Funktionen

### **HTML/CSS**
- Verwenden Sie Bootstrap 5 Klassen
- Halten Sie HTML semantisch
- Verwenden Sie CSS Custom Properties
- Responsive Design beachten

### **JavaScript**
- Verwenden Sie ES6+ Syntax
- Halten Sie Funktionen klein und fokussiert
- Verwenden Sie const/let statt var
- Kommentieren Sie komplexe Logik

## 🔄 **Workflow für Pull Requests**

### **1. Issue erstellen**
- Beschreiben Sie Ihr Vorhaben
- Warten Sie auf Feedback
- Erhalten Sie grünes Licht

### **2. Branch erstellen**
```bash
git checkout -b feature/your-feature-name
```

### **3. Änderungen entwickeln**
- Schreiben Sie sauberen Code
- Testen Sie gründlich
- Committen Sie regelmäßig

### **4. Pull Request erstellen**
- Verwenden Sie das PR Template
- Beschreiben Sie Ihre Änderungen
- Verlinken Sie das Issue
- Fügen Sie Screenshots hinzu (falls relevant)

## 📋 **Pull Request Template**

```markdown
## Beschreibung
Kurze Beschreibung der Änderungen

## Typ der Änderung
- [ ] Bug Fix
- [ ] Neues Feature
- [ ] Dokumentation
- [ ] Refactoring
- [ ] Performance-Verbesserung

## Tests
- [ ] Lokale Tests durchgeführt
- [ ] Keine neuen Bugs eingeführt
- [ ] Responsive Design getestet

## Checkliste
- [ ] Code folgt den Style Guidelines
- [ ] Selbst-Review durchgeführt
- [ ] Kommentare hinzugefügt wo nötig
- [ ] Dokumentation aktualisiert
- [ ] Keine Debug-Code-Reste

## Screenshots (falls relevant)
```

## 🧪 **Testing**

### **Manuelle Tests**
- Testen Sie auf verschiedenen Browsern
- Testen Sie responsive Design
- Testen Sie alle neuen Features
- Testen Sie Performance

### **Automatisierte Tests (geplant)**
```bash
# Unit Tests
python -m pytest tests/

# Integration Tests
python -m pytest tests/integration/

# Coverage Report
python -m pytest --cov=app tests/
```

## 📚 **Dokumentation**

### **Code-Dokumentation**
- Schreiben Sie klare Docstrings
- Kommentieren Sie komplexe Algorithmen
- Verwenden Sie Type Hints
- Aktualisieren Sie README.md

### **Benutzer-Dokumentation**
- Schreiben Sie klare Anweisungen
- Fügen Sie Beispiele hinzu
- Erstellen Sie Screenshots
- Übersetzen Sie wichtige Inhalte

## 🌍 **Übersetzungen**

### **Neue Sprachen hinzufügen**
1. Erstellen Sie einen neuen Ordner in `templates/`
2. Übersetzen Sie alle Templates
3. Erstellen Sie Sprach-Dateien in `static/locales/`
4. Aktualisieren Sie die Sprach-Auswahl

### **Bestehende Übersetzungen verbessern**
- Korrigieren Sie Grammatik und Rechtschreibung
- Verbessern Sie die Übersetzungsqualität
- Fügen Sie fehlende Übersetzungen hinzu

## 🎨 **Design-Beiträge**

### **UI/UX Verbesserungen**
- Folgen Sie dem bestehenden Design-System
- Verwenden Sie Bootstrap 5 Komponenten
- Halten Sie das Design konsistent
- Testen Sie auf verschiedenen Geräten

### **Neue Features**
- Skizzieren Sie das Design vor der Implementierung
- Erstellen Sie Mockups
- Diskutieren Sie mit dem Team
- Sammeln Sie Feedback

## 🔧 **Technische Beiträge**

### **Backend-Verbesserungen**
- Erweitern Sie die Flask-Anwendung
- Verbessern Sie die Performance
- Fügen Sie neue API-Endpoints hinzu
- Implementieren Sie Caching

### **Frontend-Verbesserungen**
- Verbessern Sie die Benutzerfreundlichkeit
- Optimieren Sie die Performance
- Fügen Sie neue Interaktionen hinzu
- Verbessern Sie die Accessibility

## 📊 **Prompt-Datenbank Beiträge**

### **Neue Prompts hinzufügen**
```json
{
  "id": "unique-id",
  "title": "Prompt-Titel",
  "description": "Beschreibung des Prompts",
  "category": "category-name",
  "platform": ["gemini", "gpt4", "claude"],
  "prompt": "Der eigentliche Prompt-Text",
  "example_output": "Beispiel-Ausgabe",
  "tags": ["tag1", "tag2"],
  "author": "Ihr Name",
  "rating": 4.5,
  "usage_count": 0
}
```

### **Kategorien erweitern**
- Fügen Sie neue Kategorien hinzu
- Organisieren Sie bestehende Prompts
- Erstellen Sie Unterkategorien
- Verbessern Sie die Navigation

## 🚫 **Was wir NICHT akzeptieren**

- Code ohne Tests
- Breaking Changes ohne Diskussion
- Änderungen ohne Dokumentation
- Unhöfliches Verhalten
- Spam oder Werbung

## 🏆 **Anerkennung**

### **Contributors werden gelistet in:**
- README.md
- GitHub Contributors
- Release Notes
- Projekt-Website

### **Besondere Anerkennung für:**
- Große Features
- Bug Fixes
- Übersetzungen
- Dokumentation
- Design-Verbesserungen

## 📞 **Hilfe und Support**

### **Bei Fragen:**
- Erstellen Sie ein GitHub Issue
- Schreiben Sie eine E-Mail an ak@ak-pro.com
- Nutzen Sie GitHub Discussions
- Treten Sie unserem Discord bei (geplant)

### **Ressourcen:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

**Vielen Dank für Ihre Beiträge! Gemeinsam machen wir den Prompt Engineering Guide noch besser! 🚀** 