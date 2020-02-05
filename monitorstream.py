# monitor Muddys music stream
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def print_song_title():
    # api endpoint
    URL = "http://muddys.digistream.info:20398/7.html"

    r = requests.get(url = URL, params = '')

    soup = BeautifulSoup(r.text, 'html5lib')

    # could be commas in the title, check and re-assemble
    n = 6
    title = ""
    bodylist = soup.body.string.split(',')
    while n < len(bodylist):
        title = title + bodylist[n]
        n = n + 1
        if n < len(bodylist):
            title = title + ","

    
    return(title)


song_title = ""
song_number = 0

while True:
    check_title = print_song_title()
    
    if song_title != check_title:
        song_number = song_number + 1
        song_title = check_title
        timestamp = datetime.now()
        timestring = timestamp.strftime("%b-%d-%Y (%H:%M:%S)")
        print(timestring, song_title)
        
    time.sleep(10)



#<html><body>69,1,148,500,66,128,David Bowie, Mick Jagger - Dancing in the Street</body></html>

