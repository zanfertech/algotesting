#!/usr/bin/env python3.6

import os
import csv
import time
from datetime import datetime, timedelta
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
        quake = get_eq_csv()
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
        print(f"{k}:\t{v}\t|{'#' * int(v*100/max_val)}")
    



def eqs_per_day(offset):
    """
    Histogram of the number of earthquakes per day in UTC
    """
    DEBUG = False
    eq_date_list = []
    eq_date_db = {}



    print("Loading...")
    quake = get_eq_csv()
    for row in quake:
        eq_date = convert_utc_to_pacific(row['time'], offset)
        if eq_date not in eq_date_list:
            eq_date_list.append(eq_date)
    
    
    for eq_date in eq_date_list:
        quake = get_eq_csv()
        dcounter = 0
        for row in quake:
            if eq_date == convert_utc_to_pacific(row['time'], offset):
                dcounter += 1
        eq_date_db.update( { eq_date : dcounter } )

    os.system('clear')
    print("Number of earthquakes per day:")
    print("")
    for k, v in eq_date_db.items():
        print(f"{k}: [{v}] {'#' * int(v/10)}")




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
                mag_per_loc.append(float(row['mag'])
        ## Per project scope definition, divide by zero shouldn't happen
        ## But we'll check anyway
        if len(mag_per_loc) == 0:
            avg_mag = 0
        else:
            avg_mag = ( sum(mag_per_loc) / len(mag_per_loc) ) 

        print(f"{loc.upper()} has had earthquakes with an average magnitudes of { avg_mag } ")
        ## Save to a dict
        avg_mag_db.update({ loc.upper() : avg_mag  })


master_live_db={}
def process_live_data_row(row):
    ## takes 1 row of live data feed as an input and processes it
    loc = row['locationSource'].upper()
    if loc not in list(master_live_db):
        master_live_db.update( { loc : [ float(row['mag']) , 1 ] } )
    else:
        count = master_live_db[loc][1]
        newmag = (master_live_db[loc][0] * count + float(row['mag'])) / (count + 1)
        master_live_db.update( { loc : [ newmag, count + 1 ] } )

def live_data(old_timestamp=''):
    quake = get_eq_csv()
    mag_per_loc = []
    for row in quake:
        time.sleep(1)
        process_live_data_row(row)
        refresh_monitor()

def refresh_monitor():
    os.system('clear')
    print('Displaying live average magnitude data')
    print("Use CTRL-C to break out")
    print("")    
    print("|Place | # of Earthquakes | Average Magnitude|")
    for k,v in master_live_db.items():
        print(f"|-- {k} --|---- {v[1]} ----|---- {v[0]} ----|")



def m_menu():
    while True:
        print("")
        print("  1. Location with the most earthquakes")
        print("  2. Histogram of the number of earthquakes per day in UTC")
        print("  3. Histogram of the number of earthquakes per day in Pacific Time")
        print("  4. Average earthquake magnitude by location")
        print("  5. Live data stream (Beta)")
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
            eqs_per_day(0)
        elif option == 3:
            eqs_per_day(-8)
        elif option == 4:
            avg_magnitude()
        elif option == 5:
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


def convert_utc_to_pacific(utcdatetime, offset):
    utc = datetime.strptime(utcdatetime, "%Y-%m-%dT%H:%M:%S.%fZ")
    pacific = utc + timedelta(hours = offset)
    return str(pacific).split(' ')[0]

def get_eq_csv():
    
    with open('1.0_month.csv') as eq_data: ### Testing live data with copy of csv that updates
        read_eq_data = csv.DictReader(eq_data, delimiter=',')
        for quake in read_eq_data:
            yield quake        

if __name__ == "__main__":
    main()

