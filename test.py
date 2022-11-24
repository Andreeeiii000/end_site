import requests
from bs4 import BeautifulSoup

cities = [
    'Odesa','Dnipro','Donetsk'
]
for city in cities:
    url = 'https://en.wikipedia.org/wiki/'+city

    request =requests.get(url)

    soup = BeautifulSoup(request.text,'lxml')
    # print(dir(request))
    # print(request.text)
    city_name =  soup.find('span').text 

    dd = soup.find('div', id='mw-content-text')

    dd2 = dd.find("div", class_="mw-parser-output")

    out = dd2.find("table", class_="infobox ib-settlement vcard")

    out2 = out.find_all("td", class_="infobox-data")


    population = out2[9].text
    print(city_name,population)