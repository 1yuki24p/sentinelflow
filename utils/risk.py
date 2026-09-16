def calculate_risk_score(incident):
    severity_scores = {
        "LOW": 25,
        "MEDIUM": 50,
        "HIGH": 75,
        "CRITICAL": 100
    }

    base_score = severity_scores.get(incident.severity, 0)

    evidence_bonus = 0

    if incident.incident_type == "Brute Force Attack":
        failed_attempts = incident.details.get("failed_attempts", 0)

        if failed_attempts >= 20:
            evidence_bonus = 20
        elif failed_attempts >= 10:
            evidence_bonus = 10

    elif incident.incident_type == "Path Traversal":
        path = incident.details.get("path", "")

        if "/etc/passwd" in path:
            evidence_bonus = 10

    final_score = base_score + evidence_bonus

    return min(final_score, 100)