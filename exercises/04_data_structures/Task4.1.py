#!/usr/bin/env python
#4.1----------------
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat=nat.replace('Fast','Gigabi')
print('nat4.1:',nat)
#4.2-------------------------------
mac = "AAAA:BBBB:CCCC"
mac=mac.replace(':','.')
print('mac4.2:',mac)
#4.3-------------------------------------

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans=config[config.find('vlan')+5::]
vlans=vlans.split(',')
print('vlans4.3:',vlans)
#4.4----------------------------------------
vlans_mesh = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print('vlans_mesh4.4: ',sorted(set(vlans_mesh)))
#4.5------------------------------------------------
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1=set(command1.split()[4].split(','))  
command2=set(command2.split()[4].split(',')) 
print('Intersection4.5:',sorted(command1.intersection(command2)))
#4.6--------------------------------------------------

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()
output = "\n{:25} {}" * 5
print(output.format("Prefix", route[0],"AD/Metric", route[1],"Next-Hop",
 route[3],"Last update", route[4],"Outbound Interface", route[5],))                   

#4.7----------------------------------------------------------------
print('\n')
mac = "AAAA:BBBB:CCCC"
macs=mac.replace(':','') 
int(macs,16)
print('macbin4.7:',bin(int(macs,16))[2:])
#4.8-----------------------------------------
ip = "192.168.3.1"
ips=ip.split('.') 
ip_format='''ip address: 
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:08b} {1:08b} {2:08b} {3:08b} 
'''   
form=ip_format.format(int(ips[0]),int(ips[1]),int(ips[2]),int(ips[3]))
print(form)

























