def noOfParityBits(noOfBits):
    i = 0
    while 2. ** i <= noOfBits + i:  # (power of 2 + parity bits laready  counted) that is for 4 bit of dataword requires 3 bit of parity bits
        i += 1
    return i


# function to genrate no of parity bits in while correction of hamming codes returns no of parity bits in given size of code word
def noOfParityBitsInCode(noOfBits):
    i = 0
    while 2. ** i <= noOfBits:
        i += 1

    return i


# parameter:data
# returns a list with parity bits position is 0 that is position which are power of 2 are 0

def appendParityBits(data):
    n = noOfParityBits(len(data))  # no of parity bits required for given length of data
    i = 0  # loop counter
    j = 0  # no of parity bits
    k = 0  # no of data bits
    list1 = list()
    while i < n + len(data):
        if i == (2. ** j - 1):
            list1.insert(i, 0)
            j += 1
        else:
            list1.insert(i, data[k])
            k += 1
        i += 1
    return list1


# returns a list of hamming codes even parity
# the concept here i used is : i will create one sublist of appropriate bits to be considered for corresponding parity bits that is
# if data is p1 p2 d1 p4 d2 d3 d4 where p is parity bits and d is data bits
# so for p1 sublist will be p1 d1 d2 d4
# for p2 sublist will be p2d1 d3d4
# for p4 sublist will be p4d2d3d4
# so to genralise formula is   list[(j*k)-1:((j+1)*k)-1] where j is intialised to 1 and after each iteration will be incremented by 2
# as we need alternate pairs of data that is for p1 pattern is like take 1 bit skip 1 take 1 skip 1 so taking alternate bits of size  k
# that is k is the weight of parity bits we are considering when for p1 k=2^0=1 for p2 k=2^1=2 for p4 k=2^2=4 so on and i for no of parity bits to be iterated.
# Will increment j upto length of list
def hammingCodes(data):
    n = noOfParityBits(len(data))
    list1 = appendParityBits(data)  # list with parity bits at appropriate position
    i = 0  # loop counter
    k = 1  # 2 to the power kth parity bit
    while i < n:
        k = 2. ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:  # if lower index is last one to be considered in sub list then
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]  # if list's size is smaller than boundary point
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j + 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)  # do the sum of sub list for corresponding parity bits

            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            list1[int(
                k) - 1] = 1  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity

        i += 1
    return list1


def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = "".join(s)
    return (res)

import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

dataword=input('Enter dataword')
msg=hammingCodes(dataword)
print("DATA after adding redundant bits:",msg)
y=convert(msg)
x=str(y)
print(x)
client_socket.sendto(x.encode("utf-8"),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(1024)
print("Server says")
print(str(data))
client_socket.close()