#!/usr/bin/env python

import os #gonna read from file cause its cool

<<<<<<< HEAD

def main():
    t = open("/home/cloud_user/bin/toe.txt", "r")

    for x in t:
        print(len(x))
        for n in range(0,3):
            print(x[n])

if __name__ == '__main__':
=======
def main():
    t = []
    t = open("/home/cloud_user/bin/toe.txt", "r")
    print(f"t is type {type(t)}")
    for x in t:
        print(f"x is legth {len(x)}")
        print(f"x is type {type(x)}")
        for n in range(0,3):
            print(x[n])

if __name__ == "__main__":
>>>>>>> master
    main()
