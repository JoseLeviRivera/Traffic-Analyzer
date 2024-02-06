from nmap import nmap


def scanner_by_range(ip_address, port_min, port_max, output_file=""):
    nm = nmap.PortScanner()

    open_ports = []

    try:
        with open(output_file, 'w') as file:
            # We're looping over all the ports in the specified range.
            for port in range(port_min, port_max + 1):
                result = nm.scan(ip_address, str(port), arguments='-sV')
                port_info = result['scan'][ip_address]['tcp'][port]

                # Extract port status and service information
                port_status = port_info['state']
                service_name = port_info.get('product', 'Unknown Service')
                service_version = port_info.get('version', 'Unknown Version')

                file.write(f"Port {port} is {port_status}, Service: {service_name}, Version: {service_version}\n")

                # Store open ports in the list
                if port_status == 'open':
                    open_ports.append(port)
    except Exception as e:
        print(f"Error: {str(e)}")

    return open_ports


def scanner_by_port(ip_address, port, output_file=""):
    nm = nmap.PortScanner()

    open_ports = []

    try:
        with open(output_file, 'w') as file:
            # Enable service version detection (-sV)
            result = nm.scan(ip_address, str(port), arguments='-sV')
            port_info = result['scan'][ip_address]['tcp'][port]

            # Extract port status and service information
            port_status = port_info['state']
            service_name = port_info.get('product', 'Unknown Service')
            service_version = port_info.get('version', 'Unknown Version')

            file.write(f"Port {port} is {port_status}, Service: {service_name}, Version: {service_version}\n")

            # Store open ports in the list
            if port_status == 'open':
                open_ports.append(port)
    except Exception as e:
        print(f"Error: {str(e)}")

    return open_ports


def run_cve_script(ip_address, port, output_file=""):
    nm = nmap.PortScanner()

    try:
        with open(output_file, 'w') as file:
            result = nm.scan(ip_address, str(port), arguments='--script vuln')
            file.write(str(result) + '\n')
            # Process the result as needed
    except Exception as e:
        print(f"Error: {str(e)}")
