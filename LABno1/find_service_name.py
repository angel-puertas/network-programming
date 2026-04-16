import socket

def find_service(port, protocol="tcp"):
    service_name = socket.getservbyport(port, protocol)
    print(f"Port {port}/{protocol} -> Service: {service_name}")

if __name__ == "__main__":
    ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443]

    for port in ports:
        find_service(port, "tcp")