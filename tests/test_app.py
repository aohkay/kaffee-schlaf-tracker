import pytest
from app import app

@pytest.fixture
def client():
    # Erstelle einen Test-Client für die Anwendung
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Teste, ob die Startseite korrekt geladen wird
    response = client.get("/")
    assert response.status_code == 200
    assert b"Kaffee-Konsum und Schlafqualität Tracker" in response.data

def test_form_page(client):
    # Teste, ob die Formularseite korrekt geladen wird
    response = client.get("/form")
    assert response.status_code == 200
    assert b"Daten eingeben" in response.data

def test_add_data(client):
    # Teste, ob Daten erfolgreich hinzugefügt werden können
    response = client.post("/form", data={
        "datum": "2025-01-01",
        "menge": 3,
        "uhrzeit": "10:00",
        "schlafdauer": 7,
        "schlafqualitaet": 8
    })
    assert response.status_code == 200
    assert b"Daten erfolgreich hinzugefügt!" in response.data
