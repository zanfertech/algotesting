#!/usr/bin/env python3.6

import math

PRIMES = [2]

#for x in range(3,10000,2)
x = 3
while x < 1000000:
    no_remainder = False
    #for n in range(2,int(math.sqrt(x) + 1 )):
    i = 0
    s = math.sqrt(x)
    while PRIMES[i] <= s and i < len(PRIMES):
        if (x % PRIMES[i]) == 0:
            no_remainder = True
            break
        i += 1
            #flag.append(n)
    if not no_remainder:
        #debug# print("{} is prime".format(x))
        PRIMES.append(x)
    x+=2

print(PRIMES)
