import ipaddress
import sys
import pandas as pd


## Collect the name of te subnets file.
## If none input use the default file name subnets.csv
defsubnetfile = "subnets.csv"
subnetfile = input("Input your subnet file name (Enter for the default " + defsubnetfile + "):")

if not subnetfile:
    subnets = pd.read_csv(defsubnetfile)
else:
    subnets = pd.read_csv(subnetfile)

print(subnets)
