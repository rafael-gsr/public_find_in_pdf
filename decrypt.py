#! /usr/bin/env python

from cryptography.fernet import Fernet
import os

# lê e guarda a key 
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

# vai até /Desktop e vai para a pasta a ser encriptada
usuario = os.getlogin()
desktop_path = os.path.join("/home",usuario,"Desktop")
os.chdir(desktop_path)

if os.path.exists(f"{desktop_path}/FIND_IN_PDF_APP") == True:
    os.chdir(f"{desktop_path}/FIND_IN_PDF_APP")

else:
    os.mkdir(f"{desktop_path}/FIND_IN_PDF_APP")
    print('Created the directory')
    print('Move the files and run again ')
    exit()

# quais arquivos devem ser encriptados
arquivos_para_desencriptar = os.listdir(os.getcwd())
fernet= Fernet(key)

print(' Files to decrypt: ', arquivos_para_desencriptar)

for index in range(0, len(arquivos_para_desencriptar)):
    if arquivos_para_desencriptar[index][-9:] == "encrypted":
        
        print('Dencrypting',arquivos_para_desencriptar[index] ,'...')
        with open(arquivos_para_desencriptar[index], 'rb') as encrypted_file:
            
            decrypted_data= fernet.decrypt(encrypted_file.read())

        with open(f"{arquivos_para_desencriptar[index][:-10]}", 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        os.remove(os.path.join(os.getcwd(), arquivos_para_desencriptar[index]))    
    
    else:
        print(arquivos_para_desencriptar[index] ,' is already decrypted')
        
print('..FINISHED..')