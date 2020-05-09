
import bs4
import requests
import webbrowser

import ItemsList
from urllib.error import HTTPError

def getPrice(url):
    res = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.content, "lxml")
    elem = soup.select('#prcIsum')
    return elem[0].text.strip()

itemsList = ItemsList.ItemsList()
itemsList.load()
enterLoop = True
check = True
urlCheck = True

while (enterLoop):
    itemsList.printkeys()
    newOrExisting = input("Type the item name that you would like to search: ")
    while (urlCheck):
        userInput = input("What is the link to your item? (enter everything that appears after the .ca/) ")
        baseUrl = "https://www.ebay.ca/"
        completeUrl = baseUrl + userInput
        try:
            price = getPrice(completeUrl)
            urlCheck = False;
        except Exception as e:
            print ("That's not a valid URL, try again. ")
              
    newprice= price.lstrip("CND$ ")
    itemsList.addItem(newOrExisting, newprice)
    while (check):
        runAgain = input("Would you like to look up another item (Type Yes or No): ")
        if runAgain.casefold() == "yes":
            enterLoop = True
            check = False
        elif runAgain.casefold() == "no":
            enterLoop = False
            check = False
            itemsList.save()
            itemsList.saveToXl()
        else:
            print ("That's not a valid option, try again. ")
            
            
            
