# a = 7
#
# import tut46
#
# print(tut46.add(3, 4))

import time
from functools import lru_cache

num = int(input("Enter num\n"))


@lru_cache(maxsize=num)
def func1(n):
    time.sleep(3)
    return n


if __name__ == '__main__':
    print("Calling func1 1 time")
    func1(3)
    func1(6)
    func1(9)
    print("Calling func1 2 time")

    func1(6)
    print("Calling func1 3 time")

    func1(9)
    print("Calling func1 4 time")
