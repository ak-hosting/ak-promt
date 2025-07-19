# 3. Prompting für verschiedene Aspekte eines Themas: Anwendungsfälle und Beispiele

## Einführung

Dieser Abschnitt demonstriert, wie die grundlegenden Prinzipien und fortgeschrittenen Techniken angewendet werden können, um verschiedene Facetten eines einzelnen Themas zu adressieren. Als Beispielthema dient "Erneuerbare Energien", um zu zeigen, wie dasselbe Kernthema zu sehr unterschiedlichen Arten von Ausgaben führen kann.

## 3.1 Informationsabruf & Zusammenfassung

### Ziel
Präzise, genaue Informationen oder Zusammenfassungen aus bereitgestelltem Text oder allgemeinem Wissen erhalten.

### Techniken
- Klarheit
- Spezifität
- Ausgabeformat
- Kontext
- Prägnanz

### Prompt-Struktur
```
"Fasse zusammen, konzentriere dich auf [Thema] in [Format/Länge] für [Zielgruppe]."
```

### Beispiel Prompt (Erneuerbare Energien)
```
Fasse die primären Vor- und Nachteile von Solar- und Windenergie für den privaten Gebrauch zusammen. 
Präsentiere die Informationen als zwei separate Aufzählungslisten, jede mit maximal fünf prägnanten Punkten. 
Gehen Sie davon aus, dass die Zielgruppe ein Hausbesitzer ist, der eine Installation in Betracht zieht.
```

### Analyse
Dieser Prompt verwendet:
- **Spezifität:** "primäre Vor- und Nachteile", "Solar- und Windenergie", "privaten Gebrauch", "Hausbesitzer"
- **Ausgabeformat:** "zwei separate Aufzählungslisten"
- **Einschränkungen:** "maximal fünf prägnante Punkte"
- **Zielgruppenorientierung:** "Hausbesitzer, der eine Installation in Betracht zieht"

## 3.2 Kreative Inhaltserzeugung

### Ziel
Originalen, ansprechenden oder fantasievollen Inhalt generieren, der einem spezifischen Stil, Ton oder Zweck entspricht.

### Techniken
- Rollenspiel
- Kontext
- Ton
- Negative Einschränkungen
- Temperatur (höher für Kreativität)

### Prompt-Struktur
```
"Agieren Sie als [Persona]. Generieren Sie [Inhaltstyp] über [Thema] für [Zielgruppe] mit [Stil]. 
Stellen Sie sicher [Einschränkungen]."
```

### Beispiel Prompt (Erneuerbare Energien)
```
Agieren Sie als leidenschaftlicher Umweltblogger. 
Schreiben Sie einen kurzen, überzeugenden Social-Media-Post (unter 150 Zeichen), 
der Menschen ermutigt, erneuerbare Energien in Betracht zu ziehen. 
Verwenden Sie einen inspirierenden und leicht informellen Ton. 
Fügen Sie keine Fachbegriffe oder Statistiken ein, 
konzentrieren Sie sich auf emotionale Anziehungskraft.
```

### Analyse
Verwendet:
- **Rollenspiel:** "leidenschaftlicher Umweltblogger"
- **Kontext:** "Social-Media-Post", "Menschen ermutigen"
- **Ton:** "inspirierend und leicht informell"
- **Negative Einschränkungen:** "Keine Fachbegriffe oder Statistiken einfügen"
- **Emotionaler Fokus:** "emotionale Anziehungskraft"

## 3.3 Datenanalyse & Interpretation

### Ziel
Erkenntnisse gewinnen, Trends erklären, numerische Informationen interpretieren oder Schlussfolgerungen aus strukturierten oder unstrukturierten Daten ableiten.

### Techniken
- Chain-of-Thought
- Spezifität
- Ausgabeformat
- Kontext

### Prompt-Struktur
```
"Analysieren Sie [Daten/Thema]. Identifizieren Sie zuerst [Aspekt 1]. 
Zweitens, erklären Sie [Implikationen]. Drittens, geben Sie [Schlussfolgerung] an. 
Präsentieren Sie in [Format]."
```

