#!/usr/bin/python3
"""
从forvo.com爬取单词发音
"""
import argparse
import base64
import requests
import bs4
import os
import fake_useragent

basedir = os.path.abspath(os.path.dirname(__file__))

def get_mp3(word, lang):
    """
    获取单词mp3
    """
    url = 'https://forvo.com/search/{word}/#{lang}'.format(word=word,lang=lang)
    print(url)
    firefox = fake_useragent.UserAgent().ff
    t = requests.get(url, headers={'User-Agent': firefox}).text
    soup = bs4.BeautifulSoup(t, 'lxml')

    content = soup.select_one('span[id^="play_"]')
    
    s = str(content['onclick'])
    mp3_name = s.strip('Play(').strip(');return false;').split(',')[1].strip("'")
    if not mp3_name:
        print('error')
    print(mp3_name)
    p = base64.b64decode(mp3_name).decode()
    dl_url = 'https://audio00.forvo.com/mp3/{}'.format(p)
    firefox = fake_useragent.UserAgent().ff
    c = requests.get(dl_url, headers={'User-Agent': firefox}, stream=True)
    if not os.path.isdir(os.path.join(basedir, 'voice')):
        os.mkdir(os.path.join(basedir, 'voice'))
    dl_path = os.path.join(basedir, 'voice/{}.mp3'.format(word))
    with open(dl_path, 'wb') as f:
        for chunk in c.iter_content():
            f.write(chunk)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", type=str,
                    help="词汇")
    parser.add_argument("-l", type=str,
                    help="语言")
    p = parser.parse_args()                    
    get_mp3(p.word, p.l)
