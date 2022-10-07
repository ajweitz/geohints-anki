#!/bin/python3

from subprocess import call
import urllib.request
import time
import os.path

rc = call("./scrap_page.sh")

f = open("bollards_temp3.txt", "r")
bollards = f.read()  # read content of file into str
f.close()  # close file

bollard_list = bollards.split('\n')

i = 0
next_i = 0
countries = {}
country = None
while i < len(bollard_list):
    if bollard_list[i].startswith("Sources"):
        if not bollard_list[i+1].startswith("Sources"):
            country = bollard_list[i+1].strip() 
        countries[bollard_list[i]] = country
    i += 1

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)'),
    ('Accept-Language','en-us')
    ]
urllib.request.install_opener(opener)

for key, value in countries.items():
    filename = f"bollards/{value}"
    i = 2
    while os.path.isfile(filename):
        filename = f"{filename}_{i}"
        i += 1
    filename = f"{filename}.jpg"
    urllib.request.urlretrieve(f"https://geohints.com/{key}",filename)
    time.sleep(0.2)