### Beispiel Prompt (Erneuerbare Energien)
```
Analysieren Sie den bereitgestellten Datensatz zu globalen Investitionstrends in erneuerbare Energien von 2010-2022. 
Identifizieren Sie zuerst die drei am schnellsten wachsenden Sektoren erneuerbarer Energien basierend auf Investitionen. 
Erklären Sie zweitens potenzielle Gründe für ihr Wachstum unter Berücksichtigung wirtschaftlicher und politischer Faktoren. 
Drittens, prognostizieren Sie einen wahrscheinlichen Trend für die nächsten fünf Jahre basierend auf diesen Daten. 
Präsentieren Sie Ihre Analyse in einem strukturierten Absatzformat, 
wobei jeder Teil Ihrer Antwort klar gekennzeichnet ist.
```

### Analyse
Nutzt:
- **Chain-of-Thought:** "Identifizieren Sie zuerst... Zweitens, erklären Sie... Drittens, prognostizieren Sie..."
- **Strukturierte Analyse:** Logischer Gedankenfluss
- **Ausgabestruktur:** "strukturiertes Absatzformat"

## 3.4 Vergleich & Kontrast

### Ziel
Zwei oder mehr Themen systematisch anhand spezifischer Kriterien vergleichen und gegenüberstellen, wobei deren Ähnlichkeiten und Unterschiede hervorgehoben werden.

### Techniken
- Spezifität
- Ausgabeformat
- Kontext

### Prompt-Struktur
```
"Vergleichen und kontrastieren Sie [Entität 1] und [Entität 2] basierend auf [Kriterien]. 
Heben Sie [Ähnlichkeiten] und [Unterschiede] hervor. Präsentieren Sie als [Format]."
```

### Beispiel Prompt (Erneuerbare Energien)
```
Vergleichen und kontrastieren Sie Wasserkraft und Geothermie als Quellen erneuerbarer Elektrizität. 
Konzentrieren Sie sich auf deren Umweltauswirkungen, geografische Einschränkungen, 
Kosteneffizienz und Skalierbarkeit. 
Präsentieren Sie Ihre Ergebnisse in einer Tabelle mit vier Spalten: 
'Kriterium', 'Wasserkraft', 'Geothermie' und 'Hauptunterschied/Ähnlichkeit'.
```

### Analyse
Definiert klar:
- **Vergleichsgegenstände:** "Wasserkraft und Geothermie"
- **Vergleichskriterien:** "Umweltauswirkungen, geografische Einschränkungen, Kosteneffizienz und Skalierbarkeit"
- **Ausgabeformat:** "Tabelle mit vier Spalten"

## 3.5 Problemlösung & Entscheidungsunterstützung

### Ziel
Lösungen brainstormen, Vor- und Nachteile bewerten oder Empfehlungen für ein gegebenes Problem oder Entscheidungsszenario geben.

### Techniken
- Chain-of-Thought
- Kontext
- Rollenspiel
- Negative Einschränkungen

### Prompt-Struktur
```
"Als [Experte/Rolle], analysieren Sie [Problem]. 
Schlagen Sie [Anzahl] Lösungen vor. Listen Sie für jede [Vor-/Nachteile] auf. 
Schließen Sie mit einer [Empfehlung] und deren Begründung ab, 
unter Berücksichtigung von [Faktoren]."
```

### Beispiel Prompt (Erneuerbare Energien)
```
Sie sind ein Stadtplaner, der die Aufgabe hat, die Kohlenstoffemissionen in einem mittelgroßen Stadtgebiet zu reduzieren. 
Schlagen Sie drei verschiedene Initiativen für erneuerbare Energien vor, die umgesetzt werden könnten. 
Beschreiben Sie für jede Initiative kurz deren Umsetzung, 
listen Sie zwei Vorteile und zwei Nachteile auf, die spezifisch für einen städtischen Kontext sind. 
Empfehlen Sie schließlich die praktikabelste Option und erklären Sie Ihre Begründung 
unter Berücksichtigung von Budgetbeschränkungen und öffentlicher Akzeptanz. 
Schlagen Sie keine Kernkraft oder groß angelegte Wasserkraftwerke vor.
```

