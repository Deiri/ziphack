'''imports'''
import zipfile
import colorama
from colorama import Fore
import os

os.system('clear') 
g = input (Fore.GREEN + "Введите путь к словарю для подбора паролей : ")
print("")
b = input ("Введите путь к архиву : ")


count = 1

with open(g,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('unlockit.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print(__banner__,'''*****ПАРОЛЬ ВЗЛОМАН*****\n******************************\n[+] Пароль найден! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print(Fore.RED + '[%s] [-] Подбор... - %s' % (number,password.decode('utf8')),'[-] Пароль неверный')
            count += 1
            pass
