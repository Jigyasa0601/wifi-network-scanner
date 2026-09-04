from scapy.all import ARP, Ether, srp

# we are targetting this ip(you can put yours)
target_ip="192.168.1.1/24"

# arp - it sends requests to ip to get mac address
x=ARP(pdst=target_ip)

# ether - it will broadcast to all devices on the network 
y=Ether(dst="ff:ff:ff:ff:ff:ff")

# combining ARP and Ether to create a packet 
packet=y/x

# srp - it sends the packet and will receive response at layer 2
outcome=srp(packet, timeout=5, verbose=0)[0]
print("\n The Connected Devices are:")
print("IP address\tMAC address")
for sent, received in outcome:
    # prsc for ip address, hwsrc for the mac adresss received
    print(f"{received.psrc}\t{received.hwsrc}")
