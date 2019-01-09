#!/usr/bin/env python3.6

import time
import random
import os

def main():
    r1 = ttt_reset()[0]
    r2 = ttt_reset()[1]
    r3 = ttt_reset()[2]
    counter = ttt_reset()[3]

    cortex(r1, r2, r3, counter)

"""
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

    r1 = ttt_reset()[0]
    r2 = ttt_reset()[1]
    r3 = ttt_reset()[2]
    counter = ttt_reset()[3]

    player = choose_player()


    complain = False
    TTT = False
    while not TTT:
        #print(f"DEBUG - counter = {counter}")
        status_check(r1, r2, r3)

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
                turn = comp(r1, r2, r3, counter)
                print(f"Computer selected {turn}")
                time.sleep(1)

        try:
            turn = int(turn)
        except:
            complain = True
            continue

        if turn == 1 and legal_move(r3, 0):
            r3[0] = player
        elif turn == 2 and legal_move(r3, 1):
            r3[1] = player
        elif turn == 3 and legal_move(r3, 2):
            r3[2] = player
        elif turn == 4 and legal_move(r2, 0):
            r2[0] = player
        elif turn == 5 and legal_move(r2, 1):
            r2[1] = player
        elif turn == 6 and legal_move(r2, 2):
            r2[2] = player
        elif turn == 7 and legal_move(r1, 0):
            r1[0] = player
        elif turn == 8 and legal_move(r1, 1):
            r1[1] = player
        elif turn == 9 and legal_move(r1, 2):
            r1[2] = player
        elif turn == 0:
            print("Exiting")
            bye_felicia()
            break
        else:
            complain = True
            continue

        TTT = check_ttt(r1, r2, r3, player)
        if TTT:
            status_check(r1, r2, r3)
            print("")
            print(f"TicTacToe - {player} wins")
            print("")
            if replay():
                ttt_reset()
                r1 = ttt_reset()[0]
                r2 = ttt_reset()[1]
                r3 = ttt_reset()[2]
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
            status_check(r1, r2, r3)
            print("Tie Game")
            print("")
            if replay():
                ttt_reset()
                r1 = ttt_reset()[0]
                r2 = ttt_reset()[1]
                r3 = ttt_reset()[2]
                counter = ttt_reset()[3]
                TTT = False
                player = choose_player()
                continue
            else:
                bye_felicia()
                break
    """

def bye_felicia():
    print("")
    print("Game Over")
    print("Thanks for playing")

def legal_move(t, turn):
    if t[turn] == 'X' or t[turn] == 'O':
        return False
    else:
        return True



def banner():
        os.system('clear')
        print("###############")
        print("## TicTacToe ##")
        print("###############")
        print("Enter 0 to exit")
        print("")

def status_check(r1, r2, r3):
        banner()
        print("")
        print(*r1, sep=" | ")
        print("--+---+--")
        print(*r2, sep=" | ")
        print("--+---+--")
        print(*r3, sep=" | ")
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

def check_ttt(r1, r2, r3, player):

    if r1[0] == r1[1] == r1[2] or r2[0] == r2[1] == r2[2] or r3[0] == r3[1] == r3[2]:
        return player
    elif r1[0] == r2[0] == r3[0] or r1[1] == r2[1] == r3[1] or r1[2] == r2[2] == r3[2]:
        return player
    elif r1[0] == r2[1] == r3[2] or r1[2] == r2[1] == r3[0]:
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

def ttt_reset():
    """
    Resets board (or single array) to numerical
    digits

    Default layout and map:
    #    c1    c2   c3
    r1 = ['7', '8', '9' ]
    r2 = ['4', '5', '6' ]
    r3 = ['1', '2', '3' ]
    #  v19             v37
    xcounter = 1
    """
    ## Redefined layout for AI testing

    r1 = ['7', '8', '9' ]
    r2 = ['4', '5', '6' ]
    r3 = ['1', '2', '3' ]
    xcounter = 1

    return (r1, r2, r3, xcounter)

##################NEW AI#################
def foresite(survey, opos, xpos):
    """
    Recursive function to evaluate next move
    """
    vr1 = (survey[7], survey[8], survey[9])
    vr2 = (survey[4], survey[5], survey[6])
    vr3 = (survey[1], survey[2], survey[3])
    
    vc1 = (survey[7], survey[4], survey[1])
    vc2 = (survey[8], survey[5], survey[2])
    vc3 = (survey[9], survey[6], survey[3])

    v19 = (survey[1], survey[5], survey[9])
    v37 = (survey[3], survey[5], survey[7])


    if opos == 1:
        check_vectors(vr3, vc1, v19)
    elif opos == 2:
        check_vectors(vr3, vc2)
    elif opos == 3:
        check_vectors(vr3, vc3, v37)
    elif opos == 4:
        check_vectors(vr2, vc1)
    elif opos == 5:
        check_vectors(vr2, vc2, v19, v37)
    elif opos == 6:
        check_vectors(vr2, vc3)
    elif opos == 7:
        check_vectors(vr1, vc1, v37)
    elif opos == 8:
        check_vectors(vr1, vc2)
    elif opos == 9:
        check_vectors(vr1, vc3, v19)


