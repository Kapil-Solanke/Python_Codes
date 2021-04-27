g = ["a", "b", "c"]
n = [11, 2, 30, 4]
# The functions like sort and reverse change the original list
print(g)
print(n)
# n.sort()
 # after the above line original list is changed
# print(n)
# n.reverse()

# n.append(34) -> append means insert at last
n.insert(2,34)
# n.remove(2)
# n.pop() -> removes last element of list
# n[2]= 36
print(n)

# Immutable  -> cannot change
# Mutable  -> can change

tp = (3,56,78)
# tp[1] = 4 -> we cannot do this because tupple is immutable

# When we create tupple of one element we need to gove extra comma

t =(1,)
print(t)

# we can swap to functions easily in python by given velow syntax

a = 3
b = 4
a , b = b , a
print(a,b)