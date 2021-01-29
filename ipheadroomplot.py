import ipaddress
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

## Functions
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
#    z = x / y
    '''
    return  "{:.2%}".format(x / y)
    '''
    return  x / y

## End Functions


cidrList = []
SubnetSizeList = []
AWSSubnetSizeList = []
FreeIPCountList = []
UsedIPCountList = []
FreeIPPercentList = []
UsedIPPercentList = []

'''
cidrList.append("10.0.0.0/23")
AWSSubnetSizeList.append(507)
'''


'''
print(cidrList)
print(AWSSubnetSizeList)
print(cidrList[0])
print(AWSSubnetSizeList[0])
'''

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
    print(UsedIPCountList[i])

    i += 1
    if i >= 10:
        break
'''
print(UsedIPCountList[i])
'''

'''
N = 1
x = np.random.rand(N)
y = np.random.rand(N)
'''
'''
x = AWSSubnetSizeList
y = SubnetSizeList
'''
x = UsedIPCountList
y = FreeIPCountList

colors = np.random.rand(i)
plt.scatter(x, y, c=colors, alpha=0.5)
plt.xlabel("AWS Subnet Size")
plt.ylabel("Subnet Size")
plt.show()


x = FreeIPCountList
y = cidrList
plt.bar(x,y)
plt.xlabel("Free IPs")
plt.ylabel("CIDR")

plt.show()



'''
# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height[0])


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
'''
