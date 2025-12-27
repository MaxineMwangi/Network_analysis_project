import socket
import threading
from honeypot.logger import log_event

class BaseHoneypot:
    def __init__(self, service_name, port):
        self.service_name = service_name
        self.port = port

    def handle_client(self, client, address):
        data = client.recv(1024).decode(errors="ignore")
        log_event(self.service_name, address[0], self.port, data)
        client.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", self.port))
        server.listen(5)
        print(f"[+] {self.service_name.upper()} honeypot listening on port {self.port}")

        while True:
            client, address = server.accept()
            thread = threading.Thread(
                target=self.handle_client,
                args=(client, address)
            )
            thread.start()
