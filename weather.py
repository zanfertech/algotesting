#!/usr/bin/env python3.6

import requests
import sys
import argparse

def main():
    print("Hello")

    allinput = argparse.ArgumentParser(description='This righ heann, takes zip and country and spits out weather')

    allinput.add_argument("zipcode", help="Neeeeeds a zip code now, ya hea")
    allinput.add_argument("--countrycode", default="us", help="add country if not US of A")

    thisparse = allinput.parse_args()

    appid = '32abecdeea1d33f0a9d38bd300538b16'
    zipcode = thisparse.zipcode
    countrycode = thisparse.countrycode
                         #https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={appid}"
    urlget = requests.get(url).json()


    durl = dict(urlget)

    for k,v in durl.items():
        print(f"{k} corresponds to {v}")   # and {v[1]}")


if __name__ == '__main__':
    main()
