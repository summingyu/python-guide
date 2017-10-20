#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup


def getbsObj(Url):
    try:
        html = urlopen(Url)
    except Exception as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html5lib")
    except Exception as e:
        print(e)
        return None
    return bsObj


bsObj = getbsObj("http://oop.iems.net.cn/task.jsp")
H_tr = bsObj.findAll("tr")
H_th = bsObj.findAll("th")
for i in range(len(H_th) - 1):
    if i == 0:
        print(H_th[i].find("a").get_text(), ":", H_th[i].find("a").attrs['href'])
    print(H_th[i + 1].get_text(), ":", H_tr[2].findAll("td")[i].get_text())
