#!/usr/bin/env python

AR = [5, 1, 3, 2 ,7, 4, 9, 6]

index = 0
flag = 0

print("Opening array: {}".format(AR))

while index < len(AR):
#    print(index) #DEBUG
#    print(flag) #DEBUG
    if AR[index] > AR[index + 1]:
        x = AR[index]
        y = AR[index + 1]

        AR[index] = y
        AR[index + 1] = x
        flag = 1
    index += 1
    if index == (len(AR) - 1) and flag == 1:
        index = 0
        flag = 0

    if index == (len(AR) - 1) and flag == 0:
        break

#    print(AR) #DEBUG

print("Sorted array: {}".format(AR))
