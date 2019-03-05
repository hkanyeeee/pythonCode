import requests
from bs4 import BeautifulSoup
r = requests.get("https://s.taobao.com/search?q=手机")
demo = r.text
# soup = BeautifulSoup(demo , "html.parser")
fo = open("output.html", "w")
# print (type("www.runoob.com!\nVery good site!\n"))
# print (type(soup))
fo.write(demo)
fo.close()