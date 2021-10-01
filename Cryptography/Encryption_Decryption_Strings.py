"""
Created on Tue Aug 18 22:37:43 2020
@author: ISH KAPOOR
"""
from cryptography.fernet import Fernet

# Generate the key for encryption and decryption method
def gen_key():

    key = Fernet.generate_key()

    with open("my_key.key", "wb") as my_key:
        my_key.write(key)

# Load my key from dir
def load_key():
    return open("my_key.key", "rb").read()

# Generate and write a new key
gen_key()

# Load the new key
key = load_key()

my_msg = str(input("Enter the message to encrypt:\n"))

enc_msg = my_msg.encode()

# Initalize the Fernet class
f = Fernet(key)

encrypted_msg = f.encrypt(enc_msg)

print("\n\n", encrypted_msg)

# Decrypt tis message
decrypted_msg = f.decrypt(encrypted_msg)

print("Decrypted message:\n\n", decrypted_msg)