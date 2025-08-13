from scapy.all import sniff
import pandas as pd

packets_data = []

def packet_callback(packet):
    # Capture only IP packets
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        proto = packet["IP"].proto
        packets_data.append({"Source": src, "Destination": dst, "Protocol": proto})

# Sniff 50 packets for the demo
sniff(prn=packet_callback, count=50)

# Convert to DataFrame
df = pd.DataFrame(packets_data)
df.to_csv("network_log.csv", index=False)

print("Captured packets saved to network_log.csv")
