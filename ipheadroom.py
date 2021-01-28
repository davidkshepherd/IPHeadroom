import ipaddress
import sys
import pandas as pd
import os

## Dataload
## Collect the name of te subnets file.
## If none input use the default file name subnets.csv

defsubnetfile = "subnets.csv"
subnetfile = input("Input your subnet file name (Enter for the default " + defsubnetfile + "):")

if not subnetfile:
    subnets = pd.read_csv(defsubnetfile)
else:
#    if os.path.exists(subnetfile):
        subnets = pd.read_csv(subnetfile)
#    else:
#        print("No file found")

def getFreeIPPercent(x,y):
    return "{:.2%}".format(x / y)

## load subnets data in to a DataFrame
df = pd.DataFrame(subnets)

## Print dataframe
print("DataFrame")
print(df)

#print(subnets)

## Evaluate data

i = 0
while i < 3:
##  print(i)
  print("=-" * 20, "=", sep="")
  print("Subnet #: ", i)
  print("SubnetID: ", subnets.SubnetId[i])
  print("CIDR Block: ", subnets.CidrBlock[i])
  cidr = subnets.CidrBlock[i]
  #print(cidr)
  ## SubnetSize is the total count of IPs in the CIDR Block
  SubnetSize = ipaddress.ip_network(cidr, strict=False).num_addresses
  print("CIDR Block Size: ", SubnetSize)

  ## AwsSubnetSize is the total count of IPs in the CIDR Block
  ## LESS 5 addresses reserved for AWS usage
  AWSSubnetSize = SubnetSize - 5
  print("AWS CIDR Block Size: ", AWSSubnetSize)

  ## FreeIPCount is the count of IPs currently avaialble in the CIDR Block
  ## This is straight from AWS
  FreeIPCount = subnets.AvailableIpAddressCount[i]
  print("Free IP Count: ", FreeIPCount)
  UsedIPCount = AWSSubnetSize - subnets.AvailableIpAddressCount[i]
  print("Used IP Count: ", UsedIPCount)
#  FreeIPPercent = FreeIPCount / AWSSubnetSize
#  print("Free IP Percent: ", "{:.2%}".format(FreeIPPercent))
  FreeIPPercent = getFreeIPPercent(FreeIPCount, AWSSubnetSize)
  print("Free IP Percent: ", FreeIPPercent)


  UsedIPPercent = UsedIPCount / AWSSubnetSize
  print("Used IP Percent: ", "{:.2%}".format(UsedIPPercent))

##  if i == 3:
##    break
  i += 1
