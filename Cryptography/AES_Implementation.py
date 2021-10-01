"""
Created on Wed Sep  9 17:53:20 2020
@author: ISH KAPOOR
"""
'''
AES or Advanced Encryption System is a cryptographic algorithm that is widely 
used now a days. When I wanted to implement it within python, there existed a 
very few resources about it and each one of them was somehow incomplete. So I 
took the liberty to make one for the sake of teaching the whole process.

Key can be of only fixed length of 16/24/32 bytes.

AES uses block-size of fixed length of 16 bytes.
If any data is more than 16 bytes,
then AES breaks it into division of 16 characters.
And work on each block separately.
Data having less than 16 bytes is padded with padding element to fill it out.

1) A random key is not generated like an ideal method, but a real user 
   key/password is taken in
2) Padding is used with complete and separate explanation behind using it
3) The differences between Hashing and Encryption/Decryption are explained
4) Modes, (CBC)Cipher Block Chain and (ECB)Electronic Code Block are explained
5) Initialization vector concepts explained
6) Hashing used for the key that can be implemented in real world
'''

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = input('Enter password:\n')

hash_object = SHA256.new(password.encode('utf-8'))

hKey = hash_object.digest()

def encrypt(info):
    
    msg = info
    BLOCK_SIZE = 16
    PAD = "{"
    padding = lambda s: s + (BLOCK_SIZE - len(s))%BLOCK_SIZE * PAD
    cipher = AES.new(hKey, AES.MODE_ECB)
    pad = padding(msg).encode('utf-8')
    Res = cipher.encrypt(pad)
    return Res

def decrypt(info):

    msg = info
    PAD = "{"
    decipher = AES.new(hKey, AES.MODE_ECB)
#    padding = lambda s: s + (BLOCK_SIZE - len(s))%BLOCK_SIZE * PAD
    Plaintext = decipher.decrypt(msg).decode('utf-8')
    pad_index = Plaintext.find(PAD)
    Res = Plaintext[:pad_index]
    return Res

mode = input("Enter the mode: E(Encode)/D(Decode)\n")

if mode.upper() == 'E':
    print('You have chosen Encryption Mode.')
    Einfo = input('Enter the message for encryption:\n')
    Cipher_Text = encrypt(Einfo)
    print('Encrypted:\n', Cipher_Text)
elif mode.upper() == 'D':
    print('You have chosen Decryption Mode.')
    Dinfo = input('Enter the message for decryption:\n')
    DInfo = bytes(Dinfo, 'utf-8')
    Plain_Text = decrypt(DInfo)
    print('Decrypted:\n', Plain_Text)