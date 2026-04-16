import socket

def get_remote_ip(domain):
    ip_address = socket.gethostbyname(domain)
    print(f"Domain: {domain}")
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    domain_name = "google.com"
    get_remote_ip(domain_name)