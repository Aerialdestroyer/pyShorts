from bs4 import BeautifulSoup
import urllib.request
import time

url = 'https://inet.se/produkt/5411920/msi-geforce-rtx-3060-ti-8gb-ventus-2x-oc'
#url = 'https://www.inet.se/produkt/6301289/inet-tryckluft-pa-burk-400ml'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent,}

while True:
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    page = response.read()
    soup = BeautifulSoup(page,'html.parser')
    tags = soup.find_all(class_="qty-string")

    try:
        num = int(tags[0].string[:2]) + int(tags[3].string[:2])
    except:
        num = -1

    if(num > 0):
        if(int(tags[0].string[:2]) > 0):
            print('In stock! At "' + soup.find_all('h4')[0].string + '"')
        if(int(tags[3].string[:2]) > 0):
            print('In stock! At "' + soup.find_all('h4')[1].string + ': ' + tags[3].parent.parent.find('a').string + '"')
        break
    else:
        print("Out of stock")
    time.sleep(60*5)