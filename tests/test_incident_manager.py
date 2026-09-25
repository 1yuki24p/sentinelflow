import sqlite3

from incident_manager import save_incident, get_all_incidents
from models.incident import Incident


def test_save_incident(tmp_path):
    database_path = tmp_path / "test.db"

    connection = sqlite3.connect(database_path)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_type TEXT NOT NULL,
            ip TEXT NOT NULL,
            severity TEXT NOT NULL,
            risk_score INTEGER NOT NULL,
            details TEXT
        )
    """)

    connection.commit()
    connection.close()

    incident = Incident(
        incident_type="Test Incident",
        ip="127.0.0.1",
        severity="LOW",
        details={
            "message": "Testing incident manager"
        }
    )

    incident.risk_score = 25

    save_incident(incident, database_path)

    incidents = get_all_incidents(database_path)

    assert len(incidents) == 1