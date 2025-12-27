from honeypot.base_honeypot import BaseHoneypot

class SSHHoneypot(BaseHoneypot):
    def __init__(self, port):
        super().__init__("ssh", port)

    def handle_client(self, client, address):
        client.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        super().handle_client(client, address)
