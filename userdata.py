#!/usr/bin/env python3.6

import os

def main():
    user = { 'admin' : True , 'active' : True , 'name' : 'Kevin' }

    if user['admin'] and user['active']:
        print(f"ACTIVE - (ADMIN) {user['name']}")
    elif user['active'] and not user['admin']:
        print(f"ACTIVE - {user['name']}")
    elif user['admin'] and not user['active']:
        print(f"(ADMIN) {user['name']}")
    else:
        print(user['name'])



if __name__ == "__main__":
    main()
