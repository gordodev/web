#!/usr/bin/env python3

#2nd attempt at script

import re
import requests
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup


# Sample strings.
list = ["dog dot", "data day", "no match"]


#Read the websites file
with open('sites.txt') as f:
    sites = f.readlines()

'''
# Loop.
for element in list:
    # Match if 2 words starting with letter "d."
    m = re.match("(d\w+)\W(d\w+)", element)

    # See if success.
    if m:
        print(m.groups())
'''

# Loop.
#sites = ['google.com','yahoo.com']
text = ['riot','violence','judge']


URL = 'http://cnn.com'
page = requests.get(URL)
pagetxt = page.text
#print ('page: ',pagetxt,'\n')

for site in sites:
    print ('\nGoing to: ',site)
    for element in text:
        # Match if 2 words starting with letter "d."
        print ('\nCheck site for: ',element,'\n')
        m = re.findall(element, pagetxt)

        # See if success.
        if m:
            print(m)
    time.sleep(1)

#X = ','.join( str(a) for a in [1,2,3] )
