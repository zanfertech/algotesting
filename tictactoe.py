#!/usr/bin/env python

import os

t = open("/home/cloud_user/bin/toe.txt", "r")

for x in t:
    print(len(x))
    for n in range(0,3):
        print(x[n])
