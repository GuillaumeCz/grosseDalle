#!/usr/bin/python

import datetime
import sys
import requests
from bs4 import BeautifulSoup


now = datetime.datetime.now()
week = format(datetime.date(now.year, now.month, now.day).isocalendar()[1], '02d')
url = 'http://www.r2c-restauration.fr/suggestion-de-la-semaine-s'+week+'-2018'
req = requests.get(url).text
soup = BeautifulSoup(req, "lxml")


def display_menu():
    menu = ""
    headers = soup.find_all("h3")
    rows = soup.find("table").find_all("td")

    entrees = rows[0:8]
    plats = rows[9:21]

    menu += "--> "+headers[0].string.encode('ascii', 'ignore') + "\n"
    for entree in entrees:
        menu += "\t"+entree.string.encode('ascii', 'ignore')+ "\n"

    menu += "--> "+headers[1].string.encode('ascii', 'ignore') + "\n"
    for plat in plats:
        menu += "\t"+plat.string.encode('ascii', 'ignore')+"\n"

    print menu 

def main(argv=None):
    display_menu()

if __name__ == '__main__':
    main()

