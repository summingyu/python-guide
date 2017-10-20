#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    Links = bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")"))
    print(includeUrl + "内链的links为:")
    print(Links)
    # 找出所有以"/"开头的链接
    for link in Links:
        if link.attrs['href'] is not None:
            if(link.attrs['href']) not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    print(internalLinks)
    return internalLinks


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if(link.attrs['href']) not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
    except (HTTPError, URLError) as e:
        print("The error is : ", e)
        return None
    bsObj = BeautifulSoup(html, "html5lib")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        if len(internalLinks) == 0:
            print("No internal links, looking around the site for one!")
            return None
        else:
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    if externalLink is not None:
        print("Random external link is: " + externalLink)
        followExternalOnly(externalLink)
    else:
        print(startingSite + " has no links!")


followExternalOnly("http://www.33e9.com/404.html")
