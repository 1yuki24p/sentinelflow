def parse_logs(filename):
    logs = []

    with open(filename, "r") as file:

        for line_number, line in enumerate(file, start=1):

            parts = line.strip().split()

            # Ignore empty lines
            if not parts:
                continue

            # A valid log entry must contain six fields
            if len(parts) != 6:
                print(
                    f"Skipping malformed log entry on line {line_number}: "
                    f"expected 6 fields, got {len(parts)}"
                )
                continue

            # Convert the status code into an integer
            try:
                status = int(parts[5])
            except ValueError:
                print(
                    f"Skipping malformed log entry on line {line_number}: "
                    "status must be an integer"
                )
                continue

            # Create a structured log dictionary
            log = {
                "date": parts[0],
                "time": parts[1],
                "ip": parts[2],
                "method": parts[3],
                "path": parts[4],
                "status": status
            }

            logs.append(log)

    return logs