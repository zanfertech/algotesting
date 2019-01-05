#!/usr/bin/env python3.6

import math

PRIMES = []

for x in range(2,10000):
    no_remainder = False
    for n in range(2,int(math.sqrt(x) + 1 )):
        if (x % n) == 0:
            no_remainder = True
            break
            #flag.append(n)
    if not no_remainder:
        #debug# print("{} is prime".format(x))
        PRIMES.append(x)

print(PRIMES)
