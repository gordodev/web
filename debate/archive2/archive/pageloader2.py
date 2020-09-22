import webbrowser
import os
import time
import subprocess
import re

#import urllib.request.urlopen

from urllib.request import urlopen

sitesFile = []

#Read the websites file
with open('sites.txt') as f:
    sites = f.readlines()

#Format sites and insert into list
sites = [x.strip() for x in sites]

keywordsin = str(input('What are you looking for?').split(" "))

#keywords = ' '.join([str(elem) for elem in keywordsin])

keywords = keywordsin

print ('keywordsin is: ',keywordsin,'...and keywords is: ',keywords)

#keywords = str(keywordsin)
#thing = "string"

print ('Checking the following channels: \n',sites,'\n\n\n')

'''
#open sites in the sites list
for site in sites:
    print ('Site: ',site)
    webbrowser.open(site)  # Go to google.com
'''

#keywords = ['deputies','police','ambush','deputies','police','ambush','deputies','police','ambush','police','ambush','deputies','police','ambush','deputies','police','ambush']

'''
for site, word in zip(sites, keywords):
    print (os.system('curl site | grep -oi move'))
    os.system('curl site | grep -oi move')
'''

for site in sites:
    print ('Here is site/word: ',site,keywords)
    #subprocess.call(["curl", site, "|", "grep", "-oi", "move"])
    html_content = urlopen(site).read().decode('utf-8')
    
    #print ('looking for',keywords,'in site: ',site)
    for word in keywords:
        #print ('looking for',word,'in site: ',site,'\n\n')
        myword = str(word)
        print ('looking for',word,'in site: ',site,'\n\n')
        matches = re.match(str(myword), html_content)
    
    if len(matches) == 0:
        print ('I did not find anything')
    else:
        print ('My string is in the html')
