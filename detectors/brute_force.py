from models.incident import Incident


def detect_brute_force(logs):
    failed_logins = {}

    for log in logs:
        if (
            log["method"] == "POST"
            and log["path"] == "/login"
            and log["status"] == 401
        ):
            ip = log["ip"]

            if ip not in failed_logins:
                failed_logins[ip] = 0

            failed_logins[ip] += 1

    incidents = []

    for ip, attempts in failed_logins.items():
        if attempts >= 5:
            incident = Incident(
                incident_type="Brute Force Attack",
                ip=ip,
                severity="HIGH",
                details={
                    "failed_attempts": attempts
                }
            )

            incidents.append(incident)

    return incidents