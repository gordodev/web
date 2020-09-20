import webbrowser
import time

import urllib
#import urllib2
import re

from lxml import html
import requests


#This works to open tabs from sites in list
sites = ['http://google.com','http://cnn.com']
'''
webbrowser.open('http://crack.com')  # Go to example.com

for site in sites:
    webbrowser.open(site)
    time.sleep(2)
'''


#page = urllib.urlopen("http://cnn.com").read()

#page = urllib2.urlopen("http://cnn.com").read()
page = str(webbrowser.open('http://cnn.com'))

re.findall("dead",page)

print (page)

'''
>>> page = urllib.urlopen("http://google.com").read()

# => via regular expression

>>> re.findall("Shopping", page)
['Shopping']

# => via string.find, returns the position ...
>>> page.find("Shopping")

'''
