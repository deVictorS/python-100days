#MONITORAMENTO DE PROCESSOS

import psutil
import time
from datetime import datetime
import os

LIMITE_CPU = 80
LIMITE_MEMORIA = 80

LOG_FILE = "logs/day17.txt"
os.makedirs("logs", exist_ok = True)

def registrarLog(mensagem):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {mensagem}\n")

def monitorarProcesso():

    for proc in psutil.process_iter(['pid', 'name']):
        
        try:
            pid = proc.info['pid']
            nome = proc.info['name']
            cpu = proc.cpu_percent(interval = 1)
            mem = proc.memory_percent()
            
            log = f"PID: {pid} - {nome} - CPU: {cpu:.2f}% - Memória: {mem:.2f}%"
            print(log)
            registrarLog(log)

            if cpu > LIMITE_CPU:
                registrarLog(f"ALERTA: CPU ELEVADA NO PROCESSO {nome} (PID {pid}) - {cpu:.2f}%")

            if mem > LIMITE_MEMORIA:
                registrarLog(f"ALERTA: MEMORIA ELEVADA NO PROCESSO {nome} (PID {pid}) - {cpu:.2f}%")

        except(psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":

    while True:
        monitorarProcesso()
        time.sleep(10)