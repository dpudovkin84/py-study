commands = ['switchport mode access', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
fast_int = ['0/1','0/3','0/4','0/7','0/9','0/10','0/11']
for intf in fast_int:
    print('int Fa{}'.format(intf))
    for com in commands:
        print('{}'.format(com))

