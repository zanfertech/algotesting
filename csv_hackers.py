#!/usr/bin/env python3.6
import csv


with open('/home/cloud_user/invalid_users_w_count_space_rmvd.txt') as hackerfile:
    hackers = csv.reader(hackerfile, delimiter=' ')
    for hacker in hackers:
        print(f" {hacker[0]} \t {hacker[1]} \t|{'#' * int(hacker[0])}")

'''
### If not using csv - readline for open can be turned into a list
    while hackers:
        hacker = hackers.split()
        print(f" {hacker[0]} \t {hacker[1]} \t|{'#' * int(hacker[0])}")
        hackers = hackerfile.readline()
'''
