#!/usr/bin/env python3.6

PRIMES = []

for x in range(2,1000):
    flag = []
    #for n in range(2,x):
    for n in range(2,int((x/2)+1)):
        if x == n:
            continue
        elif (x % n) == 0:
            flag.append(n)
    if len(flag) == 0:
        #debug# print("{} is prime".format(x))
        PRIMES.append(x)

print(PRIMES)
