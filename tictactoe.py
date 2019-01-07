#!/usr/bin/env python3.6

import random
import os

def main():

    tx = ['7', '8', '9' ]
    ty = ['4', '5', '6' ]
    tz = ['1', '2', '3' ]
#    status_check(tx, ty, tz)

    player = choose_player()

    complain = False
    counter = 1
    TTT = False
    while not TTT:
        ## print(f"DEBUG - counter = {counter}")
        status_check(tx, ty, tz)

        if counter == 1:
            print("")
            print(f"{player}'s start the game")
            print("")
            print("")

        if complain == True:
            print("Invalid key - Please try again")
            complain = False

        turn = input(f"Selection for {player}: ")
        try:
            turn = int(turn)
        except:
            complain = True
            continue

        if turn == 1 and legal_move(tz[0]):
            tz[0] = player
        elif turn == 2 and legal_move(tz[1]):
            tz[1] = player
        elif turn == 3 and legal_move(tz[2]):
            tz[2] = player
        elif turn == 4 and legal_move(ty[0]):
            ty[0] = player
        elif turn == 5 and legal_move(ty[1]):
            ty[1] = player
        elif turn == 6 and legal_move(ty[2]):
            ty[2] = player
        elif turn == 7 and legal_move(tx[0]):
            tx[0] = player
        elif turn == 8 and legal_move(tx[1]):
            tx[1] = player
        elif turn == 9 and legal_move(tx[2]):
            tx[2] = player
        elif turn == 0:
            print("Exiting")
            break
        else:
            complain = True
            continue

        TTT = check_ttt(tx, ty, tz, player)
        if TTT:
            status_check(tx, ty, tz)
            print("")
            print(f"TicTacToe - {player} wins")
            print("")
            print("Game Over")
            print("Thanks for playing")
            break
        else:
            if player == 'X':
                player = 'O'
                counter += 1
            elif player == 'O':
                player = 'X'
                counter += 1

        if counter > 9:
            status_check(tx, ty, tz)
            print("Tie Game")
            exit()

def legal_move(turn):
    if turn == 'X' or turn == 'O':
        return False
    else:
        return True

def status_check(tx, ty, tz):
        os.system('clear')
        print("###############")
        print("## TicTacToe ##")
        print("###############")
        print("Enter 0 to exit")
        print("")
        print(*tx, sep=" | ")
        print("--+---+--")
        print(*ty, sep=" | ")
        print("--+---+--")
        print(*tz, sep=" | ")
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
    if player == 1:
        player = 'X'
    elif player == 2:
        player = 'O'
    return player

if __name__ == "__main__":
    main()
