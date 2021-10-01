"""
Created on Thu Sep 10 01:07:51 2020
@author: ISH KAPOOR
"""
#H.W. : 'Visual Cryptography for Biometric privacy' paper
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

msg= "I'm always high"

bytemsg=msg.encode()
i=0

def getpassword():
	global i
	i+=1
	file=open('WordList.txt','r')
	lines=file.readlines()
	return lines[i]

password=getpassword().encode()  #to convert str to bytes

salt = os.urandom(16)
salt = b'salt_' 
kdf = PBKDF2HMAC(
	algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
key = base64.urlsafe_b64encode(kdf.derive(password)) 

def encryptdata():

	f=Fernet(key)
	encrypted=f.encrypt(bytemsg)
	return encrypted
	
def decryptdata():
	f=Fernet(key)
	decrypt=f.decrypt(encryptdata())
	decrypt=decrypt.decode()
	print("the decrypted message = "+decrypt)	
	
decryptdata()