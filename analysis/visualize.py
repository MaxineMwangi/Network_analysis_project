import json
import matplotlib.pyplot as plt
from collections import Counter

def visualize():
    services = Counter()

    with open("honeypot_logs.json") as f:
        for line in f:
            event = json.loads(line)
            services[event["service"]] += 1

    plt.bar(services.keys(), services.values())
    plt.title("Honeypot Attack Distribution")
    plt.show()

if __name__ == "__main__":
    visualize()
