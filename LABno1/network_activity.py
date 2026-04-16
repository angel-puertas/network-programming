import socket
import subprocess

def reverse_lookup(ip):
    try:
        hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        print("=== Reverse DNS Lookup ===")
        print(f"IP Address: {ip}")
        print(f"Hostname: {hostname}")
        print(f"Aliases: {aliaslist}")
        print(f"Other IPs: {ipaddrlist}")
    except socket.herror:
        print(f"Could not resolve hostname for IP: {ip}")


def show_open_ports():
    print("\n=== Open Ports and Services ===")

    try:
        # Try using ss (modern Linux)
        result = subprocess.run(["ss", "-tulnp"], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        try:
            # Fallback to netstat
            result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
            print(result.stdout)
        except FileNotFoundError:
            print("Neither 'ss' nor 'netstat' is available on this system.")


if __name__ == "__main__":
    # Task 1: Reverse lookup
    reverse_lookup("8.8.8.8")

    # Task 2: Show open ports
    show_open_ports()