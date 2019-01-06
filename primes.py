#!/usr/bin/env python3.6

import math

def main():

    PRIMES = [2]

    x = 3

    while x < 1000:
        ISPRIME = True
        for n in range(3, int(math.sqrt(x) + 1)):
            if x % n == 0:
                ISPRIME = False
                x += 2
                break

        if ISPRIME:
            PRIMES.append(x)
            x += 2

    print(PRIMES)



if __name__ == "__main__":
    main()
