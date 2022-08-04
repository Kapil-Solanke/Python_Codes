# we should not add comments in a json file, we should use double quotes in json files
import json

data = '{"var1":"harry", "var2":56}'
#  here data is just a string
# print(data)
# print(data['var1']) it shows error


# parsed = json.loads(data)
#  json.loads parses the data so i can access it as key value pairs

""""
 for information : The json. load() is used to read the JSON document from file 
 and The 
 json.loads() is used to convert the JSON String document into the Python dictionary
"""

# print(parsed)
# print(parsed['var1'])

data2 = {
    "fridge": ('roti', 345),
    "a": "application",
    "cars": ['bmw', 'audi'],
    "isbad": True
}
jscomp = json.dumps(data2, sort_keys=True)  # It creates a javascript compatible object

print(jscomp)
print(type(jscomp))

# sort_keys parameter data k key: value pairs ko sort krne ke kam ata hai
# Call json.dumps(json_object, sort_keys=True) to convert a json_object to a string with sorted keys.
