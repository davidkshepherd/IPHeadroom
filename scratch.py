import ipaddress


SubnetSize = ipaddress.ip_network('192.0.2.0/24')
print(SubnetSize.num_addresses)


SubnetSize = ipaddress.ip_network('192.0.2.0/28')
print(SubnetSize.num_addresses)

cidr = '192.0.0.0/16'
SubnetSize = ipaddress.ip_network(cidr)
print("Subnet Size: ", SubnetSize.num_addresses)


#IP = input("IP in format '123.0.0.0'} ")
cidr = input("CIDR in format '10.0.0.0/24'} ")

SubnetSize = ipaddress.ip_network(cidr)
print("Subnet Size: ", SubnetSize.num_addresses)
