#!/usr/bin/env python3.6

AR = (3, 89, 222, 78, 966,34, 5867, 34566, 7456, 23, 1000, 465, 38, 22, 55)

PEAK = []

count = 0
while count < len(AR):
    if count == 0 and AR[0] > AR[1] or (count == len(AR) -1 and AR[count] > AR[count-1]) or (AR[count] > AR[count - 1] and AR[count] > AR[count+1]):
        PEAK.append(AR[count])
    count += 1

print(PEAK)
