logs = []

with open('attack.log', 'r') as file: # with automatically closes the file after the block is executed
    for line in file:
        parts = line.strip().split()

        if not parts:
            continue # skip empty lines

        log = {
            "date": parts[0],
            "time": parts[1],
            "ip": parts[2],
            "method": parts[3],
            "path": parts[4],
            "status": int(parts[5]) # changing the status to an integer for easier processing
        }

        logs.append(log)

for log in logs:
    if log["status"] >= 400: # checking for error status codes
        print("HTTP Error Detected")
        print(f"IP: {log['ip']}")
        print(f"Request: {log['method']} {log['path']}")
        print(f"Status: {log['status']}")
        print()

failed_logins = {}
for log in logs:
    if log["method"] == "POST" and log["path"] == "/login" and log["status"] == 401: # checking for failed login attempts
        ip = log["ip"]

        if ip not in failed_logins: #If the IP address is not already in the dictionary, initialize its count to 0
            failed_logins[ip] = 0

        failed_logins[ip] += 1 # increment the count of failed login attempts for that IP address


incidents = []
#brute force attack detection: if an IP address has 5 or more failed login attempts, it is considered a brute force attack
for ip, attempts in failed_logins.items():

    if attempts >= 5:

        incident = {
            "type": "Brute Force Attack",
            "ip": ip,
            "failed_attempts": attempts,
            "serverity": "HIGH"
        }

        incidents.append(incident) # adding the incident to the list of incidents

for incident in incidents: # structuring in human-readable format for better understanding of the incident
    print("Security Incident Detected")
    print(f"Type: {incident['type']}")
    print(f"IP: {incident['ip']}")
    print(f"Failed Attempts: {incident['failed_attempts']}")
    print(f"Severity: {incident['serverity']}")
    print()