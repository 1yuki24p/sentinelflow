def detect_brute_force(logs):

    failed_logins = {}

    # Count failed login attempts by IP
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

    # Check for brute-force attacks
    incidents = []

    for ip, attempts in failed_logins.items():

        if attempts >= 5:

            incident = {
                "type": "Brute Force Attack",
                "ip": ip,
                "failed_attempts": attempts,
                "severity": "HIGH"
            }

            incidents.append(incident)

    return incidents