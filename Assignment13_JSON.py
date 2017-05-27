#! python3

''' The program will prompt for a URL,
read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)

Python for Everyone, Ch. 13, Assignment #2, using JSON

Developed by Kyle DuBois, Version 1.0 '''

import urllib.request, urllib.parse, urllib.error
import json

numList = list()

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    print('Retrieving', address)
    url = urllib.request.urlopen(address)
    data = url.read().decode()
    headers = dict(url.getheaders())
    print('Retrieved', len(data),'characters')
    # this section parses through an JSON to find user comment counts
    info = json.loads(data)

    #print(json.dumps(info, indent=4))
    # this section extracts the counts numbers for JSON and creates a list
    for u in info["comments"]:
        #print(u['count'])
        numList.append(u['count'])

    # this section runs the the list and creates a new list of integers
    nunuList = list()
    for num in numList:
        # This seciions converst into integer
        newNum = int(num)
        nunuList.append(newNum)
    # This section sums all the numbers
    tot = sum(nunuList)
    print(tot)
    break
