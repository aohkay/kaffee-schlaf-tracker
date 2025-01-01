# README

## Projekt: Kaffee-Konsum und Schlafqualität Tracker

### Beschreibung
Dieses Projekt wurde im Rahmen des Masterstudiums an der Universität Paderborn von **Alican Ohkay** für die Veranstaltung **"Digitalisierung in der Gesundheitswirtschaft"** entwickelt. Ziel der Anwendung ist es, den Zusammenhang zwischen Kaffeekonsum und Schlafqualität zu analysieren und den Nutzern hilfreiche Einblicke und Empfehlungen zu bieten.

Die Anwendung ermöglicht die Eingabe und Analyse von Daten über den Kaffeekonsum (z. B. Menge, Uhrzeit) und die Schlafqualität (z. B. Schlafdauer, subjektive Bewertung). Sie visualisiert die Daten und bietet eine benutzerfreundliche Oberfläche zur Verfolgung der individuellen Gewohnheiten.

---

## Funktionen der Anwendung
- **Daten Eingeben:**
  Nutzer können Informationen zu ihrem Kaffeekonsum und ihrer Schlafqualität über ein einfaches Formular eingeben.
- **Daten Speichern:**
  Die eingegebenen Daten werden in einer SQLite-Datenbank gespeichert.
- **Daten Analysieren:**
  Die gespeicherten Daten werden in einer tabellarischen Ansicht angezeigt, um Muster und Zusammenhänge zu identifizieren.
- **Ergebnisse Visualisieren:**
  Ergebnisse wie die durchschnittliche Schlafqualität in Abhängigkeit vom Kaffeekonsum werden benutzerfreundlich dargestellt.

---

## Verwendete Technologien
- **Programmiersprache:** Python (Flask-Framework)
- **Datenbank:** SQLite
- **Frontend:** HTML, CSS

---

## Voraussetzungen
- Python 3.x installiert
- Abhängigkeiten: Flask

Installation der Flask-Bibliothek:
```bash
pip install flask
```

---

## Installation und Ausführung
### 1. Projekt-Repository klonen:
```bash
git clone <REPOSITORY_URL>
```

### 2. Datenbank erstellen:
Führen Sie das Skript zur Erstellung der Datenbank aus:
```bash
python database_creation.py
```

### 3. Anwendung starten:
Starten Sie die Flask-Anwendung:
```bash
python app.py
```

Die Anwendung ist jetzt unter `http://127.0.0.1:5000` erreichbar.

---

## Dateistruktur
```
kaffee-schlaf-tracker/
├── app.py             # Hauptanwendung (Flask)
├── database.db        # SQLite-Datenbank
├── templates/         # HTML-Templates
│   ├── home.html      # Startseite
│   ├── form.html      # Eingabeformular
│   ├── results.html   # Ergebnisseite
├── static/            # Statische Dateien (CSS, JS, Bilder)
│   ├── styles.css     # CSS-Stil
├── database_creation.py # Skript zur Erstellung der Datenbank
└── README.md          # Projektbeschreibung
```

---

## Ausblick
Zukünftig könnten folgende Erweiterungen implementiert werden:
1. **Erweiterte Analysen:** Verwendung von Machine-Learning-Modellen zur genaueren Vorhersage der Schlafqualität.
2. **Mobile App:** Entwicklung einer mobilen Anwendung zur bequemeren Nutzung.
3. **Integration von Wearables:** Automatisches Erfassen von Schlaf- und Kaffeekonsumdaten über Fitness-Tracker.

---

## Autor
**Alican Ohkay**
- Masterstudent im Studiengang Management Information Systems
- Universität Paderborn

---Vielen Dank
