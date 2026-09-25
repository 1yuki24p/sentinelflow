import sqlite3

from incident_manager import save_incident, get_all_incidents
from models.incident import Incident

def test_save_incident():
    incident = Incident(
        incident_type="Test Incident",
        ip="127.0.0.1",
        severity="LOW",
        details={
            "message": "Testing incident manager"
        }
    )

    incident.risk_score = 25

    save_incident(incident)

    incidents = get_all_incidents()

    assert len(incidents) >= 1