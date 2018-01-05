''' requests for open Imghost, ImgTaxi
    urllib for save file, os for open file on PC automatically. 
'''
import requests
import urllib
import os
''' urllib.request for 
    re for matching the strings to be used
'''
import urllib.request
import re

####################################(Chinese Edition: 666666)

### Headers Preparation


''' Check Whether the URL is nice enough for 
'''
def correctURL(url):
    if (url.find("http")==-1):
        url = "http://"+url
    return (url)

''' Get the image url from the Hyperlink given in the Nyaa
'''

''' ImgHost, ImgTaxi, ImgDrive, ImageTeam are allowed in this function
'''
def getImgHost(url):
    r = requests.get(url)
    smallUrl = ""
    
    if(r.text.find("jpg\"")!=-1):
        smallUrl=(r.text[r.text.find("http",r.text.find("jpg\"")-80):r.text.find("jpg\"")+3])
    elif(r.text.find("jpeg")!=-1):
        smallUrl=(r.text[r.text.find("http",r.text.find("jpeg\"")-80):r.text.find("jpeg\"")+4])
    elif(r.text.find("jpg\'")!=-1):
        smallUrl=(r.text[r.text.find("http",r.text.find("jpg\'")-80):r.text.find("jpg\'")+3])
    print("Access Succeed")    
    url = smallUrl.replace("small","big")
    
    return (smallUrl)

    
''' ImgHost, ImgTaxi, ImgDrive, ImageTeam are allowed in this function

def getImgTaxi(url):
    r = requests.get(url)
    if(r.text.find("jpg\"")!=-1):
        smallUrl =  r.text[r.text.find("http",r.text.find("jpg\"")-80):r.text.find("jpg\"")+3]
    elif(r.text.find("jpeg")!=-1):
        smallUrl =  r.text[r.text.find("http",r.text.find("jpeg\"")-80):r.text.find("jpeg\"")+4]    
    elif(r.text.find("jpg\'")!=-1):
        smallUrl =  r.text[r.text.find("http",r.text.find("jpg\'")-80):r.text.find("jpg\'")+3]

    url = smallUrl.replace("small","big")
    return url
'''

def getImgPart(url):
    urlId = re.match(r".*-(.*).html.*",url)
    url = "http://imgpart.com/dlimg.php?id="+urlId.group(1)
    r=urllib.request.Request(url)
    r.add_header("Host", "imgpart.com")
    r.add_header("Connection", "keep-alive")
    r.add_header("Upgrade-Insecure-Requests", "1")
    r.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
    r.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    r.add_header("DNT", "1")
    r.add_header("Accept-Encoding", "gzip, deflate, sdch")
    r.add_header("Accept-Language", "zh-CN,zh;q=0.8")
    ### r.add_header("Cookie", "__cfduid=d20456b2d0f3e361c2cce**********************; PHPSESSID=di87**********************")
    response = urllib.request.urlopen(r)
    
    filename = re.match(r".*; (.*)",response.info()["Content-Disposition"])
    return(url+"&"+filename.group(1))
    

''' Special: Because I cannot find the redirect reason for Pixense. 
'''
def getPix(Digital,mode="Cover"):
    if(mode == "Cover"):
        r = ("http://www.fortstore.net/themes/latest/uploads4/pixsense/big/1314/"+Digital+".jpg")
    if(mode == "Content"):
        r = ("http://www.fortstore.net/themes/latest/uploads3/pixsense/big/1314/"+Digital+"_s.jpg")
    return(r)
    
def outPut(url):
    '''
    cmd = input("Welcome to the Nyaa.si Decoding Picture Assistant\n\
    Press 1 for ImgHost, ImgTaxi, or ImgDrive, ImageTeam; \n\
    Press 2 for ImgPart;\nPress 0 to quit. ")
    
    if(cmd=="0"):
        break
    url = input("The url?")
    '''
    url = correctURL(url)
    
    print(url)
    if ("imghost" in url.lower() or "imgtaxi" in url.lower() or "imgdrive" in url.lower() or "imgteam" in url.lower()):
        url = getImgHost(url)
    elif("imgpart" in url.lower()):
        url = getImgPart(url)
    elif(cmd=="3"):
        url = getPix(Dital,"Cover")
    
    print(url)
    url = correctURL(url)
    filename = url[-10:]
    ###Force to use HTTP instead of HTTPS (For Net Speed), in sacrifice of Security
    picture = requests.get(url)
    ###.replace("http","http"))
    
    '''if(picture.status_code==404):
        print("404 Access Error. Please Check whether you are in China. ")
        continue
    '''    
    with open(filename+".jpg","wb") as f:
        f.write(picture.content)
    picture.close()
    ###urllib.request.urlretrieve(url,"./JpgDown/"+filename)
    ###os.system(filename+".jpg")
