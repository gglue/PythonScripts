'''
Name: Victor Li
Date: 06/02/2022
Description: A simple script that gets the current prices of crypto using coinmarketcap.com
'''

from bs4 import BeautifulSoup
import requests
import sys

# Prints out the top 10 cryptocurrencies if no argument is given
if (len(sys.argv) == 1):
    # Get the HTML content
    page = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract the top 10 cryptocurrencies atm
    rank = 1
    ranking = []    
    table = (soup.find("tbody"))
    for crypto in (table.find_all("tr")):
        # Fetch rank, name and current price
        print("%d. " % rank, end="")
        print(crypto.find("p", class_="iworPT").text, end = "")
        print(crypto.find("div", class_="cLgOOr").text, end = "")

        # Fetch change from past day and past week
        # The change daily and weekly have the same classname, so I used a for statement
        status = crypto.find_all("span", class_="sc-15yy2pl-0")
        for change in status:
            if(change.find("span", class_="icon-Caret-up")):
                print("Up " + change.parent.text, end ="")
            else:
                print("Down " + change.parent.text, end = "")

        # Fetch Market Cap
        print(crypto.find("span", class_="ieFnWP").text)

        # Print up to the given rank value
        rank += 1
        if (rank > 10): break
else:
    print("found")

