#!/usr/bin/env python3.6


with open('/home/cloud_user/invalid_users_w_count_space_rmvd.txt') as hackerfile:
    hackers = hackerfile.readline()
    while hackers:
        hacker = hackers.split()
        print(f" {hacker[0]} \t {hacker[1]} \t|{'#' * int(hacker[0])}")
        hackers = hackerfile.readline()
