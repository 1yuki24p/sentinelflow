from database import create_database

from incident_manager import (
    save_incident,
    get_all_incidents,
    get_incidents_by_ip
)

from models.incident import Incident


def test_save_incident(tmp_path):
    database_path = tmp_path / "test.db"

    create_database(database_path)

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


def test_get_incidents_by_ip(tmp_path):
    database_path = tmp_path / "test.db"

    create_database(database_path)

    incident1 = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.10",
        severity="HIGH",
        details={
            "failed_attempts": 10
        }
    )

    incident1.risk_score = 85

    incident2 = Incident(
        incident_type="Path Traversal",
        ip="192.168.1.20",
        severity="HIGH",
        details={
            "path": "/../../etc/passwd"
        }
    )

    incident2.risk_score = 85

    save_incident(incident1, database_path)
    save_incident(incident2, database_path)

    incidents = get_incidents_by_ip(
        "192.168.1.10",
        database_path
    )

    assert len(incidents) == 1
    assert incidents[0][2] == "192.168.1.10"


def test_get_all_incidents(tmp_path):
    database_path = tmp_path / "test.db"

    create_database(database_path)

    incident1 = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.10",
        severity="HIGH",
        details={
            "failed_attempts": 10
        }
    )

    incident1.risk_score = 85

    incident2 = Incident(
        incident_type="Path Traversal",
        ip="192.168.1.20",
        severity="HIGH",
        details={
            "path": "/../../etc/passwd"
        }
    )

    incident2.risk_score = 85

    save_incident(incident1, database_path)
    save_incident(incident2, database_path)

    incidents = get_all_incidents(database_path)

    assert len(incidents) == 2
    assert incidents[0][1] == "Brute Force Attack"
    assert incidents[1][1] == "Path Traversal"