import json
import datetime

def log_event(service, ip, port, data):
    event = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "service": service,
        "ip": ip,
        "port": port,
        "data": data,
    }

    with open("honeypot_logs.json", "a") as f:
        f.write(json.dumps(event) + "\n")
