#!/usr/bin/env python3.6

import time
import random
import os

def main():

    os.system('clear')
    banner()
    mode = 3
    while mode < 1 or mode > 2:
        mode = input("Single Player - Press 1\nMulti Player - Press 2\n\n:")
        try:
            mode = int(mode)
        except:
            print("Invalid key - Please try again")
            continue
        if mode == 1:
            mode = 'single'
            break
        elif mode == 2:
            mode = 'multi'
            break
        elif mode == 0:
            exit()
        else:
            print("Invalid key - Please try again")

    tx = ttt_reset()[0]
    ty = ttt_reset()[1]
    tz = ttt_reset()[2]
    counter = ttt_reset()[3]

    player = choose_player()


    complain = False
    TTT = False
    while not TTT:
        print(f"DEBUG - counter = {counter}")
        status_check(tx, ty, tz)

        if counter == 1:
            print("")
            print(f"{player}'s start the game")
            print("")
            print("")

        if complain == True:
            print("Invalid key - Please try again")
            complain = False

        if mode == 'multi':
            turn = input(f"Selection for {player}: ")
        elif mode == 'single':
            if player == 'X':
                turn = input(f"Selection for {player}: ")
            else:
                print("Selection for Computer")
                turn = comp(tx, ty, tz, counter)
                print(f"Computer selected {turn}")
                time.sleep(1)

        try:
            turn = int(turn)
        except:
            complain = True
            continue

        if turn == 1 and legal_move(tz, 0):
            tz[0] = player
        elif turn == 2 and legal_move(tz, 1):
            tz[1] = player
        elif turn == 3 and legal_move(tz, 2):
            tz[2] = player
        elif turn == 4 and legal_move(ty, 0):
            ty[0] = player
        elif turn == 5 and legal_move(ty, 1):
            ty[1] = player
        elif turn == 6 and legal_move(ty, 2):
            ty[2] = player
        elif turn == 7 and legal_move(tx, 0):
            tx[0] = player
        elif turn == 8 and legal_move(tx, 1):
            tx[1] = player
        elif turn == 9 and legal_move(tx, 2):
            tx[2] = player
        elif turn == 0:
            print("Exiting")
            bye_felicia()
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
                bye_felicia()
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
                bye_felicia()
                break

def bye_felicia():
    print("")
    print("Game Over")
    print("Thanks for playing")

def legal_move(t, turn):
    if t[turn] == 'X' or t[turn] == 'O':
        return False
    else:
        return True

def ttt_reset():

    x = ['7', '8', '9' ]
    y = ['4', '5', '6' ]
    z = ['1', '2', '3' ]
    xcounter = 1

    return (x, y, z, xcounter)

def banner():
        print("###############")
        print("## TicTacToe ##")
        print("###############")
        print("Enter 0 to exit")
        print("")

def status_check(tx, ty, tz):
        os.system('clear')
        banner()
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
    """
    AI functionality introduced
    """

    time.sleep(1)
    if xcounter == 1:
        return random.choice([7, 9, 5, 1, 3])

    # First and second moves are randomized
    # with priority squares.
    # After 3rd move, all hell breaks loose, hahah

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
    # Also making copy before making changes
    ttt_map = avail
    for n in mlist:
        avail.pop(n)


    if xcounter == 2 or xcounter == 3:
        optimal_n = random.choice([7, 9, 5, 1, 3])
#        print(f"opt num selected is {optimal_n}")
        #while not legal_move(ttt_map[optimal_n]):
        #    print(f"{optimal_n} was rejected")
        #    optimal_n = random.choice([7, 9, 5, 1, 3])
        if 7 in xlist or 9 in xlist or 1 in xlist or 3 in xlist:
            if 5 in list(avail):
                return 5
        elif optimal_n in list(avail):
            return optimal_n
            # A random number from avail numbers
            # will be returned.

    ## When in doubt, ATTTAAACCCCKKKK
    if attack(survey):
        return

    ## Always defend
    ## Defensively attack!
    if defend(survey):
        return

    ## If all else fails, wing it!
    return (random.choice(list(avail)))


