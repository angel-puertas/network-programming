import socket

def get_remote_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print(f"Error: Unable to resolve domain '{domain}'")

if __name__ == "__main__":
    # Change this to any domain you want
    domain_name = "google.com"
    get_remote_ip(domain_name)