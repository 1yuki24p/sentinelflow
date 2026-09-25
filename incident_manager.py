import sqlite3
import json

from database import DATABASE_NAME


def save_incident(incident, database_name=DATABASE_NAME):
    connection = sqlite3.connect(database_name)
    

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


def get_all_incidents(database_name=DATABASE_NAME):
    connection = sqlite3.connect(database_name)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, incident_type, ip, severity, risk_score, details
        FROM incidents
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows

def get_incidents_by_ip(ip, database_name=DATABASE_NAME):
    connection = sqlite3.connect(database_name)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, incident_type, ip, severity, risk_score, details
        FROM incidents
        WHERE ip = ?
    """, (ip,))

    rows = cursor.fetchall()

    connection.close()

    return rows


