from scapy.all import ARP, Ether, srp
import requests

def obter_fabricante(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        resposta = requests.get(url, timeout = 3)
        if resposta.status_code == 200:
            return resposta.text
        
        else:
            return "Desconhecido"
        
    except:
        return "Erro"
    
def escanear_rede(rede):
    print(f"\nEscaneando {rede}. . .")
    pacote_arp = ARP(pdst = rede)
    pacote_broadcast = Ether(dst = "ff:ff:ff:ff:ff:ff")
    pacote = pacote_broadcast / pacote_arp

    resultado = srp(pacote, timeout = 2, iface = "enp2s0", verbose = 0)[0]

    dispositivos = []

    for enviado, recebido in resultado:
        mac = recebido.hwsrc
        fabricante = obter_fabricante(mac)
        dispositivos.append({
            'ip': recebido.psrc,
            'mac': mac,
            'fabricante': fabricante
        })
    
    print("\nDispositivos encontrados: ")

    for d in dispositivos:
        print(f"IP: {d['ip']} \t MAC: {d['mac']} \t Fabricante: {d['fabricante']}")

ip = input("\nDigite o IP: ")
escanear_rede(ip)