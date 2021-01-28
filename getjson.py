
import json

with open('/Users/shepherd/python/policies/out/subnet/resources.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print("Item 1", data[1])


# json_dict = json.loads(data)
#
# # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(json_dict)
#
# # Output: ['English', 'French']
# print(json_dict['VpcId'])
