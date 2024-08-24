from __future__ import annotations

import socket
import subprocess


class NetworkManager:
    @staticmethod
    def ping(host: str, count: int = 4) -> str:
        """Ping a host and return the output."""
        command = ['ping', '-c', str(count), host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def dns_lookup(domain: str) -> str:
        """Perform a DNS lookup for a given domain."""
        try:
            ip = socket.gethostbyname(domain)
            return f"{domain} has IP address {ip}"
        except socket.gaierror as e:
            return f"DNS lookup failed: {str(e)}"

    @staticmethod
    def port_scan(host: str, port_range: str) -> str:
        """Scan a range of ports on a given host."""
        open_ports = []
        start_port, end_port = map(int, port_range.split('-'))
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        if open_ports:
            return f"Open ports on {host}: {', '.join(map(str, open_ports))}"
        else:
            return f"No open ports found on {host} in the range {port_range}."
