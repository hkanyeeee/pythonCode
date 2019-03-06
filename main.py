# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
from flask import make_response
import requests
from bs4 import BeautifulSoup
import sys

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def hello():
    # 转码
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # 机核
    jiheWenzhangData = []
    jiheXinwenData = []
    viceWenzhangData = []
    doubanBookData = []
    doubanMovieData = []
    a = requests.get('https://www.gcores.com/categories/1/originals')
    b = requests.get('https://www.gcores.com/categories/2/originals')
    c = requests.get('http://www.vice.cn/articles/page/1')
    d = requests.get('https://movie.douban.com/review/best/')
    e = requests.get('https://book.douban.com/review/best/')
    # 处理机核Data
    def getmakeJiheList(html, data):
        soup = BeautifulSoup(html, "html.parser")
        divData = soup.find_all(class_ = 'showcase_text')
        for oneData in divData:
            data.append({
                'articalName': oneData.select('a')[0].string.strip('\n'),
                'articalHref': oneData.select('a')[0]['href']
            })
        return data

    # 处理Vice Data
    def getmakeViceList(html, data):
        soup = BeautifulSoup(html, "html.parser")
        divData = soup.find_all(class_ = 'entry-title')
        for oneData in divData:
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
    app.run(host = '0.0.0.0' ,port = 8080, debug = 'True')