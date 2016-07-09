# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:23:52 2016

@author: Deep
"""

from pws import Google
from bs4 import BeautifulSoup
import requests
import re
def search():
    url = (Google.search(query='software engineering internships', num=30, start=0, country_code="es"))
    urls = url['url']
    r = requests.get(urls)
    plain_text = r.text
    soup = BeautifulSoup(plain_text,"lxml")
    pattern = re.compile(r"<h3 class=\"r\"><a.*?>(.*?)</a></h3>")
    string=str(pattern)
    match_pattern = re.findall(pattern,plain_text)
    '''for link in match_pattern:  # printing the titles from the above pattern
        print(link)'''
    links=[]
    MAPPING = { 
    	    '%3D': '=',
    	    '%3F': '?',
    	    '%2B': '+',
    	    '%23': '#',
    	}
     
    for i in soup.findAll("a"):  # printing the links
        href = i.get("href")
        if re.search("google|youtube",href):
            pass
        else:
            if re.search("http",href):
                k = re.search("http",href)
                rough = (href[k.start():])
                #check mapping patterns
                rough = re.sub('%3D',MAPPING['%3D'],rough)
                rough = re.sub('%3F',MAPPING['%3F'],rough)
                rough = re.sub('%2B',MAPPING['%2B'],rough)
                rough = re.sub('%23',MAPPING['%23'],rough)
                m = re.search("&",rough)
                links.append(rough[:m.start()])
                print(rough[:m.start()])

    data_store = {}

    for i in range(len(links)):
        nm = re.search(r'\..*\.',links[i])
        name = links[i][nm.start():nm.end()]
        name = re.sub('\.','',name)
        val = []
        val.append(name)
        val.append(links[i])
        data_store[i+1] = val