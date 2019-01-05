#!/usr/bin/env python3.6

PRIMES = []

for x in range(2,1000):
    no_remainder = False
    for n in range(2,int((x/2)+1)):
        if (x % n) == 0:
            no_remainder = True
            #flag.append(n)
    if not no_remainder:
        #debug# print("{} is prime".format(x))
        PRIMES.append(x)

print(PRIMES)
