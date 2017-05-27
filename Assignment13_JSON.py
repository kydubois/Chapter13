#! python3

''' The program will prompt for a URL,
read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)

Assignment #2, using JSON

Developed by Kyle DuBois, Version 1.0 '''

import urllib.request, urllib.parse, urllib.error
import json

numList = list()

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    print('Retrieving', address)
    
    # This section opens the URL and parses through JSON data
    url = urllib.request.urlopen(address)
    data = url.read().decode()
    headers = dict(url.getheaders())
    print('Retrieved', len(data),'characters')
    info = json.loads(data)

    #print(json.dumps(info, indent=4))
    
    # This section looks for and extracts the count numbers from the JSON data and creates a list
    for u in info["comments"]:
        #print(u['count'])
        numList.append(u['count'])

    # This section runs through the list and creates a new list of integers
    nunuList = list()
    for num in numList:
        newNum = int(num)
        nunuList.append(newNum)
        
    # This section sums all the integers and prints the total
    tot = sum(nunuList)
    print(tot)
    break
