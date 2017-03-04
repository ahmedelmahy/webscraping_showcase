import requests
from bs4 import BeautifulSoup

  

#print(requests.post("http://www.med.alexu.edu.eg/resultsdata/national/2015-2016/5thyear/secondterm/search2.php", 
#                   data={'user':13}).text)
#lnk="http://www.med.alexu.edu.eg/resultsdata/national/2015-2016/4thyear/secondterm/search8_2.php"
#lnk="http://www.med.alexu.edu.eg/resultsdata/national/2015-2016/5thyear/secondterm/search2.php"
lnk='http://www.med.alexu.edu.eg/resultsdata/national/2014-2015/5thyear/secondterm/search8.php'
l=[]
j=0

while j < 1400 :
    j= j + 1
    html=requests.post(lnk, data={'user':j}).text
    parsed_html = BeautifulSoup(html)
    m=[]
    for i in parsed_html.find_all("td"):
        m.append(i.text)
    try:
        dict={j:m[m.index('الاجمالى العام \t ')+1]}
        l.append(dict)
        print(j,'yes') 
    except:
        print(j,'no')
        
import io
import json

with io.open("scrapedresultsmarks.json",'w',encoding="utf-8") as outfile:
  outfile.write(json.dumps(l))