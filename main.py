from nmap import nmap

from lib.nmap.scanner_range import scanner_by_range, scanner_by_port, run_cve_script

nm = nmap.PortScanner()
#scanner_by_range("127.0.0.1",1443, 1445, nm)
#scanner_by_port("127.0.0.1",5432 , nm)
#scanner_by_port("127.0.0.1",27017 , nm)

scanner_by_range("127.0.0.1",1443, 1445)
open_ports = scanner_by_port("127.0.0.1",1444)
run_cve_script("127.0.0.1",1444)
print(open_ports)







