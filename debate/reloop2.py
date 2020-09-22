#!/usr/bin/env python3

#2nd attempt at script
#This works but does not seem to have all the text

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


# Loop.
#sites = ['google.com','yahoo.com']
text = ['riot','violence','judge']


#print ('page: ',pagetxt,'\n')

for site in sites:
    print ('\nGoing to: ',site)

    url = site
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    '''  
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    '''
    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)


'''
    for element in text:
        # Match if 2 words starting with letter "d."
        print ('\nCheck site for: ',element,'\n')
        m = re.findall(element, pagetxt)

        # See if success.
        if m:
            print(m)
    time.sleep(1)

#X = ','.join( str(a) for a in [1,2,3] )
'''
