# extended_port_scanner.py
import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
            return True
        else:
            print(f"Port {port} is closed")
            return False
        sock.close()
    except socket.error as e:
        print(f"Error: {e}")
        return False

def send_message(host, port, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        sock.connect((host, port))
        sock.sendall(message.encode())
        print(f"Message sent to port {port}")
        sock.close()
    except socket.error as e:
        print(f"Error: {e}")

def start_scan_and_send(host, start_port, end_port, message):
    print(f"Scanning ports {start_port} to {end_port} on host {host}...")
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            send_message(host, port, message)

if __name__ == "__main__":
    HOST = input("Enter target host IP: ")  # Change this to the target host's IP address
    N_PORT = int(input("Enter number of ports: "))  # Specify the number of ports to scan
    for i in range(0,N_PORT):
        L_PORT = int(input("Enter ports to scan: "))  # Specify the ports to scan
    MESSAGE = input("Enter message to send: ")  # Specify the message to send
    start_scan_and_send(HOST, N_PORT, L_PORT, MESSAGE)
