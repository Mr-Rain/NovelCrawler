#!usr/bin/python3.6
# -*- coding: UTF-8 -*-

import requests
from requests.exceptions import RequestException
import re
import time

def get_first_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def get_urls(html):
    firstPattern=re.compile('正文卷</dt>.*</dl>',re.S)
    firstItem=re.findall(firstPattern,html)
    secondPattern=re.compile('href ="(.*?)">',re.S)
    items=re.findall(secondPattern,firstItem[0])
    return items

def get_text(items):
    for item in items:
        url='https://www.sbiquge.com'+item
        response = requests.get(url)
        html=response.text
        pattern=re.compile('showtxt">.*天才一秒',re.S)
        text=re.findall(pattern,html)
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(text[0])
            f.close()

def main():
    html=get_first_page('https://www.sbiquge.com/8_8551/')
    items=get_urls(html)
    get_text(items)

if __name__ == '__main__':
    main()
    time.sleep(1)