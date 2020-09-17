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


print ('Checking the following channels: \n',sites,'\n\n\n')

'''
#open sites in the sites list
for site in sites:
    print ('Site: ',site)
    webbrowser.open(site)  # Go to google.com
'''

keywords = ['deputies','police','ambush']

'''
for site, word in zip(sites, keywords):
    print (os.system('curl site | grep -oi move'))
    os.system('curl site | grep -oi move')
'''

for site, word in zip(sites, keywords):
    print ('Here is site/word: ',site,word)
    #subprocess.call(["curl", site, "|", "grep", "-oi", "move"])
    html_content = urlopen(site).read().decode('utf-8')
    
    matches = re.findall('peace', html_content);
    
    if len(matches) == 0:
        print ('I did not find anything')
    else:
        print ('My string is in the html')
