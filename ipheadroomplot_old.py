import ipaddress
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


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
##print(subnets.SubnetId[i].ljust(30, " "), cidr.ljust(20, " "), str(f'{AWSSubnetSize:,}').rjust(10, " "), str(FreeIPCount).rjust(10, " "), UsedIPPercent.rjust(8, " "), sep=" | " )

print("Subnet ID".ljust(30, " "), "CIDR".ljust(20, " "), "CIDR Size".rjust(10, " "), "Used IP #".rjust(10, " "), "Used IP %".rjust(8, " "), sep=" | ")
i = 0
#while i < 3:
for x in subnets.CidrBlock:
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
 ## UsedIPCount = AWSSubnetSize - subnets.AvailableIpAddressCount[i]
  UsedIPCount = getUsedIPCount(AWSSubnetSize, subnets.AvailableIpAddressCount[i])

## -->    print("Used IP Count: ", UsedIPCount)
#  FreeIPPercent = FreeIPCount / AWSSubnetSize
#  print("Free IP Percent: ", "{:.2%}".format(FreeIPPercent))
  FreeIPPercent = getFreeIPPercent(FreeIPCount, AWSSubnetSize)
## -->    print("Free IP Percent: ", FreeIPPercent)


#  UsedIPPercent = UsedIPCount / AWSSubnetSize
  UsedIPPercent = getUsedIPPercent(UsedIPCount, AWSSubnetSize)
## -->  print("Used IP Percent: ", UsedIPPercent)

## -->  print("Subnet ID", "CIDR", "CIDR Size", "IP Free IP #", "Free IP %" )
#######  print(subnets.SubnetId[i].ljust(30, " "), cidr.ljust(20, " "), str(AWSSubnetSize).rjust(10, " "), str(FreeIPCount).rjust(10, " "), FreeIPPercent.ljust(20, " "), sep=" | " )
'''
  print(subnets.SubnetId[i].ljust(30, " "), cidr.ljust(20, " "), str(f'{AWSSubnetSize:,}').rjust(10, " "), str(f'{UsedIPCount:,}').rjust(10, " "), UsedIPPercent.rjust(8, " "), sep=" | " )
'''

N = 1
'''
x = np.random.rand(N)
y = np.random.rand(N)
'''
x = AWSSubnetSize
y = UsedIPCount
colors = np.random.rand(N)
'''
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
'''
plt.scatter(x, y, c=colors, alpha=0.5)
plt.show()


## f'{value:,}'

##  print(str(AWSSubnetSize).ljust(20, " "), sep=" | " )

# Printing the left aligned
# string with "-" padding
#print ("The left aligned string is : ")
#print (cstr.ljust(40, '-'))


##  if i == 3:
##    break
'''
  i += 1
'''
