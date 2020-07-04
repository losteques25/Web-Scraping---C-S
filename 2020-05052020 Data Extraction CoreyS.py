from bs4 import BeautifulSoup
import requests
source=requests.get("http://www.coreyms.com").text
soup=BeautifulSoup(source,"lxml")
for article in soup.find_all("div",class_="article"):
    headline=article.a.text
    print(headline)
    summary=article.p.text
    print(summary)
    
    
    

