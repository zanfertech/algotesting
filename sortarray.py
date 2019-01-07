#!/usr/bin/env python3.6

AR = [5, 1, 14, 9, 6, 19, 17, 2 ,7, 4, 12, 15, 3, 11, 10, 8 ]

index = 0
flag = 0

print("Opening array: {}".format(AR))

while index < len(AR):
#    print(index) #DEBUG
#    print(flag) #DEBUG
    if AR[index] > AR[index + 1]:
        x = AR[index]
        AR[index] = AR[index + 1]
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
