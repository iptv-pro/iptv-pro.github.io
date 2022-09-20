#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse, urlunparse, quote

import requests
import json
import re
import os


name_dict = {
"中国教育1":"中国教育1台",
"中国教育2":"中国教育2台",
"中国教育3":"中国教育3台",
"中国教育4":"中国教育4台",
"北京卡酷少儿":"卡酷动画",
"北京影视":"BTV影视",
"北京文艺":"BTV文艺",
"北京新闻":"BTV新闻",
"北京生活":"BTV生活",
"北京科教":"BTV科教",
"北京财经":"BTV财经",
"北京青年":"BTV青年",
"北京4K超清IPTV":"北京IPTV4K超清",
"北京IPTV-淘电影":"北京IPTV淘电影",
"北京IPTV@大健康":"北京IPTV大健康",
"北京冬奥纪实4K":"北京冬奥纪实",
}

README = '''\
## TV logo list

### source
https://github.com/msolihinam/tv/tree/main/logo\n

https://github.com/Sppotato/Sppotato.github.io\n

https://github.com/m3u8playlist/tvlogo\n


|Icon|Channel|Site|
|:----|:---:|:---:|
'''

def list_files(basepath):

    filelist = []

    for entry in os.listdir(basepath):
        fullpath = os.path.join(basepath, entry)
        if os.path.isfile(fullpath):
            filelist.append(fullpath)
        else:
            print(fullpath)
            #filelist.extend(list_files(fullpath))

    return filelist


if __name__ == '__main__':

    logolist = sorted(list_files("logo/"))

    logodict = {}
    for logo in logolist:
        title = logo.split("/")[-1].replace(".png", "").replace(".jpg", "").replace(".webp", "")
        if title in name_dict.keys():
            title = name_dict[title]
        link = "https://iptv-pro.github.io/%s"%quote(logo)
        logodict[title] = link

    with open('list.txt', 'w') as file_obj:
        for title, link in logodict.items():
            file_obj.write("%s,%s\n"%(title, link))

    with open('README.md', 'w') as file_obj:
        file_obj.write(README)
        for title, link in logodict.items():
            file_obj.write('|<img src="%s" width="100" height="50">|%s|%s|\n'%(link, title, link))
