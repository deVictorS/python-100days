#MONITORAMENTO DE HARDWARE 

import psutil
import time
from datetime import datetime
import os

os.makedirs("logs", exist_ok = True)

LOG_FILE = "logs/day16.txt"

LIMITE_CPU = 90
LIMITE_MEMORIA = 80

def registrarLog(mensagem):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {mensagem}\n")

def monitorar():

    usoCpu = psutil.cpu_percent(interval = 1)
    usoMemoria = psutil.virtual_memory().percent

    alerta = []

    if usoCpu > LIMITE_CPU:
        alerta.append(f"ALERTA: CPU EM {usoCpu}%")
    if usoMemoria > LIMITE_MEMORIA:
        alerta.append(f"ALERTA: MEMORIA EM {usoMemoria}%")

    log_mensagem = f"CPU: {usoCpu}% | Memoria: {usoMemoria}%"
    if alerta:
        log_mensagem += " | " + " | ".join(alerta)

    print(log_mensagem)
    registrarLog(log_mensagem)

while True:
    monitorar()
    time.sleep(1)