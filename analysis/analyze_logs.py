import json
from collections import Counter

def analyze():
    ips = Counter()
    services = Counter()

    try:
        with open("honeypot_logs.json") as f:
            for line in f:
                event = json.loads(line)
                ips[event["ip"]] += 1
                services[event["service"]] += 1
    except FileNotFoundError:
        print("No logs found.")
        return

    print("\nTop Attacking IPs:")
    for ip, count in ips.most_common(5):
        print(f"{ip}: {count}")

    print("\nServices Targeted:")
    for service, count in services.items():
        print(f"{service}: {count}")

if __name__ == "__main__":
    analyze()
