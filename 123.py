#!/usr/bin/python
# _*_ coding: utf-8 _*_

import requests

msg = {}
new_url = '192.168.1.30'

dict_list = {
    "ums": "/ums/s/ping/get",
    "eas": "/ums/s/ping/get",
    "ocs": "/ums/s/ping/get",
    "mnc": "/ums/s/ping/get",
}

# 192.168.1.30/ums/s/ping/get
# 192.168.1.30/ums/s/ping/get
# 192.168.1.30/ums/s/ping/get
# 192.168.1.30/ums/s/ping/get


def parse_url(abc_url): #https://httpbin.org/get
    msg = requests.get(abc_url).json().get("msg")
    code = requests.get(abc_url).json().get("code")
    return msg, code


for k, v in dict_list.items():
    url = "%s%s" % (new_url, v)
    msg, code = parse_url(url)
    if msg == "abc" and code == "200":
        print("OK")
    else:
        print("not ok")
        msg[k] = ["bad"]
        print("%s,服务监控出现问题" % k)


# msg = {
#     "ocs": "bad",
#     "eas": "bad",
# }

for k, v in msg.items():
    if v.lower() == "bad":
        print("%s,服务监控出现问题" % k)
