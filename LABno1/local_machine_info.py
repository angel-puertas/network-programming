import socket
import os
import platform
import threading

def get_machine_info():
    # Computer name
    hostname = socket.gethostname()
    
    # Local IP address
    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Unable to get IP"

    print("=== Local Machine Information ===")
    print(f"Computer Name: {hostname}")
    print(f"Local IP Address: {local_ip}")


def start_tcp_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"\n[+] TCP server started on port {port}...")

    while True:
        client_socket, addr = server.accept()
        print(f"[+] Connection from {addr}")
        client_socket.send(b"Hello from server!\n")
        client_socket.close()


if __name__ == "__main__":
    get_machine_info()

    # Run server in a separate thread so script doesn't block
    server_thread = threading.Thread(target=start_tcp_server, daemon=True)
    server_thread.start()

    input("\nPress ENTER to exit...\n")