#! python3

'''This program will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)

Python for Everyone, Ch. 13, Assignment #1

Version 2.0, Developed by Kyle DuBois.'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

numList = list()

while True:
    address = input('Enter location: ')

    print('Retrieving', address)

    url = urllib.request.urlopen(address)
    data = url.read()
    print('Retrieved',len(data),'characters')

    # this section parses through an XML tree to find user comment counts
    tree = ET.fromstring(data)
    counts = tree.findall('comments/comment')
    print('User count:', len(counts))

    # this section creates a list of XML.elements
    for item in counts:
        count = item.find('count').text
        numList.append(count)

    # this section runs the the XML.elem list and creates a new list of integers
    nunuList = list()
    for num in numList:
        #converst into integer
        newNum = int(num)
        nunuList.append(newNum)

    tot = sum(nunuList)
    print(tot)
    break
