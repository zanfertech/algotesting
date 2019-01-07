#!/usr/bin/env python3.6

import os #gonna read from file cause its cool

def main():

    tx = ['x', 'x', 'x' ]
    ty = ['x', 'E', 'o' ]
    tz = ['x', 'E', 'E' ]


    if tx[0] == tx[1] == tx[2] or ty[0] == ty[1] == ty[2] or tz[0] == tz[1] == tz[2]:


    elif tx[0] == ty[0] == tz[0] or tx[1] == ty[1] == tz[1] or tx[2] == ty[2] == tz[2]:
        print("TicTacToe")
    else:
        print("try again")

if __name__ == "__main__":
    main()
