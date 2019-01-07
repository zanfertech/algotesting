#!/usr/bin/env python3.6


def main():
    x = [2, 6, 7, 3, 1, 8, 9, 5]
    print(min(x[0], x[1:]))

def min(i, x):
    print(f"DEBUG: i is {i} and x is array {x}")
    if len(x) == 1:
        if i <= x[0]:
            return i
        else:
            return x[0]
    else:
        min(x[0], x[1:])

if __name__ == "__main__":
    main()
