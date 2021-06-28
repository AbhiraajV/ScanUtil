import email
import requests
import webbrowser
import bs4
import pywhatkit as pwt
text_to_search="Hello"
#searcher= requests.get("https://www.google.com/search?q="+ text_to_search)
#searcher.raise_for_status()
#soup=bs4.BeautifulSoup(searcher.text ,"html.parser")
#querylink=soup.select('.r a')
#webbrowser.open("https://www.google.com" + querylink[0].get('href'))
#print(soup.prettify())
#print(querylink)
pwt.search("hello")
