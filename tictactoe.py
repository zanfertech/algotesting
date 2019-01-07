#!/usr/bin/env python3.6

import random
import os

def main():

    tx = ['1', '2', '3' ]
    ty = ['4', '5', '6' ]
    tz = ['7', '8', '9' ]
    status_check(tx, ty, tz)

    player = choose_player()

    if player == 1:
        player = 'x'
    elif player == 2:
        player = 'o'

    print("")
    print(f"{player}'s starts the game")
    print("")
    print("")

    complain = False
    counter = 1
    TTT = False
    while not TTT:
        ## print(f"DEBUG - counter = {counter}")
        status_check(tx, ty, tz)

        if complain == True:
            print("Invalid key - Please try again")
            complain = False

        turn = int(input(f"Selection for {player}: "))
        if turn == 1 and legal_move(tx[0]):
            tx[0] = player
        elif turn == 2 and legal_move(tx[1]):
            tx[1] = player
        elif turn == 3 and legal_move(tx[2]):
            tx[2] = player
        elif turn == 4 and legal_move(ty[0]):
            ty[0] = player
        elif turn == 5 and legal_move(ty[1]):
            ty[1] = player
        elif turn == 6 and legal_move(ty[2]):
            ty[2] = player
        elif turn == 7 and legal_move(tz[0]):
            tz[0] = player
        elif turn == 8 and legal_move(tz[1]):
            tz[1] = player
        elif turn == 9 and legal_move(tz[2]):
            tz[2] = player
        elif turn == 0:
            print("Exiting")
            break
        else:
            complain = True
            continue

        TTT = check_ttt(tx, ty, tz, player)
        if TTT:
            status_check(tx, ty, tz)
            print(f"TicTacToe - {player} wins")
            print("Game Over")
            print("Thanks for playing")
            break
        else:
            if player == 'x':
                player = 'o'
                counter += 1
            elif player == 'o':
                player = 'x'
                counter += 1

        if counter > 9:
            status_check(tx, ty, tz)
            print("Tie Game")
            exit()

def legal_move(turn):
    if turn == 'x' or turn == 'o':
        return False
    else:
        return True

def status_check(tx, ty, tz):
        os.system('clear')
        print("==TicTacToe==")
        print("Enter 0 to exit")
        print("")
        print(tx)
        print(ty)
        print(tz)
        print("")
        print("")

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
