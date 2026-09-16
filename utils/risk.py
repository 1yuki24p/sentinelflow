def calculate_risk_score(incident):
    severity_scores = {
        "LOW": 25,
        "MEDIUM": 50,
        "HIGH": 75,
        "CRITICAL": 100
    }

    return severity_scores.get(incident.severity, 0)