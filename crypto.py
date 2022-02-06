#!/usr/bin/python3 
'''
Name: Victor Li
Date: 06/02/2022
Description: A simple script that gets the current prices of crypto using coinmarketcap.com
'''
from bs4 import BeautifulSoup
from colorama import Fore, Style
import requests
import sys

def cryptoList(total):
    ''' This function helps list the top cryptocurrencies
        @param total: How much crypto you wanna list'''

    # Print table captions
    print("%-5s %-15s %-15s %-15s %-16s %s" % ("#", "Name", "Price", "Daily Change", "Weekly Change", "Market Cap"))    

    # Get the HTML content
    page = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

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
                changes += (Fore.GREEN + "Up " + change.parent.text + Style.RESET_ALL + "!")
            else:
                changes += (Fore.RED + "Down " + change.parent.text + Style.RESET_ALL + "!")

        # Split the data up for better formatting later
        changes = changes.split('!')
        
        # Fetch Market Cap
        market = crypto.find("span", class_="iosgXe").text

        # Print out the results
        print("%-5s %-15s %-15s %-24s %-25s %s" % (rank, name, price, changes[0], changes[1], market))
        
        # Print up to the given rank value
        rank += 1
        if (rank > total): break

def cryptoFind(cryptos):
    '''This function searches through coinmarketcap to find list a specific cryptocurrency
        @param cryptos: A list containing each crypto the user wants to know about'''

    # Print table captions
    print("%-5s %-15s %-15s %-15s %-16s %s" % ("#", "Name", "Price", "Daily Change", "Market Cap", "Total Supply"))

    # Repeat for each parameter
    for name in cryptos:
        # Skip parameters was used to open the program (either CLI or by Python IDLE)
        if name == "python3" or name == "crypto.py" or name == "/usr/local/bin/crypto" or name == "./crypto": continue
        # Get the HTML content
        page = requests.get("https://coinmarketcap.com/currencies/" + name)
        # If cryptocurrency exist, print out the data
        if (page): 
            soup = BeautifulSoup(page.content, 'html.parser')
            crypto = soup.find("div", class_="top-summary-container")

            # Fetch rank and price
            rank = crypto.find("div", class_="namePillPrimary").text
            price = crypto.find("div", class_="priceValue").text

            # Fetch change from past day, call twice to get the specific class
            change = crypto.find("div", class_="priceTitle").find("span", class_="sc-15yy2pl-0")
            if(change.find("span", class_="icon-Caret-up")):
                changes = (Fore.GREEN + "Up " + change.text + Style.RESET_ALL)
            else:
                changes = (Fore.RED + "Down " + change.text + Style.RESET_ALL)

            # Fetch total supply
            supply = crypto.find("div", class_="inUVOz").text                

            # Fetch Market Cap
            market = crypto.find("div", class_="statsValue").text
            
            # Print out the results
            print("%-5s %-15s %-15s %-24s %-16s %s" % (rank[6:], name, price, changes, market, supply[:-3]))


        # Give error message if DNE
        else: print("%s is not listed on CMC or you mispelt!" % name)


# Prints out the top 10 cryptocurrencies by default if no argument is given
numArgs = len(sys.argv)
if (numArgs == 1): cryptoList(10)
else: cryptoFind(sys.argv)