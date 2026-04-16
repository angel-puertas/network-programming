import socket

def find_service(port, protocol="tcp"):
    try:
        service_name = socket.getservbyport(port, protocol)
        print(f"Port {port}/{protocol} -> Service: {service_name}")
    except OSError:
        print(f"Port {port}/{protocol} -> Service: Not found")

if __name__ == "__main__":
    # List of ports to check
    ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443]

    print("=== Service Lookup ===")
    for port in ports:
        find_service(port, "tcp")