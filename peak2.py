#!/usr/bin/env python3.6

AR = (3, 89, 222, 5867, 34566, 7456, 1000, 465, 38, 22, 5)

PEAK = 0

count = 0
while count < len(AR):
    if count == 0 or AR[count] > PEAK:
        PEAK = AR[count]
    count += 1

print(PEAK)
