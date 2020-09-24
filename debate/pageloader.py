#!/usr/bin/env python3

#2nd attempt at script
#This works but does not seem to have all the text
#This will typically go back up to a month depending on how many videos are posted. Videos are only the ones that load initially until you scroll down

import re
import requests
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')
    signal.pause()


sitesMatched = []

#Read the websites file
with open('sites.txt') as f:
    sites = f.readlines()


#SAMPLE KEYWORDS for reference only!!
#text = ['trump','riots','leftist','anarchist jurisdictions','whistleblower','the trump','the the three','the sjd fef four']
#text = ['160 million']

#                          GET KEYWORDS FROM USER
text = input('Enter keywords: \n').split(" ")
print (text)

#                          GO TO EACH SITE and parse HTML
for site in sites:
    url = site
    html = urlopen(url).read()
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, features="html.parser")
    #soup = BeautifulSoup("<a aria-label>",'lxml')
    
    print(site)    
    for words in text:

        # get text
        #text = soup.get_text()
        #soup.find_all('a')
        pagetext = soup.text
        #text = soup.a
        #soup.body.b

        foundsite = 0
        m = re.findall(words, pagetext, re.IGNORECASE)    #Check for string
        amount = len(m); #print (amount)
        if m:                                             #if string found then...
            site = site.rstrip("\n")
            print ('Found string')
            #sitesMatched = sitesMatched.insert(0,site)   #Add site to sites matched list to open later
            sitesMatched.insert(0,site)   #Add site to sites matched list to open later
            
            for i in site: 
                if i == sitesMatched: 
                    print ("Element Exists")
                    if foundsite == 0:
                        print ('Site has not been added yet: ',site)
                        sitesMatched.insert(0,site)   #Add site to sites matched list to open later
                        foundsite += 1
                    else:
                        foundsite += 1
            
            print ('             TOTAL: ',words,'=',amount,'\n')
        #time.sleep(0.001)
        #print ('text: ',text)

        #print(text)
        time.sleep(0.01)

print ('HITS: ',len(sitesMatched)) #Display total matches

if len(sitesMatched):
    for page in sitesMatched:
        webbrowser.open(page)  # Go to google.com
        #siteLine = site
        #print ('Site: ',siteLine)
else:
    print ('Not found')