### Analyse
Kombiniert:
- **Rollenspiel:** "Stadtplaner"
- **Chain-of-Thought:** "vorschlagen... auflisten... empfehlen"
- **Negative Einschränkungen:** "Schlagen Sie keine Kernkraft oder groß angelegte Wasserkraftwerke vor"
- **Kontext:** "städtischer Kontext", "Budgetbeschränkungen und öffentliche Akzeptanz"

## 3.6 Code-Generierung & Debugging

### Ziel
Code-Snippets generieren, bestehenden Code erklären oder Fehler im Code identifizieren und Korrekturen vorschlagen.

### Techniken
- Spezifität
- Kontext
- Ausgabeformat
- Few-Shot
- Chain-of-Thought

### Relevanz für Gemini
Gemini zeichnet sich durch die Generierung von qualitativ hochwertigem Code aus.

### Beispiel Prompt (Erneuerbare Energien - konzeptioneller Code)
```
Schreiben Sie eine Python-Funktion, die die geschätzte jährliche Energieabgabe (in kWh) 
einer Solarmodulanlage berechnet. Die Funktion sollte drei Argumente akzeptieren: 
panel_area_sqm (float), panel_efficiency (float, als Dezimalzahl) und 
average_daily_sunlight_hours (float). 
Fügen Sie Docstrings, Typ-Hinweise und Kommentare zur Erklärung der Berechnung ein. 
Stellen Sie sicher, dass die Ausgabe eine einzelne Gleitkommazahl ist. 
Verwenden Sie keine externen Bibliotheken außer math.
```

### Analyse
Spezifiziert:
- **Programmiersprache:** Python
- **Funktionszweck:** Energieberechnung
- **Eingaben:** Drei spezifische Parameter
- **Ausgabetyp:** "einzelne Gleitkommazahl"
- **Formatierungs-/Stileinschränkungen:** "Docstrings, Typ-Hinweise, Kommentare"

## 3.7 Übersicht: Prompting-Strategien für gängige KI-Aufgaben

| Aufgabentyp | Empfohlene Techniken | Beispiel Prompt-Struktur | Erwartete Ausgabemerkmale |
|-------------|---------------------|-------------------------|---------------------------|
| **Informationsabruf & Zusammenfassung** | Klarheit, Spezifität, Ausgabeformat, Kontext, Prägnanz | "Fasse zusammen, konzentriere dich auf [Thema] in [Format/Länge] für [Zielgruppe]." | Prägnante, faktengestützte Zusammenfassungen; Listen; Antworten auf spezifische Fragen. |
| **Kreative Inhaltserzeugung** | Rollenspiel, Kontext, Ton, Negative Einschränkungen, Hohe Temperatur | "Agieren Sie als [Persona]. Generieren Sie [Inhaltstyp] über [Thema] für [Zielgruppe] mit [Stil]. Stellen Sie sicher [Einschränkungen]." | Originaler, stilistisch angepasster Text; Marketingtexte; Geschichten; Gedichte. |
| **Datenanalyse & Interpretation** | Chain-of-Thought, Spezifität, Ausgabeformat, Kontext | "Analysieren Sie [Daten/Thema]. Identifizieren Sie zuerst [Aspekt 1]. Zweitens, erklären Sie [Implikationen]. Drittens, geben Sie [Schlussfolgerung] an. Präsentieren Sie in [Format]." | Strukturierte Analyse; Erklärungen von Trends; Schlussfolgerungen; Empfehlungen. |
| **Vergleich & Kontrast** | Spezifität, Ausgabeformat, Kontext | "Vergleichen und kontrastieren Sie [Entität 1] und [Entität 2] basierend auf [Kriterien]. Heben Sie [Ähnlichkeiten] und [Unterschiede] hervor. Präsentieren Sie als [Format]." | Tabellen; Listen von Gemeinsamkeiten und Unterschieden; strukturierte Absätze. |
| **Problemlösung & Entscheidungsunterstützung** | Chain-of-Thought, Kontext, Rollenspiel, Negative Einschränkungen | "Als [Experte/Rolle], analysieren Sie [Problem]. Schlagen Sie [Anzahl] Lösungen vor. Für jede, listen Sie [Vor-/Nachteile] auf. Schließen Sie mit einer [Empfehlung] und deren Begründung ab, unter Berücksichtigung von [Faktoren]." | Detaillierte Problemanalyse; mehrere Lösungsansätze mit Bewertung; begründete Empfehlungen. |
| **Code-Generierung & Debugging** | Spezifität, Kontext, Ausgabeformat (Codeblöcke), Few-Shot, Chain-of-Thought | "Schreiben Sie eine [Sprache]-Funktion, die [Zweck] mit [Argumenten] und [Ausgabeformat] erfüllt. Fügen Sie [Formatierung] hinzu. Erklären Sie [Logik/Fehler]." | Funktionierender Code; Code-Erklärungen; Debugging-Vorschläge; Syntaxkorrekturen. |

