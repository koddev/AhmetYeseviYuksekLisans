
# %%
import requests as req
from bs4 import BeautifulSoup
from ililce import sehirler

class Local():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://www.sondakika.com/"

    def __init__(self, city: str):
        url = self.url
        header = self.header
        self.city = city.lower().replace("şçğüöı", "scguoi")
        g = req.get(url+self.city, headers=header).text
        self.soup = BeautifulSoup(g, "html.parser")
    
    def current_news(self):
        news = {
            "city": self.city,
            "title": self.soup.find("a", {"class": "content"}).span.text,
            "about": self.soup.find("p", {"class": "news-detail news-column"}).text
        }
        return news
   
    def news(self, limit: int=10):
        news = {}
        n = 1
        for i in self.soup.find_all("li", {"class": "nws"}):
            if n <= limit:
                news[n] = {
                    "tarih": i.find("span", {"class": "mdate"}).text.strip(),
                    "city": self.city,
                    "city2": "",
                    "title": i.find("a", {"class": "content"}).span.text,
                    "content": i.find("p", {"class": "news-detail news-column"}).text
                    
                }
            n+=1
        return news
    
 
# %%    
city = "Afsin"
local = Local(city)
newss=local.news(limit=10000)
data = []
data.extend(list(newss.values()))
for key in newss:
    newss[key]['city2'] = "kahramanmaras"
print(data)
# %%
 
 
 
 
# %%
data = []
 
for il, ilçeler in sehirler.items():
    print(f"{il} ili ilçeleri:")
    for ilçe in ilçeler:
        # print(f"  - {ilçe}")
        city = ilçe
        local = Local(city)
        newss = local.news(limit=10000)
        for key in newss:
            newss[key]['city2'] = il
        data.extend(list(newss.values()))

 
tekrarsiz_dizi = []
basliklar=[]
for eleman in data:
    
    if eleman["title"] not in basliklar:
        tekrarsiz_dizi.append(eleman)
        basliklar.append(eleman["title"])

data=tekrarsiz_dizi

import csv
with open("haberlocal.csv", mode="w", newline="", encoding="utf-8") as dosya:
    yazici = csv.DictWriter(dosya, fieldnames=data[0].keys())
    
    # Başlıkları yaz (sütun isimleri)
    yazici.writeheader()
    
    # Her bir sözlüğü satır olarak yaz
    yazici.writerows(data)