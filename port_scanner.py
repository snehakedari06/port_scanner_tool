import socket
import threading

PORT_SERVICES = {
    20: "FTP (Data) - File Transfer Protocol for data transfer",
    21: "FTP (Control) - Used for FTP commands and control",
    22: "SSH - Secure Shell for remote logins",
    23: "Telnet - Unencrypted remote login (not recommended)",
    25: "SMTP - Sending emails (Simple Mail Transfer Protocol)",
    53: "DNS - Domain Name System for resolving hostnames",
    80: "HTTP - Web traffic on unencrypted websites",
    110: "POP3 - Receiving emails (Post Office Protocol)",
    143: "IMAP - Accessing emails on a remote server",
    443: "HTTPS - Secure web traffic with encryption",
    3306: "MySQL - Database server",
    8080: "HTTP (Alternate) - Often used for testing or proxies"
}

open_ports = []

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = PORT_SERVICES.get(port, "Unknown Service")
            open_ports.append((port, service))
            with open("scan_results.txt", "a") as file:
                file.write(f"[OPEN] Port {port}: {service}\n")
            print(f"[OPEN] Port {port}: {service}")
        sock.close()
    except Exception as e:
        pass

def port_scanner(target, start_port, end_port):
    print(f"Scanning target: {target} (Ports {start_port}-{end_port})")
    print("=" * 50)
    with open("scan_results.txt", "w") as file:
        file.write(f"Scanning target: {target} (Ports {start_port}-{end_port})\n")
        file.write("=" * 50 + "\n")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ")
    try:
        target_ip = socket.gethostbyname(target_ip)
        print(f"Resolved target IP: {target_ip}")
    except:
        print("Invalid target. Please enter a valid IP or hostname.")
        exit()
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    print("\nScanning may take some time depending on the range and target...")
    port_scanner(target_ip, start_port, end_port)
    print("\nScan Summary:")
    for port, service in open_ports:
        print(f"Port {port}: {service}")
