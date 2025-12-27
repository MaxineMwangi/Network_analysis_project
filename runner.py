import threading
from honeypot.ssh_honeypot import SSHHoneypot
from honeypot.http_honeypot import HTTPHoneypot
from honeypot.ftp_honeypot import FTPHoneypot
import config

def start_honeypot(hp):
    hp.start()

if __name__ == "__main__":
    honeypots = [
        SSHHoneypot(config.SERVICES["ssh"]["port"]),
        HTTPHoneypot(config.SERVICES["http"]["port"]),
        FTPHoneypot(config.SERVICES["ftp"]["port"]),
    ]

    for hp in honeypots:
        threading.Thread(target=start_honeypot, args=(hp,), daemon=True).start()

    print("Honeypot services running...")
    input("Press Enter to stop.\n")
