'''
Name: Victor Li
Date: 06/02/2022
Description: A simple script that gets the current prices of crypto using coinmarketcap.com
'''

import requests
import sys
import bs4

# Prints out the top 10 cryptocurrencies if no argument is given
if (sys.argv[1] == None):
    print("none found")
else:
    print("found")

