'''
@author: Rohit Sharma
Date: 01-Aug-2022

Description: This script encrypt all aws certificates stored in a folder. It 
generate one file named filekey.key that you have to store in a secured place.
'''
from cryptography.fernet import Fernet
import os
import glob

# key generation
key = Fernet.generate_key()

	# string the key in a file
with open('/home/awadh/filekey.key', 'wb') as filekey:
	filekey.write(key)

path = '/home/awadh/certs'
all_files = glob.glob(path + "/*")
for filename in all_files:
	
	# opening the key
	with open('/home/awadh/filekey.key', 'rb') as filekey:
		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)

	# opening the original file to encrypt
	with open(filename, 'rb') as file:
		original = file.read()
		
	# encrypting the file
	encrypted = fernet.encrypt(original)

	# opening the file in write mode and
	# writing the encrypted data
	with open(filename, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

