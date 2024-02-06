import argparse
from lib.file_utils.file_utils import print_banner_green, print_green
from lib.netstat.netstat import network_monitor
from lib.nmap.scanner_range import scanner_by_port, scanner_by_range, run_cve_script
from lib.nmap.scan_with_report import scanner_by_port, scanner_by_range, run_cve_script

# Imprimir el banner
print_banner_green("banner")

# Información sobre los creadores y enlace a GitHub
print("Created by: José Levi Rivera and Erick Saul Melendez")
print("GitHub Repository: https://github.com/JoseLeviRivera/Traffic-Analyzer")
print("\n")
# Información sobre la consola principal
print("=" * 115)

# Puedes agregar más detalles sobre el propósito y funciones del script
print(
    "Welcome to Traffic Analyzer! This is a program that does network analysis with nmap, which IPs are connected to my")
print(
    "local machine, make reports and send notification emails of services not registered in the system's local database")
print("Use it responsibly and follow the documentation on GitHub for instructions.")

# Puedes agregar información sobre cómo iniciar o utilizar el script.
print("\nUsage:")
print("  python3 traffic_analyzer.py [options]")

# Puedes agregar más información sobre las opciones disponibles
print("\nOptions:")
print("  -h, --help         Show this help message and exit.")
print("  -ip                Require ip Adress to scan.")
print("  -p, --port         Single port to scan.")
print("  -r, --range        Port range to scan")
print("  --run-cve          Run CVE script for a specific port.")
print("  --network-monitor  Monitor network connections and display details.")

print("\nThank you for using Traffic Analyzer. Happy analyzing!")


def main():
    parser = argparse.ArgumentParser(description="Traffic Analyzer Script")

    parser.add_argument("-ip", help="Target IP address")

    parser.add_argument("-p", "--port", type=int, help="Single port to scan")
    parser.add_argument("-r", "--range", nargs=2, type=int, metavar=("start", "end"), help="Port range to scan")

    parser.add_argument("--run-cve", action="store_true", help="Run CVE script for a specific port.")
    parser.add_argument("--output-file", help="Specify the output file for analysis results.")

    parser.add_argument("--network-monitor", action="store_true",
                        help="Monitor network connections and display details.")

    args = parser.parse_args()

    if args.network_monitor:
            network_monitor()
    elif args.run_cve:
        if args.output_file:
            run_cve_script(args.ip, args.port, output_file=args.output_file)
        else:
            run_cve_script(args.ip, args.port)
    elif args.port:
        if args.output_file:
            scanner_by_port(args.ip, args.port, output_file=args.output_file)
        else:
            scanner_by_port(args.ip, args.port)
    elif args.range:
        port_min, port_max = args.range
        if args.output_file:
            scanner_by_range(args.ip, port_min, port_max, output_file=args.output_file)
        else:
            scanner_by_range(args.ip, port_min, port_max)
    else:
        print("Error: Please provide valid options. Use -h or --help for more information.")

if __name__ == "__main__":
    main()

# python3 traffic_analyzer.py --network-monitor
# python3 traffic_analyzer.py -ip 127.0.0.1 -p 1444
# python3 traffic_analyzer.py -ip 127.0.0.1 -r 1443 1444
# python3 traffic_analyzer.py -ip 127.0.0.1 -p 1444 --run-cve
# python3 traffic_analyzer.py -ip 127.0.0.1 -p 1444 --output-file report.txt
# python3 traffic_analyzer.py -ip 127.0.0.1 -r 1443 1444 --output-file report2.txt
# python3 traffic_analyzer.py -ip 127.0.0.1 -ip 127.0.0.1 -p 1444 --run-cve --output-file report3.txt
