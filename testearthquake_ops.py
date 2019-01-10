#!/usr/bin/env python3.6

import os
import csv
import time
from datetime import datetime
from pytz import timezone
import subprocess


def main():

    DEBUG = False

    loc_src_list = []
    eq_count_db = {}

    live_data()


    # with open('1.0_month.csv', ) as eq_data:
    #     read_eq_data = csv.DictReader(eq_data, delimiter=',')
    #     for row in read_eq_data:
    #         print(row)

#     a = 4
#     b = [3,6]
#     emptyl = [2, 5]
#     print(emptyl)
#     emptyl.append(b)
# #    emptyl.extend(b)
#     print(emptyl)
#     print("")

#     for x in emptyl:
#         print(x)

def live_data(master_live_db={}, old_timestamp='', xcounter=1):

    """
     Deep underground usage limits the growth of
     locations to mem_max size. It will not accept 
     new entries into DB, but will continue to display
     stats.
    """
    mem_max = 2

    ## test ## loc_src_list = {'AK': 3274, 'UU': 202, 'CI': 673, 'NC': 550, 'US': 773, 'NN': 320, 'NM': 25, 'PR': 530, 'UW': 79, 'HV': 264, 'MB': 131, 'OK': 10, 'SE': 22, 'LD': 2, 'ROM': 1, 'AV': 21, 'ISMP': 3}
    """
     Uses generator to load the data and
     grab the last line. Should allow for 
     very low memory consumption as unpacking
     of data should happen on the fly.
    """
    my_eq_data = (x for x in get_eq_csv())
    *head, quake = my_eq_data
    quake = dict(quake)
    new_timestamp = quake['time']
    loc = quake['locationSource'].upper()

    if new_timestamp == old_timestamp:
        time.sleep(60) """ Checks every 60 seconds, unless data is pouring in """
        return live_data(master_live_db, new_timestamp, xcounter)

    """
         master_live_db configuration:
      { location : [ magnitude , counter ] }
    """
    if len(list(master_live_db)) == mem_max:
        pass  ## 
    elif loc not in list(master_live_db):
        master_live_db.update( { loc : [ float(quake['mag']) , 1 ] } )
    else:
        master_live_db.update( { loc : [ ( ( master_live_db[loc][0] + float(quake['mag']) ) / 2 ) , ( master_live_db[loc][1] + 1 ) ] } )

    os.system('clear')
    print('Displaying live average magnitude data')
    print("Use CTRL-C to break out")
    print(master_live_db)
    print("|Place | # of Earthquakes | Average Magnitude|")
    for k,v in master_live_db.items():
        print(f"|--{k}--|----{v[1]}----|----{v[0]}----|")
    print(xcounter) #DEBUG
    xcounter += 1 #DEBUG
    time.sleep(1) #DEBUG
    

    return live_data(master_live_db, new_timestamp, xcounter) ## counter for checking recursion




def get_eq_csv():
    with open('/Users/Zanfer/Desktop/ZanferTech/GitHub/algotesting/1.1_month.csv') as eq_data: ### Testing live data with copy of csv that updates
        read_eq_data = csv.DictReader(eq_data, delimiter=',')
        for quake in read_eq_data:
            yield quake




if __name__ == "__main__":
    main()
