from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
from datetime import datetime
import time

port = 161
mikrotik_ip = '192.168.88.1'
community = 'public'
oids = {
    
    'uptime': '1.3.6.1.2.1.1.3.0',
    'cpu': '1.3.6.1.4.1.14988.1.1.3.10.0',
    'mem_used': '1.3.6.1.4.1.14988.1.1.4.1.0',
    'mem_total':  '1.3.6.1.4.1.14988.1.1.4.2.0',
}

def get_snmp_value(oid):
    resposta = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((mikrotik_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(resposta)

    if errorIndication:
        print("Erro de comunicação:", errorIndication)
        return None

    elif errorStatus:
        print("Erro SNMP:", errorStatus.prettyPrint())
        return None
    else:
        for varBind in varBinds:
         return int(varBind[1])   

uptime = get_snmp_value(oids['uptime'])

if uptime is not None:
   uptime_horas = int(uptime) /100 /60 /60
   print(f"{datetime.now()} -  Uptime: {uptime_horas:.2f} horas")

