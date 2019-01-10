#!/usr/bin/env python3.6

import os
import csv
import time
from datetime import datetime
from pytz import timezone


def main():
    """
        Earthquake Programming Challenge
    """

    DEBUG = False

    m_menu()



def most_eqs():
    """
     Prints location with the most earthquakes
     As well as a pretty graph
    """
    DEBUG = False
    loc_src_list = get_loc_list()
    eq_count_db = {}

    print("Loading...")



    for loc in loc_src_list:
        head, *quake = get_eq_csv()
        eq_count = 0
        for row in quake:
            if row['locationSource'] == loc:
                eq_count += 1
        
        eq_count_db.update( { loc.upper() : eq_count } )

    print("")
    max_val = (sorted(eq_count_db.values(), reverse=True)[0])

    os.system('clear')
    print("Number of earthquakes per day:")
    print("")
    for k, v in eq_count_db.items():
        if v == max_val:
            print(f"The location with the most earthquakes is {k}")
    print("")

    ## Graphical breakdown of earthquakes per location
    for k, v in eq_count_db.items():
        print(f"{k}:\t{v}\t]{'#' * int(v*100/max_val)}")
    
    m_menu()


def eqs_per_day():
    """
    Histogram of the number of earthquakes per day in UTC
    """
    DEBUG = False
    eq_date_list = []
    eq_date_db = {}

    print("Loading...")
    quake = get_eq_csv()
    for row in quake:
        eq_date = (row['time']).split('T')[0]
        if eq_date not in eq_date_list:
            eq_date_list.append(eq_date)
    
    
    for eq_date in eq_date_list:
        quake = get_eq_csv()
        dcounter = 0
        for row in quake:
            if eq_date == (row['time']).split('T')[0]:
                dcounter += 1
        eq_date_db.update( { eq_date : dcounter } )

    os.system('clear')
    print("Number of earthquakes per day:")
    print("")
    for k, v in eq_date_db.items():
        print(f"{k}: [{v}] {'#' * int(v/10)}")

    m_menu()


def avg_magnitude():
    """
    Average earthquake magnitude for each location source
    """

    avg_mag_db = {}
    loc_src_list = get_loc_list()
    
    os.system('clear')
    print("Average earthquake magnitude:")
    print("")
    for loc in loc_src_list:
        quake = get_eq_csv()
        mag_per_loc = []
        for row in quake:
            if row['locationSource'] == loc:
                mag_per_loc.append(float(row['mag']))
        ## Per project scope definition, divide by zero shouldn't happen
        ## But we'll check anyway
        if len(mag_per_loc) == 0:
            avg_mag = 0
        else:
            avg_mag = ( sum(mag_per_loc) / len(mag_per_loc) ) 

        print(f"{loc.upper()} has had earthquakes with an average magnitudes of { avg_mag } ")
        ## Save to a dict
        avg_mag_db.update({ loc.upper() : avg_mag  })

    m_menu()


def live_data(master_live_db={}, old_timestamp=''):

    """
     Deep underground usage limits the growth of
     locations to mem_max size. It will not accept 
     new entries into DB, but will continue to display
     stats.
    """
    mem_max = 100

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
        time.sleep(60) ## Checks every 60 seconds, unless data is pouring in
        return live_data(master_live_db, new_timestamp)

    """
         master_live_db configuration:
      { location : [ magnitude , counter ] }
    """
    if len(list(master_live_db)) == mem_max:
        pass 
    elif loc not in list(master_live_db):
        master_live_db.update( { loc : [ float(quake['mag']) , 1 ] } )
    else:
        master_live_db.update( { loc : [ ( ( master_live_db[loc][0] + float(quake['mag']) ) / 2 ) , ( master_live_db[loc][1] + 1 ) ] } )

    os.system('clear')
    print('Displaying live average magnitude data')
    print("Use CTRL-C to break out")
    print("")    
    print("|Place | # of Earthquakes | Average Magnitude|")
    for k,v in master_live_db.items():
        print(f"|-- {k} --|---- {v[1]} ----|---- {v[0]} ----|")

    
    return live_data(master_live_db, new_timestamp)


def m_menu():
    while True:
        print("")
        print("  1. Location with the most earthquakes")
        print("  2. Histogram of the number of earthquakes per day in UTC")
        print("  3. Average earthquake magnitude by location")
        print("  4. Live data stream (Beta)")
        print("  0. Exit")
        print("")
        
        try:
            option = int(input("Please select from options 1-4: "))
        except:
            print("Invalid selection - Please try again")
            continue

        if option == 1:
            most_eqs()
        elif option == 2:
            eqs_per_day()
        elif option == 3:
            avg_magnitude()
        elif option == 4:
            live_data()
        elif option == 0:
            print("Have a nice day")
            exit()
        else:
            print("Invalid selection - Please try again")


def get_loc_list():
    """
     Provides other functions with a list of all locations
     """
    DEBUG = False

    loc_src_list = []
    quake = get_eq_csv()
    for row in quake:
        if row['locationSource'] not in loc_src_list:
                loc_src_list.append(row['locationSource'])

    if DEBUG:
        print(f"List of unique locations: {loc_src_list}")

    return loc_src_list


def get_eq_csv():
    
    with open('1.0_month.csv') as eq_data: ### Testing live data with copy of csv that updates
        read_eq_data = csv.DictReader(eq_data, delimiter=',')
        for quake in read_eq_data:
            yield quake        

if __name__ == "__main__":
    main()
