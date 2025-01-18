import scapy.all as scapy
import argparse

clients_list = []

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target[s] to scan")
    options = parser.parse_args()
    if not options.target:
        parser.error("Please specify a target. Use --help for more details")
    else:
        return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #srp function outputs two values (answer, unanswered), we just need the answered value at position 0
    for element in answer_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return (clients_list)

def print_result(results_list):
    print("IP\t\t\tMAC Addres\n----------") 
    for client in results_list: 
        print(client["ip"] + "\t\t" + client["mac"])
        
options = get_args()
scan_result = scan(options.target)
print_result(scan_result)

    

