import ipaddress
import sys
import pandas as pd

subnets = pd.read_csv('subnets.csv')
# #print(subnets)
# #print(subnets.AvailableIpAddressCount)
# #print(subnets.CidrBlock)
#
# ##print(ipaddress.ip_network(subnets.CidrBlock))
#
# SubnetSize = ipaddress.ip_network(subnets.CidrBlock)
# #print(SubnetSize.num_addresses)
'''
SubnetSize = ipaddress.ip_network('192.0.2.0/24')
print(SubnetSize.num_addresses)


SubnetSize = ipaddress.ip_network('192.0.2.0/28')
print(SubnetSize.num_addresses)

cidr = '192.0.0.0/16'
SubnetSize = ipaddress.ip_network(cidr)
print("Subnet Size: ", SubnetSize.num_addresses)
'''

#IP = input("IP in format '123.0.0.0'} ")
#defaultcidr = "10.0.0.0/24"

'''
print("Script name ", sys.argv[0])
#print(sys.argv[1])
print("Length of list", len(sys.argv))
print("Length of list", int(len(sys.argv)))

#x = 5
x = int(len(sys.argv))
print("type:", type(x))
print(x)

# passed = int(len(sys.argv))
#
# if passed = 1
#     print("nothing passed")
#
# if sys.argv[1] == null
#     defaultcidr = "10.0.0.0/24"
# else
#     defaultcidr=sys.argv[1]
###print(len(defaultcidr))
'''

#if len(defaultcidr) = 0
#if not defaultcidr:
defaultcidr = "10.0.0.0/24"

print("Input your CIDR or just hit enter for the default (" + defaultcidr + ")")
if not defaultcidr:
    defaultcidr = "10.0.0.0/24"

cidr = input("CIDR in format " + defaultcidr + ": ")
if not cidr:
    cidr = defaultcidr


SubnetSize = ipaddress.ip_network(cidr, strict=False)
AWSSubnetSize = SubnetSize.num_addresses - 5
##AvailIPCount =
##AvailIPPercent

print("Subnet Size: ", SubnetSize.num_addresses)
print("AWS Subnet Size: ", AWSSubnetSize)
