#!/usr/bin/env python
ip_address=input('Input ip address:')
ip=ip_address.split('/')[0]
mask=ip_address.split('/')[1]
ip_format=''' 
Network: 
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:<8b} {1:<8b} {2:<8b} {3:<8b} 
''' 
ip_list=ip.split('.')
ip_f=ip_format.format(int(ip_list[0]),int(ip_list[1]),int(ip_list[2]),int(ip_list[3]))
print(ip_f)
print('Mask'+'\n'+'1'*int((mask))+'0'*(32-int(mask)))

