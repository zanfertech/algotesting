#!/usr/bin/env python3.6

import random

def main():

    tx = ['1', '2', '3' ]
    ty = ['4', '5', '6' ]
    tz = ['7', '8', '9' ]

    player = choose_player()

    if player == 1:
        player = 'x'
    elif player == 2:
        player = 'o'

    print(f"{player} starts the game")

    TTT = False
    while not TTT:
        print(tx)
        print(ty)
        print(tz)
        turn = int(input(f"Selection for {player}: "))
        if turn == 1:
            tx[0] = player
        elif turn == 2:
            tx[1] = player
        elif turn == 3:
            tx[2] = player
        elif turn == 4:
            ty[0] = player
        elif turn == 5:
            ty[1] = player
        elif turn == 6:
            ty[2] = player
        elif turn == 7:
            tz[0] = player
        elif turn == 8:
            tz[1] = player
        elif turn == 9:
            tz[2] = player
        elif turn == 0:
            print("Exiting")
            break
        else:
            print("Invalid key - Please try again")
            continue

        TTT = check_ttt(tx, ty, tz, player)
        if TTT:
            print(f"TicTacToe - {player} wins")
            print("Game Over")
            print("Thanks for playing")
            break
        else:
            if player == 'x':
                player = 'o'
            elif player == 'o':
                player = 'x'

def check_ttt(tx, ty, tz, player):

    if tx[0] == tx[1] == tx[2] or ty[0] == ty[1] == ty[2] or tz[0] == tz[1] == tz[2]:
        return player
    elif tx[0] == ty[0] == tz[0] or tx[1] == ty[1] == tz[1] or tx[2] == ty[2] == tz[2]:
        return player
    elif tx[0] == ty[1] == tz[2] or tx[2] == ty[1] == tz[0]:
        return player
    else:
        return 0

def choose_player():
    player = random.randint(1,2)
    return player

if __name__ == "__main__":
    main()
