#!/usr/bin/env python

AR = (3, 89, 222, 78, 966,34, 5867, 34566, 7456, 23, 1000, 465, 38, 22, 55)

PEAK = [AR[0]]

count = 0
while count < len(AR):
    if (count + 1) == len(AR):
        break
    if count == 0 or AR[count] > PEAK or AR[(count - 1)] < AR[count] and AR[(count + 1)]:
        PEAK.append(AR[count])
    count += 1

print(PEAK)
