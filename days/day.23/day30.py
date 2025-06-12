#MONITORAMENTO DO FLASK

import csv
import psutil
import time
import os
from flask import request

log_file = "log.csv"

if not os.path.exists(log_file):
    with open(log_file, 'w', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "endpoint", "status", "cpu_percent"])

def iniciar_monitoramento(app):
    @app.before_request
    def iniciar_timer():
        request.inicio = time.time()

    @app.after_request
    def registrar_dados(response):
        tempo = time.time() - request.inicio
        process = psutil.Process(os.getpid())
        uso_cpu = process.cpu_percent(interval = 0.05)
        timestamp = time.strftime("%H:%M:%S")
        uso_mem = process.memory_info().rss / 1024 / 1024
        print(f"[{request.remote_addr}] {request.method} {request.path}"
              f"-> {response.status_code} | {tempo:.4f}s | CPU: {uso_cpu:.2f}% | MEM? {uso_mem: .2f}MB")
        
        with open(log_file, 'a', newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, request.path, response.status_code, uso_cpu])

        return response