def check_vectors(vr, vc, vd1=[], vd2=[]):
    """
    Checks row vector 'vr', column vector 'vc'
    and diagonal vector 'vd' if not null.
    """
    print(f"Vector vr is {vr}")
    print(f"Vector vc is {vc}")
    print(f"Vector vd is {vd1}")
    print(f"Vector vd is {vd2}")


def best_chance(survey, xcounter):
    """
    Best chance to win, based on all possible
    variations
    """
    DEBUG = True

    if DEBUG:
        print(f"DEBUG: counter at {xcounter}")
        print(f"DEBUG: lenth of survey {len(survey)}")
        print(f"DEBUG: contents of survey {survey}")
    
    avail_list = list(range(1, 10))
    if DEBUG:
        print(f"DEBUG: avail_list before is {avail_list}")
    for k, v in survey.items():
        if v == 'X' or v == 'O':
            avail_list.pop(k)
    if DEBUG:
        print(f"DEBUG: avail_list after is {avail_list}")

    if xcounter == 1:
        for opos in range(1, ( len(survey) + 1 )):
            avail_list.pop(opos)
            if DEBUG:
                print(f"DEBUG: avail_list after opos pop is {avail_list}")
            for xpos in avail_list:
                if DEBUG:
                    print(f"DEBUG: xpos at {opos}")
                    print(f"DEBUG: oppos at {xpos}")
                foresite(survey, opos, xpos)
            


