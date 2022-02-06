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

    # Print table captions
    print("%2s %-15s %-15s %-15s %-15s %-15s" % ("#", "Name", "Price", "Daily Change", "Weekly Change", "Market Cap"))

    # Extract the top 10 cryptocurrencies atm
    rank = 1  
    table = (soup.find("tbody"))
    for crypto in (table.find_all("tr")):
        # Fetch name and current price
        name = crypto.find("p", class_="iworPT").text
        price = crypto.find("div", class_="cLgOOr").text

        # Fetch change from past day and past week
        # The change daily and weekly have the same classname, so I used a for statement
        changes = ""
        status = crypto.find_all("span", class_="sc-15yy2pl-0")
        for change in status:
            if(change.find("span", class_="icon-Caret-up")):
                changes += ("Up " + change.parent.text + "!")
            else:
                changes += ("Down " + change.parent.text + "!")
        # Split the data up for better formatting later
        changes = changes.split('!')
        
        # Fetch Market Cap
        market = crypto.find("span", class_="iosgXe").text

        # Print out the results
        print("%2s %-15s %-15s %-15s %-15s %-15s" % (rank, name, price, changes[0], changes[1], market))
        
        # Print up to the given rank value
        rank += 1
        if (rank > 10): break
else:
    print("found")

