import os


# function implementing caesar cipher
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

if __name__ == '__main__':

    text=input("enter text to encrypt:")
    s=int(input("enter shift:"))
    print("encrypted text:",encrypt(text,s))

