import socket
#import termcolor


def scan(target, ports):
    print("\n Scanning for " + str(target))
    for port in range(1, ports):
        scan_port(target, port)
    

def scan_port(ip_addrs, port):
    try:
        sock = socket.socket()
        sock.connect((ip_addrs, port))
        #print(termcolor.colored("✅ Port Opened " + port), 'green')
        print("✅  Port Opened " + str(port))
        sock.close()
    except:
        #print(termcolor.colored("❌ Port Closed " + port), 'red')
        print("❌  Port Closed " + str(port))
        #pass


targets = input("Enter the Targets you want to scan (separate ip addresses by ',') : ")
ports = int(input("Enter the number of ports you want to scan : "))


if ',' in targets:
    #print(termcolor.colored("-----Scanning Multiple Targets-----"), 'violet')
    print("-------Scanning Multiple Targets-------")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)