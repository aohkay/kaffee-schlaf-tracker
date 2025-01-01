# Kaffee-Konsum und Schlafqualität Tracker
# Eine Flask-Anwendung zur Verfolgung und Analyse von Kaffeekonsum und Schlafqualität

from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

# Flask-Anwendung initialisieren
app = Flask(__name__)
DATABASE = 'database.db'

# Verbindungsfunktion für die SQLite-Datenbank
# Diese Funktion stellt sicher, dass eine Verbindung zur SQLite-Datenbank hergestellt wird
# und speichert die Verbindung im Anwendungs-Kontext (g).
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Verbindung zur Datenbank schließen
# Diese Funktion wird automatisch beim Beenden der Anfrage ausgeführt,
# um sicherzustellen, dass die Datenbankverbindung ordnungsgemäß geschlossen wird.
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Startseite der Anwendung
# Die Funktion "home" rendert die Hauptseite der Anwendung (home.html).
@app.route("/")
def home():
    return render_template("home.html")

# Formularseite für die Dateneingabe
# Diese Route zeigt ein Formular für die Eingabe von Kaffeekonsum- und Schlafdaten.
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Daten aus dem Formular abrufen
        datum = request.form["datum"]
        menge = request.form["menge"]
        uhrzeit = request.form["uhrzeit"]
        schlafdauer = request.form["schlafdauer"]
        schlafqualitaet = request.form["schlafqualitaet"]

        # Daten in die SQLite-Datenbank einfügen
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO konsum (datum, menge, uhrzeit, schlafdauer, schlafqualitaet) VALUES (?, ?, ?, ?, ?)",
            (datum, menge, uhrzeit, schlafdauer, schlafqualitaet)
        )
        db.commit()
        # Weiterleitung zur Ergebnisseite
        return redirect(url_for("results"))

    # Formularseite rendern
    return render_template("form.html")

# Ergebnisseite zur Anzeige der gespeicherten Daten
# Diese Route zeigt die gespeicherten Daten in einer Tabelle an.
@app.route("/results")
def results():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM konsum")
    daten = cursor.fetchall()
    # Rendern der Ergebnisseite mit den abgerufenen Daten
    return render_template("results.html", daten=daten)

# Hauptfunktion der Anwendung
# Diese Bedingung stellt sicher, dass die Anwendung nur ausgeführt wird,
# wenn die Datei direkt gestartet wird.
if __name__ == "__main__":
    app.run(debug=True)
