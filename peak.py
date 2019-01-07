#!/usr/bin/env python3.6

AR = (3, 89, 222, 5867, 34566, 7456, 1000, 465, 38, 22, 5)

PEAK = []

count = 0
while count < len(AR):
#    print("current count is: {}".format(count))
    current = count
    prev = count - 1
    nex = count + 1

    if prev < 0:
        if AR[current] > AR[nex]:
            PEAK.append(AR[current])
    elif nex > len(AR):
        if AR[current] > AR[prev]:
            PEAK.append(AR[current])
            break
    else:
        if AR[current] >= AR[prev] and AR[current] >= AR[nex]:
            PEAK.append(AR[current])
    count += 1

print(PEAK)
