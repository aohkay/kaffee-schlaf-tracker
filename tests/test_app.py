# Tests für die Flask-Anwendung
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Testet die Startseite der Anwendung."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Kaffee-Konsum und Schlafqualität Tracker" in response.data

def test_form(client):
    """Testet die Formularseite."""
    response = client.get('/form')
    assert response.status_code == 200
    assert b"Daten Eingeben" in response.data

def test_add_entry(client):
    """Testet das Hinzufügen eines Eintrags."""
    response = client.post('/add', data={
        'datum': '2025-01-01',
        'menge': 3,
        'uhrzeit': '08:00',
        'schlafdauer': 7,
        'schlafqualitaet': 8
    })
    assert response.status_code == 200
    assert b"Daten erfolgreich hinzugefügt!" in response.data
