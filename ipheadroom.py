import ipaddress
import sys
import pandas as pd
import os

## Functions
def getFreeIPPercent(x,y):
    return "{:.2%}".format(x / y)

def getAWSSubnetSize(x):
    return x - 5

def getSubnetSize(x):
    return ipaddress.ip_network(x, strict=False).num_addresses

def getFreeIPCount(x):
    return subnets.AvailableIpAddressCount[x]

## UsedIPPercent = UsedIPCount / AWSSubnetSize
## print("Used IP Percent: ", "{:.2%}".format(UsedIPPercent))

def getUsedIPPercent(x,y):
#    z = x / y
    return  "{:.2%}".format(x / y)

## End Functions


## Dataload
## Collect the name of te subnets file.
## If no input use the default file name "subnets.csv"
defaultsubnetsfile = "subnets.csv"
subnetfile = input("Input your subnet file name (Enter for the default " + defaultsubnetsfile + "):")

if not subnetfile:
    subnets = pd.read_csv(defaultsubnetsfile)
else:
#    if os.path.exists(subnetfile):
        subnets = pd.read_csv(subnetfile)
#    else:
#        print("No file found")


## load subnets data in to a DataFrame
## -->  df = pd.DataFrame(subnets)
## Print dataframe
## -->  print("\nDataFrame\n")
## -->  print(df)

#print(subnets)

## Evaluate data

print("=-" * 20, "=", sep="")
print("Subnet ID", "CIDR", "CIDR Size", "IP Free IP #", "Free IP %", sep=" | ")
i = 0
while i < 3:
##  print(i)
## -->  print("=-" * 20, "=", sep="")
## -->    print("Subnet #: ", i)
## -->    print("Subnet ID: ", subnets.SubnetId[i])
## -->    print("CIDR Block: ", subnets.CidrBlock[i])
  cidr = subnets.CidrBlock[i]
  #print(cidr)
  ## SubnetSize is the total count of IPs in the CIDR Block
  #SubnetSize = ipaddress.ip_network(cidr, strict=False).num_addresses
  SubnetSize = getSubnetSize(cidr)
## -->    print("CIDR Block Size: ", SubnetSize)

  ## AwsSubnetSize is the total count of IPs in the CIDR Block
  ## LESS 5 addresses reserved for AWS usage
  #AWSSubnetSize = SubnetSize - 5
  AWSSubnetSize = getAWSSubnetSize(SubnetSize)
## -->    print("AWS CIDR Block Size: ", AWSSubnetSize)

  ## FreeIPCount is the count of IPs currently avaialble in the CIDR Block
  ## This is straight from AWS
  #FreeIPCount = subnets.AvailableIpAddressCount[i]
  FreeIPCount = getFreeIPCount(i)

## -->    print("Free IP Count: ", FreeIPCount)
  UsedIPCount = AWSSubnetSize - subnets.AvailableIpAddressCount[i]
## -->    print("Used IP Count: ", UsedIPCount)
#  FreeIPPercent = FreeIPCount / AWSSubnetSize
#  print("Free IP Percent: ", "{:.2%}".format(FreeIPPercent))
  FreeIPPercent = getFreeIPPercent(FreeIPCount, AWSSubnetSize)
## -->    print("Free IP Percent: ", FreeIPPercent)


#  UsedIPPercent = UsedIPCount / AWSSubnetSize
  UsedIPPercent = getUsedIPPercent(UsedIPCount, AWSSubnetSize)
## -->  print("Used IP Percent: ", UsedIPPercent)

## -->  print("Subnet ID", "CIDR", "CIDR Size", "IP Free IP #", "Free IP %" )
  print(subnets.SubnetId[i], cidr, AWSSubnetSize, FreeIPCount, FreeIPPercent, sep=" | " )


##  if i == 3:
##    break
  i += 1
