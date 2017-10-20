#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
from urllib.request import urlopen


def getCountry(ipAdress):
    response = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=" + ipAdress).read().decode("utf-8")
    responseJson = json.loads(response)
    print(responseJson.get("code"))
    return responseJson.get("data")
    # return responseJson


print(getCountry("103.239.206.53"))
