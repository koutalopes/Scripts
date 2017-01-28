# -*- coding: utf-8 -*-

"""
03/10/2016
koutalopes

0.1
"""

import feedparser
import urllib.request

def get_links():
    rss = "http://www.shanaproject.com/feeds/secure/user/37700/WHXW4234TW/"
    d = feedparser.parse(rss)

    a = [x for x in d["items"]]

    return a

def save_file():
    sav = "/home/kouta/.config/rtorrent/watch/"
    for item in get_links():
        name = item["description"]
        content = urllib.request.urlopen(item["link"])

        open ("{}{}.torrent".format(sav, name), "wb").write(content.read())

save_file()
