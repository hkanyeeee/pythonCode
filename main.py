# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import urllib3
# import sys

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/news/<pager>')
def hello(pager):
    # # 转码
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    jiheWenzhangData = []
    jiheXinwenData = []
    viceWenzhangData = []
    doubanBookData = []
    doubanMovieData = []
    url1 = 'https://www.gcores.com/categories/1/originals?page=%s' % (pager)
    url2 = 'https://www.gcores.com/categories/2/originals?page=%s' % (pager)
    url3 = 'http://www.vice.cn/articles/page/%s' % (pager)
    url4 = 'https://movie.douban.com/review/best/?start=40'
    url5 = 'https://book.douban.com/review/best/?start=40'
    if int(pager) < 4:
        url4 = 'https://movie.douban.com/review/best/?start=%d' % ((int(pager) - 1)*20)
        url5 = 'https://book.douban.com/review/best/?start=%d' % ((int(pager) - 1)*20)
    a = requests.get(url1)
    b = requests.get(url2)
    c = requests.get(url3)
    d = requests.get(url4)
    e = requests.get(url5)

    # 处理机核Data
    def getmakeJiheList(html, data):
        soup = BeautifulSoup(html, "html.parser")
        divData = soup.find_all(class_ = 'showcase_text')
        print(type(divData))
        for oneData in divData:
            if len(oneData.select('a')) > 0:
                data.append({
                    'articalName': oneData.select('a')[0].string.strip('\n'),
                    'articalHref': oneData.select('a')[0]['href']
                })
        return data

    # 处理Vice Data
    def getmakeViceList(html, data):
        soup = BeautifulSoup(html, "html.parser")
        divData = soup.find_all(class_ = 'entry-title')
        print(type(divData))
        for oneData in divData:
            if len(oneData.select('a')) > 0:
                data.append({
                    'articalName': oneData.select('a')[0].string.strip('\n'),
                    'articalHref': oneData.select('a')[0]['href']
                })
        return data

    # 处理豆瓣 Data
    def getmakeDoubanList(html, data):
        soup = BeautifulSoup(html, "html.parser")
        divData = soup.find_all(class_ = 'main-bd')
        for oneData in divData:
            if len(oneData.select('h2')[0]) > 0:
                if len(oneData.select('h2')[0].select('a')[0]) > 0:
                    data.append({
                        'articalName': oneData.select('h2')[0].select('a')[0].string,
                        'articalHref': oneData.select('h2')[0].select('a')[0]['href']
                    })
        return data

    return jsonify({
        'jiheWenzhang': getmakeJiheList(a.text, jiheWenzhangData),
        'jiheXinwen': getmakeJiheList(b.text, jiheXinwenData),
        'viceWenzhang': getmakeViceList(c.text, viceWenzhangData),
        'doubanMovieData': getmakeDoubanList(d.text, doubanMovieData),
        'doubanBook': getmakeDoubanList(e.text, doubanBookData),
        })



if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port = 8080)