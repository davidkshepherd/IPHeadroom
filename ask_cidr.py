import ipaddress
import sys

defaultcidr = "10.0.0.0/24"

print("Input your CIDR or just hit enter for the default (" + defaultcidr + ")")
#if not defaultcidr:
#    defaultcidr = "10.0.0.0/24"
print("=-=-=-=-=  IP Headrom Calculator  =-=-=-=-=")
print("=-=-=-=-=        Data Input       =-=-=-=-=")
cidr = input("Your CIDR (format " + defaultcidr + "): ")
if not cidr:
    cidr = defaultcidr

SubnetSize = ipaddress.ip_network(cidr, strict=False)
IPCount = SubnetSize.num_addresses
AWSSubnetSize = SubnetSize.num_addresses - 5

defaultAvailIPCount = int(AWSSubnetSize/2)

AvailIPCount = input("Number of IPs avaialble (" + str(defaultAvailIPCount) + "): ")
if not AvailIPCount:
    AvailIPCount = defaultAvailIPCount
FreeIPCount = AWSSubnetSize - AvailIPCount
FreeIPPercent = AvailIPCount/AWSSubnetSize

##AvailIPCount =
##AvailIPPercent
print("=-=-=-=-=        Data Input       =-=-=-=-=")
print("  ")
print("=-=-=-=-=         Results         =-=-=-=-=")

print("Subnet CIDR:", cidr)
print("Subnet Size: ", IPCount)
print("AWS Subnet Size: ", AWSSubnetSize)

print("Count of Free IP addresses: ", FreeIPCount)
#print("Percent of Free IP addresses: ", "{:.2%}".format(AvailIPCount/AWSSubnetSize))
print("Percent of Free IP addresses: ", "{:.2%}".format(FreeIPPercent))
#"{:.2%}".format(AvailIPCount/AWSSubnetSize)
