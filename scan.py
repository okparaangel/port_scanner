import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        s.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    host = input("Enter the hostname or IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    print(f"Scanning ports {start_port} to {end_port} on {host}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    main()
