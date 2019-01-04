#!/usr/bin/env python3.6

PRIMES = []

for x in range(2,1000):
    flag = []
    #for n in range(2,x):
    for n in range(2,int((x/2)+1)):  ## Algo change cause a number can never be divisible by a number more than half it's value
        #if x == n:
        #    continue
        if (x % n) == 0:  ## Used to be elif, because there was a chance x could == n
            flag.append(n)
    if len(flag) == 0:
        #debug# print("{} is prime".format(x))
        PRIMES.append(x)

print(PRIMES)
