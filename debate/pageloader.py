#!/usr/bin/env python3

#2nd attempt at script
#This works but does not seem to have all the text
#This will typically go back up to a month depending on how many videos are posted. Videos are only the ones that load initially until you scroll down

import re
import time
import os
import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

from playsound import playsound
from gtts import gTTS 

def say(text):
    '''
    Say text
    '''
    message = text
    language = 'en'
    speech = gTTS(text = message, lang = language, slow = False)
    speech.save('text.mp3')
    playsound('text.mp3')


# Play the wav file
playsound('beep41.mp3')



sitesMatched = []

#Read the websites file
with open('sites.txt') as f:
    sites = f.readlines()


#SAMPLE KEYWORDS for reference only!!
#text = ['trump','riots','leftist','anarchist jurisdictions','whistleblower','the trump','the the three','the sjd fef four']
#text = ['160 million']

#                          GET KEYWORDS FROM USER
say('Enter Keywords')
text = input('Enter keywords: \n').split(",")
say('Searching')
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
        pagetext = soup.text

        foundsite = 0
        #say('Searching for string')
        m = re.findall(words, pagetext, re.IGNORECASE)    #Check for string
        
        amount = len(m); #print (amount)
        if m:                                             #if string found then...
            site = site.rstrip("\n")
            playsound('beep41.mp3')
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

        #time.sleep(0.01)

say('search complete')
print ('HITS: ',len(sitesMatched)) #Display total matches


print (len(sitesMatched))   #QA checking url list length

if len(sitesMatched) > 0:
    for page in sitesMatched:
        say('Openning pages now')
        webbrowser.open(page)  #open browser
        say('All pages opened')
        #print ('Site: ',siteLine)
else:
    print ('Not found')
    sayStuff = "Oh my. I\'m so sorry. Nobody cares about "+words
    say(sayStuff)

playsound('beep43.mp3')
say('I\'m done. I\'ll be here if you need me. Shutting down for now.')

