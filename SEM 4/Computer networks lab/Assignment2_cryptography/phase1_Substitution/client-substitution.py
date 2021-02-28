# encryption using Caesar Cipher Technique
import os

def encrypt(text, s):
    result=""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result+= chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result+= chr((ord(char) + s - 97) % 26 + 97)


    return result



def main():

    #known to both client and server
    shift=11

    #reading msg to encrypt it
    f = open('file_a', 'r')
    text = f.read()
    f.close()

    #encrypting msg
    encrypt1=encrypt(text,shift)

    #writing encrypte msg into file2
    f = open('file_b', 'w+')
    f.write(encrypt1)
    f.close()


main()