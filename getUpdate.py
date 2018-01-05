from outPut import *

import requests
import re

### To get links in one certain page, use this for interpreting to picture links in "outPut.py"

def getLinks(nyaa_url,mode="Typical Mode"):
    tempList = []
    r = requests.get(nyaa_url)
    array = r.text.split("\n")
    array = re.split("http://|https://|&#10;|\)| |<",array[293])
    address = [item for item in filter(lambda x:x != "",array)] ### Delete the empty string here
    
    for i in address:
        if(mode=="Complete Mode"):
            if(i.find("htm")!=-1 | i.find("jpg")!=-1):
                tempList.append(i)
        else:
            if(i.find("htm")!=-1):
                tempList.append(i)
    for i in tempList:
        print(i+"~")
    return(tempList)
            
        
linkList = getLinks("https://sukebei.nyaa.si/view/2416768","Clean Mode")
while(True):
    if(len(linkList)==0):
        break
    print(linkList[-1]+"at getUpdate Line 29")
    outPut(linkList.pop())