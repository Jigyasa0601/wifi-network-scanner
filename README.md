# wifi-network-scanner
A network reconnaissance tool built with python & scapy that performs ARP broadcast to map all active hosts on a lan. Useful for network admins to monitor unauthorized devices.
## How It Works 
1. It takes your local network range(for example - `192.168.1.1/24`)
2. It sends an **ARP REQUEST** to every possible IP in that range.
3. All active devices connected to the wi-fi replies with their MAC address.
4. We combine the IP and MAC address and display it in a table to show all the connected devices.
## About Tools, protocol, modules used in building this project 
**1. Python**
Python is the industry-standard programming language for cybersecurity and ethical hacking because it allows security professionals to build custom tools, automate analysis, and react to threats at lightning speed. Security teams use it for both offensive penetration testing and defensive security operations.
Security analysts use Python to map networks, find active hosts, and discover open ports.
    * **Scapy**: A powerful library used to forge, sniff, dissect, and manipulate network packets. It allows hackers to bypass firewalls or test network defenses.
    * **Socket**: A built-in module used to create raw network connections, often used to build custom port scanners.
**2. ARP**
ARP(Address Resolution Protocol) is a fundamental networking protocol used to map a dynamic IP address (logical layer 3 address) to a permanent physical MAC address (media access control layer 2 address) on a local network.Whenever a device wants to talk to another device on the same local network, it knows the target's IP address but needs its physical MAC address to actually deliver the data packets over the hardware.
**3. Ether module (from Scapy)** 
In networking, Ether refers to Ethernet, the standard link-layer technology used to connect devices in a physically wired local area network (LAN). When working with cybersecurity and Python, the term "ether module" usually refers to how Python libraries—specifically Scapy—handle the Ethernet Frame header (Layer 2 of the OSI model).An Ethernet frame wraps around network data (like an IP packet) so it can travel across physical wires, switches, and network interface cards using physical MAC addresses.
**4. srp() Fumction**
`srp` stands for Send and Receive Packets at Layer 2. This function does the main work - it sends our crafted packets and listens for replies from connected devices. 
**5. IP Range / CIDR - `192.168.1.1/24`**
`/24` is CIDR notation. It tells the scanner to check 254 IP addresses (from 192.168.1.1 to 192.168.1.254). You can change it according to your network. 
**6. Npcap**
Npcap is a specialized kernel-level packet capture and injection architecture developed by the Nmap Project for the Microsoft Windows operating system. If you are using tools like Scapy (via Python), Wireshark, or Nmap on a Windows computer, NPCAP is the engine under the hood. It bridges the gap between Windows and raw hardware interfaces.

## Installation & Usage 
**Step 1: Clone the repository**
```bash
git clone https://github.com/Jigyasa0601/wifi-network-scanner.git
cd wifi-network-scanner```
