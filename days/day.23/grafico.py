#GRÁFICOS DE MONITORAMENTO

import matplotlib.pyplot as plt
import csv
from collections import Counter
from collections import defaultdict

timestamps = []
cpus = []
requisicos_por_tempo = Counter()

with open ("log.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        t = row["timestamp"]
        timestamps.append(t)
        cpus.append(float(row["cpu_percent"]))
        requisicos_por_tempo[t] += 1

plt.figure(figsize = (10, 5))
plt.plot(list(requisicos_por_tempo.keys()), list(requisicos_por_tempo.values()), marker = "o")
plt.title("Requisições por segundo")
plt.xlabel("Horário")
plt.ylabel("Nº de requisições")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.grid()
plt.show()

plt.figure(figsize = (14, 6))
plt.plot(timestamps, cpus, color = "red", linewidth = 2, marker = "o", markersize = 4)
plt.title("Uso de CPU (%)")
plt.xlabel("Horário")
plt.ylabel("CPU (%)")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.grid(True, linestyle = "--", alpha = 0.5)
plt.tight_layout()
plt.show()