## 3.8 Praktische Anwendung: Ein Thema, viele Perspektiven

### Beispiel: "Erneuerbare Energien" aus verschiedenen Blickwinkeln

**1. Technische Perspektive:**
```
Erklären Sie die technischen Grundprinzipien der Photovoltaik-Technologie 
für Ingenieure mit Grundkenntnissen in Elektrotechnik. 
Fokussieren Sie sich auf Wirkungsgrad, Materialien und aktuelle Forschungstrends.
```

**2. Wirtschaftliche Perspektive:**
```
Analysieren Sie die Wirtschaftlichkeit von Solarenergie-Investitionen 
aus Sicht eines Kleinunternehmers. Berücksichtigen Sie Anschaffungskosten, 
ROI, staatliche Förderungen und steuerliche Aspekte.
```

**3. Umweltperspektive:**
```
Bewerten Sie die Umweltauswirkungen der verschiedenen erneuerbaren Energietechnologien 
(Solar, Wind, Wasserkraft, Biomasse) über den gesamten Lebenszyklus. 
Vergleichen Sie CO2-Fußabdruck, Landnutzung und Ressourcenverbrauch.
```

**4. Gesellschaftliche Perspektive:**
```
Diskutieren Sie die sozialen Auswirkungen des Übergangs zu erneuerbaren Energien. 
Berücksichtigen Sie Arbeitsplätze, Energiegerechtigkeit, 
lokale Gemeinschaften und politische Herausforderungen.
```

**5. Zukunftsperspektive:**
```
Prognostizieren Sie die Entwicklung der erneuerbaren Energietechnologien 
in den nächsten 20 Jahren. Identifizieren Sie Schlüsseltechnologien, 
Durchbrüche und potenzielle Disruptionen im Energiesektor.
```

## Zusammenfassung

Die "Aspekte eines Themas" werden nicht nur durch den Inhalt, sondern maßgeblich durch die Prompt-Struktur definiert. Die Beispiele zeigen, wie dasselbe Kernthema ("Erneuerbare Energien") zu sehr unterschiedlichen Arten von Ausgaben führen kann. Der untersuchte "Aspekt" ist keine inhärente Eigenschaft des Themas selbst, sondern eine direkte Konsequenz davon, wie der Prompt die Aufgabe formuliert.

Die Beherrschung des Prompt Engineering ermöglicht es einem Benutzer, den Fokus der KI auf ein Thema dynamisch nach Belieben "neu zu definieren" und facettenreiche Erkenntnisse zu gewinnen, ohne mehrere, vortrainierte Modelle für jeden spezifischen Aspekt zu benötigen.

Im nächsten Abschnitt werden wir uns auf die spezifischen Fähigkeiten verschiedener KI-Plattformen konzentrieren und wie diese optimal genutzt werden können. 