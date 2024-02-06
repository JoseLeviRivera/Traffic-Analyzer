import psutil
from ip2geotools.databases.noncommercial import DbIpCity


def network_monitor(output_file_path):
    connections = psutil.net_connections(kind="inet")
    with open(output_file_path, "w") as report_file:
        for con in connections:
            if con.status == "ESTABLISHED" and con.raddr.ip != "127.0.0.1":
                print("=" * 70, file=report_file)
                print("Connections found", file=report_file)
                get_process_details(con.pid, report_file)
                print(f"Scanning details in remote host ({con.raddr.ip})", file=report_file)
                show_ip_details(con.raddr.ip, report_file)


def show_ip_details(ip, report_file):
    try:
        res = DbIpCity.get(ip, api_key="free")
        print(f"Ip Address: {res.ip_address}", file=report_file)
        print(f"Location : {res.city}, {res.region}, {res.country}", file=report_file)
        print(f"Coordinates : (Lat: {res.latitude}, Lng: {res.longitude})", file=report_file)
    except Exception as e:
        print(f"Error fetching details for IP {ip}: {str(e)}", file=report_file)


def get_process_details(pid, report_file):
    try:
        process = psutil.Process(pid)
        print(f"[+] Process Name: {process.name()} ", file=report_file)
        print(f"[+] Process ID: {pid}", file=report_file)
        print(f"[+] Process Status: {process.status()}", file=report_file)
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}", file=report_file)
    except psutil.AccessDenied:
        print(f"Access Denied to process with pid {pid}", file=report_file)


if __name__ == '__main__':
    output_file_path = "reportehost.txt"  # Reemplaza con la ruta deseada
    network_monitor(output_file_path)
