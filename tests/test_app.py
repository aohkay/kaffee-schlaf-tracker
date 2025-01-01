# Tests für die Flask-Anwendung
import pytest
from app import app

@pytest.fixture
def client():
    """Fixture zur Einrichtung des Testclients für die Flask-App."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Testet, ob die Startseite geladen wird."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Willkommen bei Kaffee-Konsum und Schlafqualität Tracker" in response.data

def test_form(client):
    """Testet, ob die Formularseite geladen wird."""
    response = client.get('/form')
    assert response.status_code == 200
    assert b"Datum" in response.data
    assert b"Menge" in response.data

def test_add_entry(client):
    """Testet, ob ein Eintrag erfolgreich hinzugefügt wird."""
    response = client.post('/add', data={
        'datum': '2025-01-01',
        'menge': 2,
        'uhrzeit': '10:00',
        'schlafdauer': 7,
        'schlafqualitaet': 8
    })
    assert response.status_code == 200
    assert b"Daten erfolgreich hinzugefügt!" in response.data
