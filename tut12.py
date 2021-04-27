# one way of writing set

# l = [2,4,5]
# s = set(l)

# second way of wrirting set
# s = set([1,2,3])

# third way of wrirting set
s = set()
s.add(2)
s.add(1)

# Note : the set has all unique elements in it ,it is same as set in maths
s1 = s.intersection({1, 2, 3}) # It takes intersection of s and {1,2,3} and stores in it s1
print(s, s1)
print(type(s))
