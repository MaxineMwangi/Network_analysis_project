from honeypot.base_honeypot import BaseHoneypot

class HTTPHoneypot(BaseHoneypot):
    def __init__(self, port):
        super().__init__("http", port)

    def handle_client(self, client, address):
        request = client.recv(2048).decode(errors="ignore")
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            "<h1>Welcome</h1>"
        )
        client.send(response.encode())
        super().handle_client(client, address)
