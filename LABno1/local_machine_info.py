import socket
import os
import platform
import threading

def get_machine_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"Computer Name: {hostname}")
    print(f"Local IP Address: {local_ip}")

if __name__ == "__main__":
    get_machine_info()