#! python3

'''This program will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)

Python for Everyone, Ch. 13, Assignment #1

Version 1.0, Developed by Kyle DuBois.'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

numList = list()

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    print('Retrieving', address)

    url = urllib.request.urlopen(address)
    #print('Retrieving', url)
    #uh = urllib.urlopen(url)
    data = url.read()
    print('Retrieved',len(data),'characters')
    #print(data)
    tree = ET.fromstring(data)


    counts = tree.findall('.//count')
    print('User count:', len(counts))

    for count in counts:
        #print('Name:', item.find('name').text)
        print('Count:', count.find('count').text)
