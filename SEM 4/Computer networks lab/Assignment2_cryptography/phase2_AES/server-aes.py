# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes
import json

def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


def main():
    #kown to both client and server
    password = 'madhu20'

    #reading the encrypted data
    f = open('file_b', 'r')
    data=f.read()
    f.close()

    #converting str to dictionary
    encrypted=json.loads(data)

    #decrypting
    decrypted=decrypt(encrypted,password)

    #writing the decrypted text to file3
    f = open('file_c', 'w+')
    decrypted=str(decrypted)
    f.write(decrypted)
    f.close()


main()