def cortex(r1, r2, r3, xcounter):
    """
    Advance calculations in order to determine
    best possible move.
    """

    ## Construct grid

    survey = { 1 : r3[0] , 2 : r3[1] , 3 : r3[2] ,
            4 : r2[0] , 5 : r2[1] , 6 : r2[2] ,
            7 : r1[0] , 8 : r1[1] , 9 : r1[2] }

    ## Determine counter based on avaialble squares
    xcounter = (list(survey.values()).count('O') + list(survey.values()).count('X')) + 1
    
    #here we go
    best_chance(survey, xcounter)








    """
def comp(r1, r2, r3, xcounter):
    """
    ## AI functionality introduced
    """

    time.sleep(1)
    if xcounter == 1:
        return random.choice([7, 9, 5, 1, 3])

    # First and second moves are randomized
    # with priority squares.
    # After 3rd move, all hell breaks loose, hahah

    # Build comps personal mapping of board
    survey = { 1 : r3[0] , 2 : r3[1] , 3 : r3[2] ,
            4 : r2[0] , 5 : r2[1] , 6 : r2[2] ,
            7 : r1[0] , 8 : r1[1] , 9 : r1[2] }

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


    scan_r1 = { 7 : survey[7], 8 : survey[8], 9 : survey[9] }
    scan_r2 = { 4 : survey[4], 5 : survey[5], 6 : survey[6] }
    scan_r3 = { 1 : survey[1], 2 : survey[2], 3 : survey[3] }

    scan_lr1 = list(scan_r1.values())
    scan_lr2 = list(scan_r2.values())
    scan_lr3 = list(scan_r3.values())

    scan_19 = { 1 : survey[1], 5 : survey[5], 9 : survey[9]}
    scan_37 = { 3 : survey[3], 5 : survey[5], 7 : survey[7]}

    one = list(scan_19.values())
    three = list(scan_37.values())
    nr3 = []
    nr2 = []
    nr1 = []
    n19 = []
    n37 = []

    scan_c1 = { 7 : survey[7], 4 : survey[4], 1 : survey[1] }
    scan_c2 = { 8 : survey[8], 5 : survey[5], 2 : survey[2] }
    scan_c3 = { 9 : survey[9], 6 : survey[6], 3 : survey[3] }
    scan_lc1 = list(scan_c1.values())
    scan_lc2 = list(scan_c2.values())
    scan_lc3 = list(scan_c3.values())
    nc1 = []
    nc2 = []
    nc3 = []

    ## Offensive strategy
    if list(scan_lr1).count('O') == 2:
        for k,v in scan_r1.items():
            if v == 'O':
                nr1.append(k)
        if sum(nr1) == 15 and legal_move(list(scan_lr1), 2):
            return 9
        if sum(nr1) == 16 and legal_move(list(scan_lr1), 1):
            return 8
        if sum(nr1) == 17 and legal_move(list(scan_lr1), 0):
            return 7

    if list(scan_lr2).count('O') == 2:
        for k,v in scan_r2.items():
            if v == 'O':
                nr2.append(k)
        if sum(nr2) == 9 and legal_move(list(scan_lr2), 2):
            return 6
        if sum(nr2) == 10 and legal_move(list(scan_lr2), 1):
            return 5
        if sum(nr2) == 11 and legal_move(list(scan_lr2), 0):
            return 4

    if list(scan_lr3).count('O') == 2:
        for k,v in scan_r3.items():
            if v == 'O':
                nr3.append(k)
        if sum(nr3) == 3 and legal_move(list(scan_lr3), 2):
            return 3
        if sum(nr3) == 4 and legal_move(list(scan_lr3), 1):
            return 2
        if sum(nr3) == 5 and legal_move(list(scan_lr3), 0):
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
        if sum(n37) == 8 and legal_move(list(three), 2):
            return 7
        if sum(n37) == 10 and legal_move(list(three), 1):
            return 5
        if sum(n37) == 12 and legal_move(list(three), 0):
            return 3

    if list(scan_lc1).count('O') == 2:
        for k,v in scan_c1.items():
            if v == 'O':
                nc1.append(k)
        if sum(nc1) == 11 and legal_move(list(scan_lc1), 2):
            return 1
        if sum(nc1) == 8 and legal_move(list(scan_lc1), 1):
            return 4
        if sum(nc1) == 5 and legal_move(list(scan_lc1), 0):
            return 7

    if list(scan_lc2).count('O') == 2:
        for k,v in scan_c2.items():
            if v == 'O':
                nc2.append(k)
        if sum(nc2) == 13 and legal_move(list(scan_lc2), 2):
            return 2
        if sum(nc2) == 10 and legal_move(list(scan_lc2), 1):
            return 5
        if sum(nc2) == 7 and legal_move(list(scan_lc2), 0):
            return 8

    if list(scan_lc3).count('O') == 2:
        for k,v in scan_c3.items():
            if v == 'O':
                nc3.append(k)
        if sum(nc3) == 15 and legal_move(list(scan_lc3), 2):
            return 3
        if sum(nc3) == 12 and legal_move(list(scan_lc3), 1):
            return 6
        if sum(nc3) == 9 and legal_move(list(scan_lc3), 0):
            return 9


    ## Defensive strategy
    if list(scan_lr1).count('X') == 2:
        for k,v in scan_r1.items():
            if v == 'X':
                nr1.append(k)
        if sum(nr1) == 15 and legal_move(list(scan_lr1), 2):
            return 9
        if sum(nr1) == 16 and legal_move(list(scan_lr1), 1):
            return 8
        if sum(nr1) == 17 and legal_move(list(scan_lr1), 0):
            return 7

    if list(scan_lr2).count('X') == 2:
        for k,v in scan_r2.items():
            if v == 'X':
                nr2.append(k)
        if sum(nr2) == 9 and legal_move(list(scan_lr2), 2):
            return 6
        if sum(nr2) == 11 and legal_move(list(scan_lr2), 0):
            return 4
        if sum(nr2) == 10 and legal_move(list(scan_lr2), 1):
            return 5 ## Probably unnecessary so last ## comment from old algo

    if list(scan_lr3).count('X') == 2:
        for k,v in scan_r3.items():
            if v == 'X':
                nr3.append(k)
        if sum(nr3) == 3 and legal_move(list(scan_lr3), 2):
            return 3
        if sum(nr3) == 4 and legal_move(list(scan_lr3), 1):
            return 2
        if sum(nr3) == 5 and legal_move(list(scan_lr3), 0):
            return 1

    #print(f"DEBUG: testing one {one}")
    if list(one).count('X') == 2:
        for k,v in scan_19.items():
            if v == 'X':
                n19.append(k)
        if sum(n19) == 6 and legal_move(list(one), 2):
            return 9
        if sum(n19) == 10 and legal_move(list(one), 1):
            return 5
        if sum(n19) == 14 and legal_move(list(one), 0):
            return 1

    #print(f"DEBUG: testing three {three}")
    if list(three).count('X') == 2:
        for k,v in scan_37.items():
            if v == 'X':
                n37.append(k)
        if sum(n37) == 8 and legal_move(list(three), 2):
            return 7
        if sum(n19) == 10 and legal_move(list(three), 1):
            return 5
        if sum(n37) == 12 and legal_move(list(three), 0):
            return 3

    if list(scan_lc1).count('X') == 2:
        for k,v in scan_c1.items():
            if v == 'X':
                nc1.append(k)
        if sum(nc1) == 11 and legal_move(list(scan_lc1), 2):
            return 1
        if sum(nc1) == 8 and legal_move(list(scan_lc1), 1):
            return 4
        if sum(nc1) == 5 and legal_move(list(scan_lc1), 0):
            return 7

    if list(scan_lc2).count('X') == 2:
        for k,v in scan_c2.items():
            if v == 'X':
                nc2.append(k)
        if sum(nc2) == 13 and legal_move(list(scan_lc2), 2):
            return 2
        if sum(nc2) == 10 and legal_move(list(scan_lc2), 1):
            return 5
        if sum(nc2) == 7 and legal_move(list(scan_lc2), 0):
            return 8

    if list(scan_lc3).count('X') == 2:
        for k,v in scan_c3.items():
            if v == 'X':
                nc3.append(k)
        if sum(nc3) == 15 and legal_move(list(scan_lc3), 2):
            return 3
        if sum(nc3) == 12 and legal_move(list(scan_lc3), 1):
            return 6
        if sum(nc3) == 9 and legal_move(list(scan_lc3), 0):
            return 9



    return (random.choice(list(avail)))
    """

if __name__ == "__main__":
    main()
