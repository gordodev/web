#!/usr/bin/env python3

#2nd attempt at script
#This works but does not seem to have all the text
#This will typically go back up to a month depending on how many videos are posted. Videos are only the ones that load initially until you scroll down

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
    #sites[-1] = sites[-1].strip()
    #sites = f.readlines


# Loop.
#sites = ['google.com','yahoo.com']
#text = ['riot','violence','judge','leftist','antifa','black bloc','racist','portland']
#text = ['rochester']

text = ['trump','riots','leftist','anarchist jurisdictions','whistleblower','the trump','the the three','the sjd fef four']


#print ('page: ',pagetxt,'\n')

for site in sites:
    #print ('\n',site)

    url = site
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    #soup = BeautifulSoup("<a aria-label>",'lxml')
    '''  
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    '''
    print(site)    
    for words in text:

        # get text
        #text = soup.get_text()
        #soup.find_all('a')
        pagetext = soup.text
        #text = soup.a
        #soup.body.b

        m = re.findall(words, pagetext, re.IGNORECASE)
        amount = len(m); #print (amount)
        if m:
            site = site.rstrip("\n")
            #print (site,'   <========    ',words)
            print ('             TOTAL: ',words,'=',amount,'\n')
        #time.sleep(0.001)
        #print ('text: ',text)

        '''
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        '''
        #print(text)
        time.sleep(0.01)


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
