import ipaddress
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

'''
## Functions
'''
def getFreeIPPercent(x,y):
    return "{:.2%}".format(x / y)

def getAWSSubnetSize(x):
    return x - 5

def getSubnetSize(x):
    return ipaddress.ip_network(x, strict=False).num_addresses

def getUsedIPCount(x,y):
    return x - y

def getFreeIPCount(x):
    return subnets.AvailableIpAddressCount[x]

def getUsedIPPercent(x,y):
    return x / y
## End Functions
'''
Set up Lists to hold created data
'''
cidrList = []
SubnetSizeList = []
AWSSubnetSizeList = []
FreeIPCountList = []
UsedIPCountList = []
FreeIPPercentList = []
UsedIPPercentList = []

'''
## Dataload and choices
## Collect the name of the subnets file.
## If no input use the default file name "subnets.csv"
## Collect user choices on displays
## Choices default to Yes
'''
defaultsubnetsfile = "subnets.csv"

print("=" * 41, " IP Headroom Tool ", "=" * 41)
print("=" *2)
subnetfile = input("== Input your subnet file name (Enter for the default " + defaultsubnetsfile + "): ")
print("=" *2)
showtable = input("== Do you want to see a Results Table?  Y/n: ")
print("=" *2)
sample = input("== Sample 20 subnets?  Y/n: ")
print("=" *2)
showbar = input("== Do you want to see a Bar Chart?  Y/n: ")
print("=" *2)
showscatter = input("== Do you want to see a Scatter Plot?  Y/n: ")
print("=" * 41, " IP Headroom Tool ", "=" * 41)
print("")
print("=" * 46, " Results ", "=" * 46)



if not subnetfile:
    subnets = pd.read_csv(defaultsubnetsfile)
else:
    subnets = pd.read_csv(subnetfile)

i = 0
#while i < 3:
for x in subnets.CidrBlock:
    cidr = subnets.CidrBlock[i]
    cidrList.append(cidr)
    #print(cidr)
    ## SubnetSize is the total count of IPs in the CIDR Block
    #SubnetSize = ipaddress.ip_network(cidr, strict=False).num_addresses
    SubnetSize = getSubnetSize(cidr)
    SubnetSizeList.append(SubnetSize)
    ## -->    print("CIDR Block Size: ", SubnetSize)

    ## AwsSubnetSize is the total count of IPs in the CIDR Block
    ## LESS 5 addresses reserved for AWS usage
    #AWSSubnetSize = SubnetSize - 5
    AWSSubnetSize = getAWSSubnetSize(SubnetSize)
    AWSSubnetSizeList.append(AWSSubnetSize)
    ## -->    print("AWS CIDR Block Size: ", AWSSubnetSize)

    ## FreeIPCount is the count of IPs currently avaialble in the CIDR Block
    ## This is straight from AWS
    #FreeIPCount = subnets.AvailableIpAddressCount[i]
    FreeIPCount = getFreeIPCount(i)
    FreeIPCountList.append(FreeIPCount)
    ## -->    print("Free IP Count: ", FreeIPCount)

    ## UsedIPCount = AWSSubnetSize - subnets.AvailableIpAddressCount[i]
    UsedIPCount = getUsedIPCount(AWSSubnetSize, subnets.AvailableIpAddressCount[i])
    UsedIPCountList.append(UsedIPCount)
    ## -->    print("Used IP Count: ", UsedIPCount)

    #  FreeIPPercent = FreeIPCount / AWSSubnetSize
    #  print("Free IP Percent: ", "{:.2%}".format(FreeIPPercent))
    FreeIPPercent = getFreeIPPercent(FreeIPCount, AWSSubnetSize)
    FreeIPPercentList.append(FreeIPPercent)
    ## -->    print("Free IP Percent: ", FreeIPPercent)

    #  UsedIPPercent = UsedIPCount / AWSSubnetSize
    UsedIPPercent = getUsedIPPercent(UsedIPCount, AWSSubnetSize)
    UsedIPPercentList.append(UsedIPPercentList)
    ## -->  print("Used IP Percent: ", UsedIPPercent)


## loop through the csv get get valuse, create more values and add to your lists
##    print(UsedIPCountList[i])
#    showtable = input("Do you want to see a Results Table?  Y/N: ")
    if showtable not in ('n', 'N'):
        if i == 0:
            print("###", "Subnet ID".ljust(30, " "), "CIDR".ljust(20, " "), "CIDR Size".rjust(10, " "), "Used IP #".rjust(10, " "), "Used IP %".rjust(8, " "), sep=" | ")
            print(str(i +1 ).ljust(3, " "),subnets.SubnetId[i].ljust(30, " "), cidr.ljust(20, " "), str(f'{AWSSubnetSize:,}').rjust(10, " "), str(f'{UsedIPCount:,}').rjust(10, " "), str("{00:.2%}".format(UsedIPPercent)), sep=" | " )
        else:
            print(str(i + 1).ljust(3, " "),subnets.SubnetId[i].ljust(30, " "), cidr.ljust(20, " "), str(f'{AWSSubnetSize:,}').rjust(10, " "), str(f'{UsedIPCount:,}').rjust(10, " "), str("{00:.2%}".format(UsedIPPercent)), sep=" | " )
    i += 1

    if sample not in ('n', 'N'):
        if i >= 20:
            break



## Set up Bar Chart if requested
if showbar not in ('n', 'N'):
    y = FreeIPCountList
    x = cidrList
#    plt.figure(figsize=(10,8))
    fig= plt.figure(figsize=(9,7))
    plt.barh(x,y)
    plt.xlabel("Free IPs")
    plt.ylabel("CIDR")
    plt.show()
else:
    print("OK.  Maybe next time?")

## Set up Scatter Chart
if showscatter not in ('n', 'N'):
    x = UsedIPCountList
    y = FreeIPCountList
    colors = np.random.rand(i)
    fig= plt.figure(figsize=(9,7))
    plt.scatter(x, y, c=colors, alpha=0.5)
    plt.xlabel("Used IP Count")
    plt.ylabel("Free IP Count")
    plt.show()
else:
    print("OK.  Maybe next time?")
