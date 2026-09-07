def parse_logs(filename):
    logs = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()

            if not parts:
                continue

            log = {
                "date": parts[0],
                "time": parts[1],
                "ip": parts[2],
                "method": parts[3],
                "path": parts[4],
                "status": int(parts[5])
            }

            logs.append(log)
    return logs

