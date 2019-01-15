#!/usr/bin/env python3.6

from time import sleep
import random
import os


class Advanced_AI:

    def __init__(self, r1, r2, r3, xcounter):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.xcounter = xcounter


    def test_ttt():
    """
    This is the from the opening from main()
    I re-named it to test_ttt()
    """
        r1 = ttt_reset()[0]
        r2 = ttt_reset()[1]
        r3 = ttt_reset()[2]
        counter = ttt_reset()[3]

        cortex(r1, r2, r3, counter)

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
    Algo:

    def grid
    {
    3x3 matrix
    }

    rules for determining if ‘legal seq in grid’
    {
    any squares in a linear order that spans from one end of the grid to the other
    }

    rules for ‘best chance to win’ {
    possibils are ‘legal seq in grid’
    return possibils minus moves that lose minus moves that end in draw	
    }

    def check_all_squares
    for selfpo is 1-9
        for oppo is 1-9.pop(selfpo):
        all_possibils are grid-in-list popping slfpo and oppo
        winning possibils are all combinations that can make a  ‘legal seq in grid’
        which po next gives the ‘best chance to win’ and not lose
    ## I’d like to use a recursive function here t do the following: 
    # recurs(aviailist, loselist, selfpo, oppo)
    #        calulate all possibilites for po
    #       recurs((send all pertinent params for next iteration))
    #
    # whats the best current position

    def different_way_to_say_it
        at current position, given all avail square, which squares give me the best chance to win
        if lenght of bes po is > 1 randomly choose the next pos
            otherwise choose the best po
        bestlist = (availlist - loselist)
        incrmnt oppo 
        
        if no ‘best chance to win’ avail
            accept draw


    never accept defeat
        raise exception if you have to

        """


    def legal_move(t, turn):
        if t[turn] == 'X' or t[turn] == 'O':
            return False
        else:
            return True




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



    def check_ttt(r1, r2, r3, player):
    """
    OLD
    """
        if r1[0] == r1[1] == r1[2] or r2[0] == r2[1] == r2[2] or r3[0] == r3[1] == r3[2]:
            return player
        elif r1[0] == r2[0] == r3[0] or r1[1] == r2[1] == r3[1] or r1[2] == r2[2] == r3[2]:
            return player
        elif r1[0] == r2[1] == r3[2] or r1[2] == r2[1] == r3[0]:
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