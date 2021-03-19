from bs4 import BeautifulSoup
import urllib.request
import time

url = 'https://www.blocket.se/annonser/hela_sverige/elektronik/datorer_tv_spel/datortillbehor_program?cg=5023&q=rtx%202060'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent,}

request = urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
page = response.read()
soup = BeautifulSoup(page,'html.parser')
tags = soup.find_all("div")


i = 0
for tag in tags:   
    if(tag.has_attr("to")):
        print(i, True)
    i = i+1