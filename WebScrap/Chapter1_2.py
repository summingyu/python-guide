#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsOjb = BeautifulSoup(html.read(), "html5lib")
        title = bsOjb.findAll("a", {"class": "link"})
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.33e9.com/33.html")
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    for name in title:
        print(name)
