# String functions
s = "harry is a good teacher"
# Note : [a :b ] means string indexes from a to b ,note that a index is included and b is excluded
# If you dont give a it will take default 0 , if you dont give b it will take entire length string as default
# a:b:c -> means that start from a then take index after  c-1 then continue till b
# eg -> 0:19:3 , it means start from 0(a)  then take indexes after  skipping every 2 digits(c-1) upto 19(b) index
# if c is minus then first reverse the string then print from backwards by skipping (-c-1)

print(len(s))
print(s[::-1])

# If string has no numbers in it then it is numberic string and isalnum returns true
# If string has no spaces in it then isalpha returns true

# print(s.isalpha())
# print(s.endswith("teacher"))
# print(s.count("a"))
# print(s.capitalize()) -> it capitalizes only first letter of string

print(s.upper())