import webbrowser
import os
import time

sitesFile = []
#sites = []

with open('sites.txt') as f:
    sites = f.readlines()

sites = [x.strip() for x in sites]


print ('Checking the following channels: \n',sites)


for site in sites:
    webbrowser.open(site)  # Go to google.com
    print ('Site: ',site)
