from honeypot.base_honeypot import BaseHoneypot

class FTPHoneypot(BaseHoneypot):
    def __init__(self, port):
        super().__init__("ftp", port)

    def handle_client(self, client, address):
        client.send(b"220 FTP Server Ready\r\n")
        super().handle_client(client, address)
