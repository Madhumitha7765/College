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


def hammingCorrection(data):
    n = noOfParityBitsInCode(len(data))
    i = 0
    list1 = list(data)
    errorthBit = 0
    while i < n:
        k = 2. ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]  # if list's size is smaller than boundary point
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j + 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)

            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            errorthBit += k  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
        i += 1
    if errorthBit >= 1:
        print("error in ", errorthBit, " bit after correction data is ")
        # toggle the corrupted bit
        if list1[int(errorthBit - 1)] == '0' or list1[int(errorthBit - 1)] == 0:
            list1[int(errorthBit - 1)] = 1
        else:
            list1[int(errorthBit - 1)] = 0
    else:
        print("No error")
    list2 = list()
    i = 0
    j = 0
    k = 0
    # returning only data from codeword that is ignoring parity bits
    while i < len(list1):  # returning only data bits
        if i != ((2 ** k) - 1):
            temp = list1[int(i)]
            list2.append(temp)
            j += 1
        else:
            k += 1
        i += 1
    return list2
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = "".join(s)
    return (res)

import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
data,addr=sock.recvfrom(1024)
print('Client sent:',str(data))
x=list(data.decode())
print(x)
msg=hammingCorrection(x)
print('Dataword after correction:',msg)
#x=convert(msg)
