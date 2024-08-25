from __future__ import annotations

import ipaddress
import socket
import subprocess
import threading
import time

import requests
import speedtest
import whois
from tqdm import tqdm


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
        """Scan a range of ports on a given host with a progress bar."""
        open_ports = []
        start_port, end_port = map(int, port_range.split('-'))

        print(f"Scanning ports on {host}...")

        for port in tqdm(
            range(start_port, end_port + 1),
            desc='Scanning', unit='port',
        ):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)

        if open_ports:
            return f"Open ports on {host}: {', '.join(map(str, open_ports))}"
        else:
            return f"No open ports found on {host} in the range {port_range}."

    @staticmethod
    def traceroute(host: str, max_hops: int = 30) -> str:
        """Perform a traceroute to a specified host."""
        command = ['traceroute', '-m', str(max_hops), host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def whois_lookup(domain: str) -> str:
        """Perform a WHOIS lookup for a domain."""
        try:
            domain_info = whois.whois(domain)
            return str(domain_info)
        except Exception as e:
            return f"WHOIS lookup failed: {str(e)}"

    @staticmethod
    def geoip_lookup(ip: str) -> str:
        """Get geolocation information for an IP address."""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            geo_info = response.json()
            if geo_info['status'] == 'fail':
                return f"Geolocation lookup failed: {geo_info['message']}"
            return (
                f"IP: {ip}\nCountry: {geo_info['country']}\n"
                f"Region: {geo_info['regionName']}\nCity: {
                    geo_info['city']
                }\nISP: {geo_info['isp']}"
            )
        except Exception as e:
            return f"Geolocation lookup failed: {str(e)}"

    @staticmethod
    def http_request(url: str) -> str:
        """Perform an HTTP GET request and return the status and headers."""
        try:
            response = requests.get(url)
            headers = '\n'.join(
                [f"{key}: {value}" for key, value in response.headers.items()],
            )
            return f"Status: {response.status_code}\nHeaders:\n{headers}"
        except Exception as e:
            return f"HTTP request failed: {str(e)}"

    @staticmethod
    def _run_speed_tests_with_progress(pbar: tqdm, result: dict) -> None:
        """Run download and upload speed tests
                while updating the same progress bar."""
        try:
            st = speedtest.Speedtest()
            # Update the progress bar halfway before the download test
            for _ in range(50):  # Assuming each tick is 0.1 second
                time.sleep(0.1)
                pbar.update(1)

            # Start the download speed test
            pbar.set_description('Testing download speed')
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            result['download'] = download_speed

            # Update the progress bar halfway before the upload test
            for _ in range(50):  # Assuming each tick is 0.1 second
                time.sleep(0.1)
                pbar.update(1)

            # Start the upload speed test
            pbar.set_description('Testing upload speed')
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            result['upload'] = upload_speed

            pbar.set_description('Testing finished')
        except Exception as e:
            result['error'] = str(e)
        finally:
            pbar.n = pbar.total  # Ensure the progress bar completes
            pbar.close()

    @staticmethod
    def speedtest() -> str:
        """Perform a speed test and return the download
            and upload speeds with a combined loading spinner."""
        result: dict = {}
        pbar = tqdm(
            total=100, desc='Speedtest in progress',
            bar_format='{l_bar}{bar} [ time left: {remaining} ]',
        )

        # Run the speed tests and progress bar in the same thread
        test_thread = threading.Thread(
            target=NetworkManager._run_speed_tests_with_progress, args=(
                pbar, result,
            ),
        )
        test_thread.start()
        test_thread.join()

        if 'error' in result:
            return f"Speedtest failed: {result['error']}"

        download_speed = result.get('download', 0)
        upload_speed = result.get('upload', 0)

        return f"Download speed: {download_speed:.2f} Mbps\n\
                Upload speed: {upload_speed:.2f} Mbps"

    @staticmethod
    def ping_sweep(subnet: str) -> str:
        """Perform a ping sweep over a subnet to find active hosts."""
        active_hosts = []
        network = ipaddress.ip_network(subnet, strict=False)

        for ip in tqdm(network.hosts(), desc='Pinging'):
            command = ['ping', '-c', '1', '-W', '1', str(ip)]
            result = subprocess.run(command, stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                active_hosts.append(str(ip))

        if active_hosts:
            return f"Active hosts in {subnet}:\n" + '\n'.join(active_hosts)
        else:
            return f"No active hosts found in {subnet}."

    @staticmethod
    def tcp_check(host: str, port: int) -> str:
        """Check if a TCP connection to a specified port is possible."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                result = sock.connect_ex((host, port))
                if result == 0:
                    return f"Connection to {host}:{port} succeeded!"
                else:
                    return f"Connection to {host}:{port} failed!"
        except Exception as e:
            return f"TCP check failed: {str(e)}"

    @staticmethod
    def arp_cache() -> str:
        """Display the ARP cache."""
        command = ['arp', '-a']
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def ifconfig() -> str:
        """Display network interface information."""
        command = ['ifconfig']
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
