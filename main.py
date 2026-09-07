from parser import parse_logs
from detectors.brute_force import detect_brute_force
from utils.output import print_http_error, print_incident


# Parse log file
logs = parse_logs("attack.log")


# Display HTTP errors
for log in logs:

    if log["status"] >= 400:
        print_http_error(log)


# Detect brute-force attacks
incidents = detect_brute_force(logs)


# Display incidents
for incident in incidents:
    print_incident(incident)