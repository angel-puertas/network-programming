import socket
import subprocess

def reverse_lookup(ip):
    hostname = socket.gethostbyaddr(ip)
    print(f"Hostname: {hostname}")


def show_open_ports():
    result = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    reverse_lookup("8.8.8.8")
    show_open_ports()