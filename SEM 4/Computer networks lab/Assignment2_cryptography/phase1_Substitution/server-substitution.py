# Decryption using Caesar Cipher Technique
import os

def decrypt(text, s):
    result=""
    # traverse text
    s=26-s
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if (char.isupper()):
            result+= chr((ord(char) + s - 65) % 26 + 65)

            #Decrypt lowercase characters
        else:
            result+= chr((ord(char) + s - 97) % 26 + 97)


    return result

def main():

    shift=11

    #reading the encrypted msg
    f = open('file_b', 'r')
    data = f.read()
    f.close()

    #decrypting the msg
    x=decrypt(data,shift)

    #writing the decrypted msg into file3
    f = open('file_c', 'w+')
    f.write(x)
    f.close()

main()