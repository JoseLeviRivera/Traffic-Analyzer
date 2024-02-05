import psutil
from ip2geotools.databases.noncommercial import DbIpCity


def network_monitor():
    connections = psutil.net_connections(kind="inet")
    for con in connections:
        if con.status == "ESTABLISHED" and con.raddr.ip != "127.0.0.1":
            print(f"================================================================")
            print(f"Connections found")
            get_process_details(con.pid)
            print(f"Scanning details in remote host ({con.raddr.ip})")
            show_ip_details(con.raddr.ip)


def show_ip_details(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"Ip Address: {res.ip_address}")
    print(f"Location : {res.city}, {res.region}, {res.country}")
    print(f"Coordinates : (Lat: {res.latitude}, Lng: {res.longitude})")


def get_process_details(pid):
    try:
        process = psutil.Process(pid)
        print(f"[+] Process Name: {process.name()} ")
        print(f"[+] Process ID: {pid}")
        print(f"[+] Process Status: {process.status()}")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}")
    except psutil.AccessDenied:
        print(f"Access Denied to process with pid {pid}")


if __name__ == '__main__':
    network_monitor()