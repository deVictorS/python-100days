#MONITORAMENTO DE HARDWARE 

import psutil
import time
from datetime import datetime
import os

os.makedirs("logs", exist_ok = True)

LOG_FILE = "logs/day16.txt"

LIMITE_CPU = 90
LIMITE_MEMORIA = 80

def registrar_log(mensagem):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {mensagem}\n")

def monitorar():

    uso_cpu = psutil.cpu_percent(interval = 1)
    uso_memoria = psutil.virtual_memory().percent

    alerta = []

    if uso_cpu > LIMITE_CPU:
        alerta.append(f"ALERTA: CPU EM {uso_cpu}%")
    if uso_memoria > LIMITE_MEMORIA:
        alerta.append(f"ALERTA: MEMORIA EM {uso_memoria}%")

    log_mensagem = f"CPU: {uso_cpu}% | Memoria: {uso_memoria}%"
    if alerta:
        log_mensagem += " | " + " | ".join(alerta)

    print(log_mensagem)
    registrar_log(log_mensagem)

while True:
    monitorar()
    time.sleep(1)