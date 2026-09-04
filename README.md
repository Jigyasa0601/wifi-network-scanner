# wifi-network-scanner
A network reconnaissance tool built with python & scapy that performs ARP broadcast to map all active hosts on a lan. Useful for network admins to monitor unauthorized devices.
## How It Works 
1. It takes your local network range(for example - `192.168.1.1/24`)
2. It sends an **ARP REQUEST** to every possible IP in that range.
3. All active devices connected to the wi-fi replies with their MAC address.
4. We combine the IP and MAC address and display it in a table to show all the connected devices.
## About Tools, protocol, modules used in building this project 
