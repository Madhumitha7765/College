# PING COMMAND USES ICMP PROTOCOL IN TRANSPORT LAYER

from scapy.all import *
import time
from time import ctime

from scapy.layers.inet import IP, ICMP

hostip="192.168.0.178"
global pkt_count
print("\n")


# RTT statistics calculation (avg RTT,loss rate)
def RTT_statistics(avg_RTT,sequence_number):

    sequence_number = list(map(int, sequence_number))
    avg_round_trip_time = sum(avg_RTT)/len(avg_RTT)
    sn = int(max(sequence_number))
    if int(sn) ==int(pkt_count):
        print(f'\nAVERAGE-RTT: {avg_round_trip_time}  SENT-PACKETS: {pkt_count}  RECEIVED-PACKETS: {sn}  * NO LOSS OF PACKETS * ')
    else:
        loss = (pkt_count - sn)/pkt_count
        loss_rate = loss*100
        print(f'\nAVERAGE-RTT: {avg_round_trip_time}  SENT-PACKETS: {pkt_count}  RECEIVED-PACKETS: {sn}  LOSS-RATE: {loss_rate}% ')
       



# function to send 10 ping requests to server

def send_payload():

    pkt_count=10
    while pkt_count:   

        seq_no = 10-pkt_count          
        Time_sent = time.time()   
        Message = 'MY_PING' + ',' + str(seq_no+1) + ',' + str(Time_sent) 
        pkt = IP(dst=hostip)/ ICMP()/Message
        response = sr1(pkt, verbose=0)
        pkt_count -=1
        time.sleep(1)




# function invoked for every packet received

def display(pkt):
    
    Time_received = time.time()
    Payload = pkt[3].load.decode('utf-8').split(',')
    received_msg = Payload[0]
    sequence_no = Payload[1]
    Time_sent = Payload[2]
   
    # calculating RTT
    round_trip_time = Time_received-float(Time_sent)
    t = ctime(Time_received)

    if round_trip_time <= 1:
        print(f'Sequence no: {sequence_no} Time received: {t} Received message: {received_msg} Successfully_Received  RTT: {round_trip_time}' ) 
        avg_RTT.append(round_trip_time)
        sequence_number.append(sequence_no)
    else:
        #Failure case
        print(f'Sequence no:{sequence_no} Timed Out')





if __name__ == "__main__":

    avg_RTT = []
    sequence_number = []
    pkt_function = display
    pkt_filter = "src 192.168.0.178 and icmp"

    receiver = AsyncSniffer(prn=pkt_function, filter=pkt_filter)
    receiver.start()
    time.sleep(2)
    send_payload() 
    pkt_count=10   
    receiver.stop()

    # Average RTT and loss rate calculation
    RTT_statistics(avg_RTT,sequence_number)
    print("\n")
    