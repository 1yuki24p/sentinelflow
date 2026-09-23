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

    test_incident.risk_score = 25

    save_incident(test_incident)

    print("Incident saved successfully.")