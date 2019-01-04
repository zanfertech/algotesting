#!/usr/bin/env python3.6

PRIMES = []
flag = []

for x in range(2,200):
    flag = []
    for n in range(2,10):
        if x == n:
            continue
        elif (x % n) == 0:
            flag.append(n)
    if len(flag) == 0:
        print("{} is prime".format(x))
        PRIMES.append(x)

print(PRIMES)
