import webbrowser
import os

sites = []
'''
with open('sites.txt') as f:
        #sites = str(f.read())
        sites.append(f.read())
'''

#print ('sites has: ',sites,' END')

sites = ['http://google.com','http://youtube.com']

'''
for site in sites:
    os.system("start \"\" ")+str(site)
'''


for site in sites:
    webbrowser.open(site)  # Go to google.com
    print ('Site: ',site)

