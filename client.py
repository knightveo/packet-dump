import socket


def request(host: str = "example.com", port: int = 80) -> bytes:
    with socket.create_connection((host, port), timeout=3) as sock:
        sock.sendall(b"GET / HTTP/1.0\r\nHost: example.com\r\n\r\n")
        chunks: list[bytes] = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)


if __name__ == "__main__":
    print(request().decode("latin1", errors="replace"))