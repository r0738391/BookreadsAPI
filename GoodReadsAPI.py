#Hello, this code will return a list of authors, books, ratings and publication dates based on input from the user.
#Don't forget to enter your own bookreads api key as "key" under the "Variable" section.

#Imports
import requests
import http.client
import urllib.parse
import xml.etree.ElementTree as ElementTree
from tabulate import tabulate

#Variable (Change Key To Your API Key)
key = ""
userInput = ""
url = ""
titleList = []
nameList = []
ratingList = []
yearList = []

#Ask User For User Input
print("Book to search for: ", end="" )
userInput = input()

#Create Authenticated Connection, Get Data
url = ("https://www.goodreads.com/search.xml?key=" + key + "&q=" + urllib.parse.quote(userInput))
response = requests.get(url)
root = ElementTree.fromstring(response.content)

#Create List Of Titles
for title in root.findall('.//best_book/title'):
    titleList.append(title.text)

#Create List of Authors
for name in root.findall('.//author/name'):
    nameList.append(name.text)

#Create List of Ratings
for rating in root.findall('.//work/average_rating'):
    ratingList.append(rating.text)

#Create List of Years
for year in root.findall('.//work/original_publication_year'): 
    yearList.append(year.text)


#Create Table of Authores and Titles Sorted By Author
table = sorted((list(zip(nameList, titleList, ratingList, yearList))))

#Check For Results
if len(table) == 0:
    #Tell User If None Found
    print("Sorry, but I couldn\'t find any books by \"" + userInput + "\"")
else:
    #Print Pretty Table
    print(tabulate(table, headers=["Author", "Title", "Rating 1-5", "Publication year"], tablefmt="rst"))