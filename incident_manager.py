import sqlite3
import json

from database import DATABASE_NAME


def save_incident(incident):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO incidents (
            incident_type,
            ip,
            severity,
            risk_score,
            details
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            incident.incident_type,
            incident.ip,
            incident.severity,
            incident.risk_score,
            json.dumps(incident.details)
        )
    )

    connection.commit()
    connection.close()


def get_all_incidents():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, incident_type, ip, severity, risk_score, details
        FROM incidents
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows

def get_incidents_by_ip(ip):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, incident_type, ip, severity, risk_score, details
        FROM incidents
        WHERE ip = ?
    """, (ip,))

    rows = cursor.fetchall()

    connection.close()

    return rows


if __name__ == "__main__":
    from models.incident import Incident

    test_incident = Incident(
        incident_type="Test Incident",
        ip="127.0.0.1",
        severity="LOW",
        details={
            "message": "Testing incident manager"
        }
    )

    test_incident.risk_score = 85

    save_incident(test_incident)

    incidents = get_all_incidents()

    for incident in incidents:
        print(incident)