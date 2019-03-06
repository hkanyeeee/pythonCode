# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import sys


# 转码
reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get("https://movie.douban.com/review/best/")
demo = r.text
for oneData in divData:
    print((oneData.select('h2')[0].select('a')[0].string))
    break
# fo = open("output.html", "w")
# # print (type("www.runoob.com!\nVery good site!\n"))
# # print (type(soup))
# fo.write(demo)
# fo.close()

soup = BeautifulSoup(demo, "html.parser")
divData = soup.find_all(class_ = 'main-bd')
# print(type(divData[0]))
for oneData in divData:
    print((oneData.select('h2').children[0]['href']))
    print((oneData.select('a')[0].string))
    break