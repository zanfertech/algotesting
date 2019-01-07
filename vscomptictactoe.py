#!/usr/bin/env python3.6

import random
import os

def main():

#    status_check(tx, ty, tz)
#    for x in ttt_reset():
#        print(x[0])
#        print(x[1])
#        print(x[2])
    tx = ttt_reset()[0]
    ty = ttt_reset()[1]
    tz = ttt_reset()[2]
    counter = ttt_reset()[3]

    player = choose_player()

    complain = False
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

        if player == 'X':
            turn = input(f"Selection for {player}: ")
        else:
            turn = comp(tx, ty, tz, counter)

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
            if replay():
                ttt_reset()
                tx = ttt_reset()[0]
                ty = ttt_reset()[1]
                tz = ttt_reset()[2]
                counter = ttt_reset()[3]
                TTT = False
                player = choose_player()
                continue
            else:
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
            if replay():
                ttt_reset()
                tx = ttt_reset()[0]
                ty = ttt_reset()[1]
                tz = ttt_reset()[2]
                counter = ttt_reset()[3]
                TTT = False
                player = choose_player()
                continue
            else:
                print("")
                print("Game Over")
                print("Thanks for playing")
                break

def legal_move(turn):
    if turn == 'X' or turn == 'O':
        return False
    else:
        return True

def ttt_reset():

    x = ['7', '8', '9' ]
    y = ['4', '5', '6' ]
    z = ['1', '2', '3' ]
    xcounter = 1

    return (x, y, z, xcounter)

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

def replay():
    ans = input("Would you like to play again? (y/n): ").lower()
    if ans == 'y':
        return True
    elif ans == 'n':
        return False
    else:
        print("invalid response")
        replay()

def check_ttt(tx, ty, tz, player):

    if tx[0] == tx[1] == tx[2] or ty[0] == ty[1] == ty[2] or tz[0] == tz[1] == tz[2]:
        return player
    elif tx[0] == ty[0] == tz[0] or tx[1] == ty[1] == tz[1] or tx[2] == ty[2] == tz[2]:
        return player
    elif tx[0] == ty[1] == tz[2] or tx[2] == ty[1] == tz[0]:
        return player
    #else:
    #    return 0
    """
    Removed need for ending game after one round
    Implemented recursive play
    """

def choose_player():
    player = random.randint(1,2)
    if player == 1:
        player = 'X'
    elif player == 2:
        player = 'O'
    return player

def comp(x, y, z, xcounter):
    if xcounter == 1:
        return random.choice([7, 9, 5, 1, 3])
    elif xcounter == 2:
        return random.randint(1, 9)

    # Build comps personal mapping of board
    survey = { 1 : z[0] , 2 : z[1] , 3 : z[2] ,
            4 : y[0] , 5 : y[1] , 6 : y[2] ,
            7 : x[0] , 8 : x[1] , 9 : x[2] }

    xlist = []
    olist = []

    # Populate lists of x and o items
    # For now its random so it could go in
    # the same array but for future advancement
    # We'll most likely need the lists separated
    for k, v in survey.items():
        if v == 'X':
            xlist.append(k)
    for k, v in survey.items():
        if v == 'O':
            olist.append(k)

    # Combine the lists to a master list
    mlist = xlist + olist

    # A few operations needed to get a list
    # of available numbers.  They create a
    # dict which maps 1-9 to 0.  Then  maps
    # it so keys match values.
    avail = dict.fromkeys(range(1, 10), 0)
    for n in range(1, 10):
        avail[n] = n

    # A final list of numbers is created by
    # removing the numbers we gathered from
    # survey.
    for n in mlist:
        avail.pop(n)

    # A random number from avail numbers
    # will be returned.
    return (random.choice(list(avail)))


if __name__ == "__main__":
    main()
