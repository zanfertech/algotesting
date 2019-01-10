#!/usr/bin/env python3.6

import os
import csv
import time
from datetime import datetime
from pytz import timezone

this = "2019-01-04T12:40:36.560Z"
thisnow = this.split("T")[0]
print(thisnow + '\n')

def main():
    """
        Earthquake Programming Challenge
    Task
    Write a Python program to analyze earthquake data. We are mainly looking for the organization, structure, and
    approach to solving the problems. The output of the code can be as simple as print statements or return values. Feel
    free to include unit tests if necessary.
    Download the data
    Download the newest CSV from the 30 day M1.0+ Earthquake feed from the website
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php and include it with your program.
    Requirements
    Please use Python 3.x. You may refer to outside sources for syntactical help or documentation, but not for looking up
    anything specific to the questions. You can use any standard library in Python, but you may only use the external
    libraries dateutil and pytz. All other third-party libraries are off-limits.
    Questions
    Below are four questions relating to the CSV.

    1. Which location source had the most earthquakes?
    2. Compute the data for a histogram of the number of earthquakes per day in UTC timezone. You do not need to
    plot the histogram, just compute the data that would be required to plot it.
        a. The program should print or return data points which represent the number of earthquakes in each
        respective day.
        b. Extra credit: Add an argument to your program that modifies it to compute the number of earthquakes per
        day in Pacific timezone instead of UTC.
    3. Compute the average earthquake magnitude for each location source.
    4. Pretend that the CSV is a real-time stream of earthquake data. Provide an object that can process 1 CSV row at a
    time and return the average earthquake magnitude for each location source when queried.
        a. Extra credit: Modify the behavior of your object written in answer #4: Imagine that this code is going to be
        running for years at a time without being restarted on a device buried deep underground with a fixed
        amount of memory available. This means you cannot safely store the sum of earthquake magnitudes or
        write the sum to disk. You can still keep a count of the number of earthquakes in memory.
    """
    
    # avg_mag_per_loc()

    # try:
    #     with open('1.0_month.csv') as eq_data:
    #         read_eq_data = csv.reader(eq_data, delimiter=',')
    # except:
    #     os.system('wget https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv')
    #     with open('1.0_month.csv') as eq_data:
    #         read_eq_data = csv.reader(eq_data, delimiter=',')

    #         for row in read_eq_data:
    #             print(row)
    DEBUG = False

    loc_src_list = []
    eq_count_db = {}

    with open('1.0_month.csv') as eq_data:
        read_eq_data = csv.DictReader(eq_data, delimiter=',')
        for row in read_eq_data:
            if row['locationSource'] not in loc_src_list:
                loc_src_list.append(row['locationSource'])
        if DEBUG:
            print(f"List of unique locations: {loc_src_list}")

        for loc in loc_src_list:
            eq_data.seek(0)
            eq_count = 0
            for row in read_eq_data:
                if row['locationSource'] == loc:
                    eq_count += 1
            
            eq_count_db.update( { loc.upper() : eq_count } )
        print(eq_count_db)
        print("")
        max_val = (sorted(eq_count_db.values(), reverse=True)[0])

        for k, v in eq_count_db.items():
            if v == max_val:
                print(f"The location with the most earthquakes is {k}")
        print("")

        ## Graphical breakdown of earthquakes per location
        for k, v in eq_count_db.items():
            print(f"{k}: {'#' * int(v/10)}")
        
        print("")
        print("")

        
        eq_data.seek(0)
        eq_date_list = []
        eq_date_db = {}

        for row in read_eq_data:
            eq_date = (row['time']).split('T')[0]
            if eq_date not in eq_date_list:
                eq_date_list.append(eq_date)
        
        
        for eq_date in eq_date_list:
            eq_data.seek(0)
            dcounter = 0
            for row in read_eq_data:
                if eq_date == (row['time']).split('T')[0]:
                    dcounter += 1
            eq_date_db.update( { eq_date : dcounter } )
        print(eq_date_db)

        print("")
        print("")
        for k, v in eq_date_db.items():
            print(f"{k}: [{v}] {'#' * int(v/10)}")

        avg_mag_db = {}
        for loc in loc_src_list:
            eq_data.seek(0)
            mag_per_loc = []
            for row in read_eq_data:
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
        print(avg_mag_db)


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
    print("|Place | # of Earthquakes | Average Magnitude|")
    for k,v in master_live_db.items():
        print(f"|--{k}--|----{v[1]}----|----{v[0]}----|")

    
    return live_data(master_live_db, new_timestamp)




def get_eq_csv():
    with open('1.0_month.csv') as eq_data: ### Testing live data with copy of csv that updates
        read_eq_data = csv.DictReader(eq_data, delimiter=',')
        for quake in read_eq_data:
            yield quake        









if __name__ == "__main__":
    main()