def attack(survey):
    """
    Offensive strategy
    """
    print("DEBUG: Offensive strategy engaged")
    scan_rx = { 7 : survey[7], 8 : survey[8], 9 : survey[9] }
    scan_ry = { 4 : survey[4], 5 : survey[5], 6 : survey[6] }
    scan_rz = { 1 : survey[1], 2 : survey[2], 3 : survey[3] }

    scan_19 = { 1 : survey[1], 5 : survey[5], 9 : survey[9]}
    scan_37 = { 3 : survey[3], 5 : survey[5], 7 : survey[7]}

    one = list(scan_19.values())
    three = list(scan_37.values())
    nrz = []
    nry = []
    nrx = []
    n19 = []
    n37 = []

    scan_c1 = { 7 : survey[7], 4 : survey[4], 1 : survey[1] }
    scan_c2 = { 8 : survey[8], 5 : survey[5], 2 : survey[2] }
    scan_c3 = { 9 : survey[9], 6 : survey[6], 3 : survey[3] }
    nc1 = []
    nc2 = []
    nc3 = []

    ## Offensive trategy
    if list(scan_rx).count('O') == 2:
        for k,v in scan_rx.items():
            if v == 'O':
                nrx.append(k)
        if sum(nrx) == 15 and legal_move(list(scan_rx), 2):
            return 9
        if sum(nrx) == 16 and legal_move(list(scan_rx), 1):
            return 8
        if sum(nrx) == 17 and legal_move(list(scan_rx), 0):
            return 7

    if list(scan_ry).count('O') == 2:
        for k,v in scan_ry.items():
            if v == 'O':
                nry.append(k)
        if sum(nry) == 9 and legal_move(list(scan_ry), 2):
            return 6
        if sum(nry) == 10 and legal_move(list(scan_ry), 1):
            return 5
        if sum(nry) == 11 and legal_move(list(scan_ry), 0):
            return 4

    if list(scan_rz).count('O') == 2:
        for k,v in scan_rz.items():
            if v == 'O':
                nrz.append(k)
        if sum(nrz) == 3 and legal_move(list(scan_rz), 2):
            return 3
        if sum(nrz) == 4 and legal_move(list(scan_rz), 1):
            return 2
        if sum(nrz) == 5 and legal_move(list(scan_rz), 0):
            return 1

    if one.count('O') == 2:
        for k,v in scan_19.items():
            if v == 'O':
                n19.append(k)
        if sum(n19) == 6 and legal_move(list(one), 2):
            return 9
        if sum(n19) == 10 and legal_move(list(one), 1):
            return 5
        if sum(n19) == 14 and legal_move(list(one), 0):
            return 1

    if three.count('O') == 2:
        for k,v in scan_37.items():
            if v == 'O':
                n37.append(k)
        if sum(n37) == 8 and legal_move(list(one), 2):
            return 7
        if sum(n37) == 10 and legal_move(list(one), 1):
            return 5
        if sum(n37) == 12 and legal_move(list(one), 0):
            return 3

    if list(scan_c1.values()).count('O') == 2:
        for k,v in scan_c1.items():
            if v == 'O':
                nc1.append(k)
        if sum(nc1) == 11 and legal_move(list(scan_c1), 2):
            return 1
        if sum(nc1) == 8 and legal_move(list(scan_c1), 1):
            return 4
        if sum(nc1) == 5 and legal_move(list(scan_c1), 0):
            return 7

    if list(scan_c2.values()).count('O') == 2:
        for k,v in scan_c2.items():
            if v == 'O':
                nc2.append(k)
        if sum(nc2) == 13 and legal_move(list(scan_c2), 2):
            return 2
        if sum(nc2) == 10 and legal_move(list(scan_c2), 1):
            return 5
        if sum(nc2) == 7 and legal_move(list(scan_c2), 0):
            return 8

    if list(scan_c3.values()).count('O') == 2:
        for k,v in scan_c3.items():
            if v == 'O':
                nc3.append(k)
        if sum(nc3) == 15 and legal_move(list(scan_c3), 2):
            return 3
        if sum(nc3) == 12 and legal_move(list(scan_c3), 1):
            return 6
        if sum(nc3) == 9 and legal_move(list(scan_c3), 0):
            return 9
    else:
        return 0

