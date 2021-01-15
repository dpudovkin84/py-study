#!/usr/bin/env python
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
int_type=input('Input interface type:')
interface=input('Input interface number:')
dict_choice={'access':'Input vlan:','trunk':'Input vlan list:'}
#print(dict_choice[int_type])
vlan=input(dict_choice[int_type])

access='\n'.join(access_template) 
trunk='\n'.join(trunk_template) 
dict_template={'access':access,'trunk':trunk}
print('\n')
print('interface',interface)
print(dict_template[int_type].format(vlan))













