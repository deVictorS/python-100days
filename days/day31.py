from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
from datetime import datetime
import time


mikrotik_ip = ''
community = 'public'
oid_uptime = '1.3.6.1.2.1.1.3.0'

resposta = getCmd(
    SnmpEngine(),
    CommunityData(community),
    UdpTransportTarget((mikrotik_ip, 161)),
    ContextData(),
    ObjectType(ObjectIdentity(oid_uptime))
)

errorIndication, errorStatus, errorIndex, varBinds = next(resposta)

if errorIndication:
    print("Erro de comunicação:", errorIndication)

elif errorStatus:
    print("Erro SNMP:", errorStatus.prettyPrint())

else:
    for varBind in varBinds:
        uptime = varBind[1]
        uptime_horas = int(uptime) /100 /60 /60
        print(f"[{datetime.now()}] Uptime: {uptime_horas:.2f} horas")
