from scapy.all import *
from scapy.layers.inet import IP, ICMP

hostname = "google.com"

TTL=1  #time to live(hop limit)
print("\n")

while True:
    
    # Send a ICMP packet and receive response
    pkt = IP(dst=hostname, ttl=TTL) / ICMP()/" hey there "
    # sr1 - send and receive 1 packet at a time
    resp = sr1(pkt, verbose=0)
    #response.display()
    
    if resp is None:
        # No reply
        break
    elif resp.type == 11:
         # time exceeded
        print("%d hop away from Source , IP : " %TTL, resp.src)
        TTL+=1
        continue
    elif resp.type != 3: 
        # type=3 denotes destination is unreachable
        print("Server host IP : " , resp.src)
        print("\n************************************************************")
        print("\nIP address of Source :  ",resp.dst)
        print("\nIP address of Google server : ",resp.src)
        print("\nNumber of intermediate routers or HOP COUNT between source and destination : ",(TTL-1))
        print("\nTraceroute completed,packet echoed back ! ")
        print("\n************************************************************\n")
        break
    else:
        print("\nRe-enter meaningful URL")