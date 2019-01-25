#!/usr/bin/env python3.6
Z = []

x = 1
y = x
while x < 10000000000000000000000000000:
    Z.append(y)
    y = y + x
    Z.append(x)
    x = y + x
    
print(Z)


    