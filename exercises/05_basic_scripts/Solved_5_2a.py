#!/usr/bin/env python
ip_address=input('Input ip address:')
ip=ip_address.split('/')[0]
mask=ip_address.split('/')[1]
bin_mask='1'*int((mask))+'0'*(32-int(mask))
ip_format=''' 
Network: 
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:<08b} {1:<08b} {2:<08b} {3:<08b} 
''' 
ip_host_format=''' 
Host: 
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:<08b} {1:<08b} {2:<08b} {3:<08b} 
''' 
mask_format='''
Mask:
{Mask}
{0:<8} {1:<8} {2:<8} {3:<8} 
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''
ip_list=ip.split('.')

m1,m2,m3,m4=[
    int(bin_mask[0:8],2),
    int(bin_mask[8:16],2),
    int(bin_mask[16:24],2),
    int(bin_mask[24:32],2)
    ]  
ip1,ip2,ip3,ip4=[
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3])
    ]
    
ip_f=ip_host_format.format(ip1,ip2,ip3,ip4)
print(ip_f)





bin_ip_str='{0:08b}{1:08b}{2:08b}{3:08b}'.format(ip1,ip2,ip3,ip4)
bin_net_str=bin_ip_str[:int(mask)]+'0'*(32-int(mask))

ip1s,ip2s,ip3s,ip4s=[
    int(bin_net_str[0:8],2),
    int(bin_net_str[8:16],2),
    int(bin_net_str[16:24],2),
    int(bin_net_str[24:32],2)
    ]

ips_f=ip_format.format(ip1s,ip2s,ip3s,ip4s)
#print('\n'*2)
print(ips_f)

print(mask_format.format(m1,m2,m3,m4,Mask=mask))


