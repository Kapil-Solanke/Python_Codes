"""
Iterable - A python object on which __iter__() or __getitem__() is defined , when we run this methods on that object it
gives us ITERATOR
Iterator - A python object on which __next__() is defined
Iteration -  the process of iterating the object is called iteration

GENERATOR - types of iterator , we can traverse them only one time eg.range()
There are three keywords in python
1) return = it means returning point of funcn after reteurn funcn will not execute antything
2) print - it means to print on the console
3) YIELD - it means to generate value on the fly , we use generators to save the RAM

"""


def gen(n):
    for i in range(n):
        yield i


g = gen(2348979749874024823048)
# we do not want that a number like above we store in our meemory an make our pc slow , so we created GENERATOR  which
#  is capable of generating numbers from 0 to 2348979749874024823048 when i need you I will iterate you , for iterating
# we have iterator __next__()
print(g)

h = gen(3)
print(h)
# print(h.__next__())
# print(h.__next__())
# print(h.__next__())  # StopIteration
# print(h.__next__())  this will show error because we have exceeded StopIteration

for i in h:
    print(i)

name = "harry"
ier = iter(name)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


# print(dir(str))

# for i in dir(str):
#     print(i)

def factcal(n):
    if n == 0 or n == 1:
        return 1
    return n * factcal(n - 1)


def factgen(n):
    yield factcal(n)


g = factgen(7)
for i in g:
    print(i)
