import socket
import sys
import time

def port_scanner(target_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except socket.error:
            print(f"Could not connect to port {port}")

target_host = input("Enter the target host: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

port_scanner(target_host, start_port, end_port)    
