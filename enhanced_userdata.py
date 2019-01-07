#!/usr/bin/env python3.6

import os

def main():
    counter = 1
    users = [{ 'admin' : True , 'active' : True , 'name' : 'Kevin' },
            { 'admin' : False , 'active' : True , 'name' : 'Devin' },
            { 'admin' : True , 'active' : True , 'name' : 'yevin' },
            { 'admin' : True , 'active' : False , 'name' : 'Revin' },
            { 'admin' : True , 'active' : True , 'name' : 'Sevin' },
            { 'admin' : True , 'active' : False , 'name' : 'Oevin' },
            { 'admin' : True , 'active' : True , 'name' : 'Pevin' },
            { 'admin' : False , 'active' : True , 'name' : 'Nevin' },
            { 'admin' : False , 'active' : False, 'name' : 'Xevin' },
            ]

    for user in users:
#        for admin, active, name in user.items():
        if user['admin'] and user['active']:
            m = (f"ACTIVE - (ADMIN) {user['name']}")
        elif user['active'] and not user['admin']:
            m = (f"ACTIVE - {user['name']}")
        elif user['admin'] and not user['active']:
            m = (f"(ADMIN) {user['name']}")
        else:
            m = (user['name'])

        print(f"{counter}. {m}")
        counter += 1


if __name__ == "__main__":
    main()