def defend(survey):
    ## Defensive strategy
    print("DEBUG: Defensive strategy engaged")
    scan_rx = { 7 : survey[7], 8 : survey[8], 9 : survey[9] }
    scan_ry = { 4 : survey[4], 5 : survey[5], 6 : survey[6] }
    scan_rz = { 1 : survey[1], 2 : survey[2], 3 : survey[3] }

    scan_19 = { 1 : survey[1], 5 : survey[5], 9 : survey[9]}
    scan_37 = { 3 : survey[3], 5 : survey[5], 7 : survey[7]}

    one = list(scan_19.values())
    three = list(scan_37.values())
    nrz = []
    nry = []
    nrx = []
    n19 = []
    n37 = []

    scan_c1 = { 7 : survey[7], 4 : survey[4], 1 : survey[1] }
    scan_c2 = { 8 : survey[8], 5 : survey[5], 2 : survey[2] }
    scan_c3 = { 9 : survey[9], 6 : survey[6], 3 : survey[3] }
    nc1 = []
    nc2 = []
    nc3 = []

    if list(scan_rx).count('X') == 2:
        for k,v in scan_rx.items():
            if v == 'X':
                nrx.append(k)
        if sum(nrx) == 15 and legal_move(list(scan_rx), 2):
            return 9
        if sum(nrx) == 16 and legal_move(list(scan_rx), 1):
            return 8
        if sum(nrx) == 17 and legal_move(list(scan_rx), 0):
            return 7

    if list(scan_ry).count('X') == 2:
        for k,v in scan_ry.items():
            if v == 'X':
                nry.append(k)
        if sum(nry) == 9 and legal_move(list(scan_ry), 2):
            return 6
        if sum(nry) == 11 and legal_move(list(scan_ry), 0):
            return 4
        if sum(nry) == 10 and legal_move(list(scan_ry), 1):
            return 5 ## Probably unnecessary so last ## comment from old algo

    if list(scan_rz).count('X') == 2:
        for k,v in scan_rz.items():
            if v == 'X':
                nrz.append(k)
        if sum(nrz) == 3 and legal_move(list(scan_rz), 2):
            return 3
        if sum(nrz) == 4 and legal_move(list(scan_rz), 1):
            return 2
        if sum(nrz) == 5 and legal_move(list(scan_rz), 0):
            return 1

    if one.count('X') == 2:
        for k,v in scan_19.items():
            if v == 'X':
                n19.append(k)
        if sum(n19) == 6 and legal_move(list(one), 2):
            return 9
        if sum(n19) == 14 and legal_move(list(one), 0):
            return 1
        if sum(n19) == 10 and legal_move(list(one), 1):
            return 5 ## Probably unnecessary so last

    if three.count('X') == 2:
        for k,v in scan_37.items():
            if v == 'X':
                n37.append(k)
        if sum(n37) == 8 and legal_move(list(one), 2):
            return 7
        if sum(n37) == 12 and legal_move(list(one), 0):
            return 3
        if sum(n19) == 10 and legal_move(list(one), 1):
            return 5 ## Probably unnecessary so last

    if list(scan_c1.values()).count('X') == 2:
        for k,v in scan_c1.items():
            if v == 'X':
                nc1.append(k)
        if sum(nc1) == 11 and legal_move(list(scan_c1), 2):
            return 1
        if sum(nc1) == 8 and legal_move(list(scan_c1), 1):
            return 4
        if sum(nc1) == 5 and legal_move(list(scan_c1), 0):
            return 7

    if list(scan_c2.values()).count('X') == 2:
        for k,v in scan_c2.items():
            if v == 'X':
                nc2.append(k)
        if sum(nc2) == 13 and legal_move(list(scan_c2), 2):
            return 2
        if sum(nc2) == 7 and legal_move(list(scan_c2), 0):
            return 8
        if sum(nc2) == 10 and legal_move(list(scan_c2), 1):
            return 5 ## Probably unnecessary so last

    if list(scan_c3.values()).count('X') == 2:
        for k,v in scan_c3.items():
            if v == 'X':
                nc3.append(k)
        if sum(nc3) == 15 and legal_move(list(scan_c3), 2):
            return 3
        if sum(nc3) == 12 and legal_move(list(scan_c3), 1):
            return 6
        if sum(nc3) == 9 and legal_move(list(scan_c3), 0):
            return 9
    else:
        return 0


if __name__ == "__main__":
    main()
