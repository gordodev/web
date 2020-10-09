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

def checkcache(string):
    string = ["carlyle"]
    #command = "grep -c "+str(text)[1:-1]+" ~/dev/github/web/debate/tmp/*" #Check cache for string
    command = "echo \"Channels with keywords: `grep -ci "+str(text)[1:-1]+" ~/dev/github/web/debate/tmp/* | grep -v \":0\" | grep -c :`\"" #Check cache for string
    #str(test_list)[1:-1]
    print (command)
    os.system(command)

    #os.system('grep -l taxes ~/dev/github/web/debate/tmp/*')

#checkcache(text)

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

#saystuff = str(text)
saystuff = str(text)
say(saystuff)

checkcache(text)

say('Searching')
print (text)

sitenum = 0                     #Used to track cache file numbers and/or site number
#sitenem = str(sitenum)
#                          GO TO EACH SITE and parse HTML
for site in sites:
    f = open("./tmp/page"+str(sitenum),"w+")   #open/create cache file
    url = site
    html = urlopen(url).read()                 #open url and insert into variable html
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, features="html.parser")
    f.write( str(soup)+'\n' )                  #Insert page into cache file
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
            #playsound('beep41.mp3')
            #sitesMatched = sitesMatched.insert(0,site)   #Add site to sites matched list to open later
            sitesMatched.insert(0,site)   #Add site to sites matched list to open later
            
            for i in site: 
                if i in sitesMatched: 
                    print ("Element Exists")
                    if foundsite == 0:
                        print ('Site has not been added yet: ',site)
                        sitesMatched.insert(0,site)   #Add site to sites matched list to open later
                        foundsite += 1
                    else:
                        foundsite += 1
                        print ('not found')
            
            print ('             TOTAL: ',words,'=',amount,'\n')

        #else:
            #playsound('qbeep.mp3')
        #time.sleep(0.01)
    sitenum += 1

say('search complete')
sayStuff = "I found "+str(len(sitesMatched))+"hits"
say(sayStuff)

print ('HITS: ',len(sitesMatched)) #Display total matches


#print (len(sitesMatched))   #QA checking url list length

if len(sitesMatched) > 0:
    say('Openning pages now')
    for page in sitesMatched:
        webbrowser.open(page)  #open browser
        #print ('Site: ',siteLine)
    playsound('beep43.mp3'); say('All pages opened')
else:
    print ('Not found')
    sayStuff = "Oh my. I\'m so sorry. Nobody cares about "+words
    say(sayStuff)

say('I\'m done. I\'ll be here if you need me. Shutting down for now.')

