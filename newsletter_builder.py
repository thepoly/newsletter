# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:43:06 2022

@author: William
"""

from bs4 import BeautifulSoup
from content_gttr import extract
import argparse
import sys

with open("html_blocks/bar.html") as inf:
    bar_txt = inf.read()
    
def build_top_story(url):
    attrs   = extract(url)
    kicker = attrs['kicker'].upper()
    summary = attrs['summary']
    image_link = attrs['image_link']
    headline = attrs['headline']
    image_text = attrs['image_text']
    author = attrs['author']
    author_link = attrs['author_link']
    
    kicker = kicker.upper()
    with open("html_blocks/top_story.html") as inf:
        txt = inf.read()
        html = txt.format(HEADLINE=headline,SUMMARY=summary, IMAGE_LINK=image_link,
                          KICKER=kicker,URL=url, ALT_TEXT=image_text)
    soup = BeautifulSoup(html, features='lxml')
    return soup

def build_middle_story_right(url):
    attrs   = extract(url)
    kicker = attrs['kicker'].upper()
    summary = attrs['summary']
    image_link = attrs['image_link']
    headline = attrs['headline']
    image_text = attrs['image_text']
    author = attrs['author']
    author_link = attrs['author_link']
    
    
    with open("html_blocks/middle_story_right.html") as inf:
        txt = inf.read()
        html = txt.format(HEADLINE=headline,SUMMARY=summary, IMAGE_LINK=image_link,
                          KICKER=kicker,URL=url, ALT_TEXT=image_text)
    soup = BeautifulSoup(html, features='lxml')
    return soup

def build_middle_story_left(url):
    attrs   = extract(url)
    kicker = attrs['kicker'].upper()
    summary = attrs['summary']
    image_link = attrs['image_link']
    headline = attrs['headline']
    image_text = attrs['image_text']
    author = attrs['author']
    author_link = attrs['author_link']
    
    
    with open("html_blocks/middle_story_left.html") as inf:
        txt = inf.read()
        html = txt.format(HEADLINE=headline,SUMMARY=summary, IMAGE_LINK=image_link,
                          KICKER=kicker,URL=url, ALT_TEXT=image_text)
    soup = BeautifulSoup(html, features='lxml')
    return soup
def bar():
    return BeautifulSoup(bar_txt, features='lxml')
        
blocks = [build_top_story, build_middle_story_right, build_middle_story_left]

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', "--output_file", action='store',dest='output_file', default='my_newsletter.html')
    parser.add_argument('-a', "--article_file", action="store", dest='articles_file', default='articles.txt')
    parser.add_argument('-t', "--template", action="store", dest='template', default='1')
    parser.add_argument('-b', "--block_types", action='store', dest='block_types', type=int, nargs='+', default=None)
    
    args = parser.parse_args(sys.argv[1:])
    
    block_types = args.block_types
    
    with open(args.articles_file) as inf:
        articles = inf.readlines()
    
    n_articles = len(articles)
    if n_articles != len(block_types):
        raise Exception(f"Number Of Blocks Provided Does Not Match Number Of Articles in {args.articles_file}")
    
    for i in range(n_articles):
        articles[i] = articles[i].strip()
        
    
    template_fd = open(f"html_blocks/template{args.template}.html")
    template = BeautifulSoup(template_fd.read(),features='lxml')    
    template_fd.close()
    
    body = template.find("td", {'class': "middleBodyContainer"})
    
    sequential = []
    
    print("FETCHING ARTICLES")
    for i in range(n_articles):
        bt = block_types[i]
        block = blocks[bt](articles[i])
        
        sequential.append(block)
        
        if i != n_articles - 1:
            sequential.append(bar())
    
    title = 'Newsletter'

    print("COMPILING HTML")
    body.extend(sequential)

     
    newsletter = open('my_newsletter.html', 'w')
    template.title.insert(0,title)
    template.year.insert(0,'2022')
    html = str(template)
    newsletter.write(html)
    newsletter.close()

    print("COMPLETED")