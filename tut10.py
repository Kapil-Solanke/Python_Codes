# Dictionary  is nothing but key value pairs
d = {1, 2, 3}
print(d)

d1 = {"Ram" : "sita", "Radha" : "Krishna" , "Draupadi" :{"a" : "arjun" , "b" : "Bheem"} }
print(d1["Draupadi"]["a"])

# to add any key in dictionary do as given below line
d1 [23] = ["tera"]
d1.update({25 : "mera"})

# print(d1.keys()) -> print keys of dict

print(d1.items())

# to delete key in dictionary do as bleow
del d1[23]
print(d1)

# case 1
# Whwn we do below line we pass original dict , therfore if we ake any change in d2 it gets reflected in d1
# d2 = d1
# del d2[25]
# print(d1)

# case 2
# here we pass copy of d1 in d3 so any change in d2 does not get reflected in d1
# d2 = d1.copy()
# del d2[25]
# print(d2)
# print(d1)
