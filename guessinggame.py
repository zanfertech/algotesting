#!/usr/bin/env python3.6

import random
print("Hellooooo, I want to play a little game")
print("")
print("Pick a number from 1 - 1000")


print("")
print("")
print("")
print("")
print("")
print("")

def main():
    lrange = 1
    hrange = 1000
    i = 2
    while i != 0:
        num = random.randint(lrange, hrange + 1)
        print("")
        i = int(input(f"Is you number {num}? Enter 0 if it is; 1 if it is more than {num}; -1 if it s less than {num}: "))

        if i == -1:
            hrange = num
        elif i == 1:
            lrange = num
        else:
            print("Horraaayyyyyyy")

if __name__ == "__main__":
    main()

