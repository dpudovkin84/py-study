#!/usr/bin/env python
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
device=input('Input device name:')
parametr=input('Input device parametr: {}'.format(','.join(london_co.get(device.lower()).keys())))
print('\n'+'-'*30)
print(london_co[device.lower()].get(parametr.lower(),'no such parametr'))










