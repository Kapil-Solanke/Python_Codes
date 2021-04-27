import time
from functools import lru_cache


@lru_cache(maxsize=3)  # maxsize tells how many value we want to cache or store. Greater maxsize means more memory will
# be used of your pc , eg. here maxsize = 3 means store my last 3 calls
def some_work(n):
    # some task in funcn taking n seconds
    time.sleep(3)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)  # this value will be cached if maxsize = 3
    some_work(5)  # this value will be cached if maxsize = 3
    some_work(9)  # this value will be cached if maxsize = 3
    print("Done...Calling again")
    some_work(3)  # here there will be delay because this value was not cached
    print("Called again")

    some_work(9)  # this will not take time because it was cached before

    print("Called again")

""""
Caching means to store the data in a place from where it can be served faster. In case of data that has been frequently 
used, the computer assigns a cache memory, so it does not have to load it again and again from the main memory
"""
