#!/usr/bin/env python3.6

def main():
    info = { "f_n" : "Zanfer", "l_n" : "Ali", "age" : 35, "birthdate" : "1/5/1984"}

    p = "."
    for x in range(1, 8):
        print(p)
        p += p

    print(f"Hi!  My name is {info['f_n']} {info['l_n']} and it's my birthday!!")
    print(f"I was born on this day, {info['birthdate']}, and I am now {info['age']} years old :) ")

    x = len(p)//2
    while x > 0:
        print(p[:x])
        x = (x//2)

if __name__ == '__main__':
    main()
