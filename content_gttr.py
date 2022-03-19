# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:57:57 2022

@author: William
"""

from urllib import request
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    url = "https://poly.rpi.edu/sports/2022/03/engineers-advance-after-game-3-thriller/"
    page = request.urlopen(url)
    soup = BeautifulSoup(page, features='lxml')


def extract(url):
    page = request.urlopen(url)
    soup = BeautifulSoup(page, features='lxml')
    
    headline = soup.find("meta", property="og:title")['content']
    summary = soup.find("meta", property="og:description")['content']
    image_link = soup.find("meta", property="og:image")['content']
    image_tag = soup.find('div', {'class':re.compile('featured-photo *')})
    author_tag = soup.find('a', {'class':'author-name'})
    author_link = author_tag.attrs['href']
    author = "https://poly.rpi.edu/" + author_tag.text
    
    
    
    try:
        image_text = image_tag.text
    except:
        image_text = ""
    kicker = soup.find("strong", {'class': "text-primary text-uppercase text-kicker"} ).text
    
    
    #TO DO: fetch author name(s) and featured image photographer.
    return {'headline': headline,
            'summary': summary,
            'image_link': image_link,
            'image_text': image_text,
            'kicker': kicker,
            'author': author,
            'author_link': author_link }

