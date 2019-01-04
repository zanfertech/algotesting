#!/usr/bin/env python3.6

PRIMES = []

for x in range(0,200):
    for n in range(0,10):
        if (x % n) != 0:
            print("{} is prime".format(x))
            PRIMES.append(x)

print(PRIMES)
