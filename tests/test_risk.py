from models.incident import Incident
from utils.risk import calculate_risk_score


def test_brute_force_with_five_attempts():
    incident = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.10",
        severity="HIGH",
        details={
            "failed_attempts": 5
        }
    )

    assert calculate_risk_score(incident) == 75


def test_brute_force_with_ten_attempts():
    incident = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.20",
        severity="HIGH",
        details={
            "failed_attempts": 10
        }
    )

    assert calculate_risk_score(incident) == 85


def test_brute_force_with_twenty_attempts():
    incident = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.30",
        severity="HIGH",
        details={
            "failed_attempts": 20
        }
    )

    assert calculate_risk_score(incident) == 95


def test_path_traversal_with_sensitive_file():
    incident = Incident(
        incident_type="Path Traversal",
        ip="10.0.0.20",
        severity="HIGH",
        details={
            "path": "/../../etc/passwd"
        }
    )

    assert calculate_risk_score(incident) == 85


def test_score_never_exceeds_one_hundred():
    incident = Incident(
        incident_type="Brute Force Attack",
        ip="192.168.1.40",
        severity="CRITICAL",
        details={
            "failed_attempts": 20
        }
    )

    assert calculate_risk_score(incident) == 100