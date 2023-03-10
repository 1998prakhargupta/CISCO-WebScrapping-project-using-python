import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import locale
import sys
from lxml import html
from lxml.html.soupparser import fromstring
import time
from io import StringIO
import os
import csv
import json
import pymysql
import urllib
import requests

request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com",
    "Connection": "close"
}





def get_soup(url, request_headers):
    while True:            
        #connectTor()
        r = requests.Session()
        response = r.get(url, headers=request_headers)
        the_page = response.content.decode('utf-8',errors='ignore')
        the_soup = BeautifulSoup(the_page, 'html.parser')
        if "please verify you're a human to continue" in the_page.lower():
            print("error flag condition matched while url: ", url)
            #renew_tor()
        else:
            return the_soup
            break
            
def get_page(url, request_headers):
    while True:            
        #connectTor()
        r = requests.Session()
        response = r.get(url, headers=request_headers)
        the_page = response.content.decode('utf-8',errors='ignore')
        if "please verify you're a human to continue." in the_page.lower():
            print("error flag condition matched while url: ", url)
            #renew_tor()
        else:
            return the_page
            break
        


def make_url(base_url , *res, **params):
    url = base_url
    for r in res:
        url = '{}/{}'.format(url, r)
    if params:
        url = '{}?{}'.format(url, urllib.parse.urlencode(params))
    return url
#print make_url('http://example.com', 'user', 'ivan', aloholic='true', age=18)


def get_content(x,a,b,c):
    try:
        y = x.find(a,{b:c}).get_text().strip()
    except:
        y= '***'
    return y
    

def get_elem(x,y):
    try:
        a = x[y]
    except:
        a ='***'
    return a
    
def get_tag(x,a,b,c,d):
    try:
        y = get_elem(x.find(a,{b:c}),d)
    except:
        y = '***'
    return y
    
    
def innerHTML_1(x,a,b,c):
    try:
        y = x.find(a,{b:c})
    except:
        y ='<p></p>'
    return y
    
    
def innerHTML(element):
    return element.decode_contents(formatter="html")
    
def dbinsert(dbname, tablename, fieldnames, fieldvalues):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='abc123', db=dbname,  charset='utf8')
    cur = conn.cursor()
    sqlstring = 'insert into ' + tablename + ' (' + ','.join(fieldnames) + ') VALUES (' + ','.join(['%s'] * len(fieldnames))+ ')'
    #print (sqlstring, fieldvalues)
    try:
        cur.execute(sqlstring, fieldvalues)
    except Exception as e:
        if not 'duplicate' in str(e).lower():
            print (str(e))
def session_get_page(s, url, request_headers):
    while True:            
        #connectTor()
        
        response = s.get(url, headers=request_headers)
        the_page = response.content.decode('utf-8',errors='ignore')
        if "please verify you're a human to continue." in the_page.lower():
            print("error flag condition matched while url: ", url)
            #renew_tor()
        else:
            return the_page
            break
def session_get_soup(s, url, request_headers):
    while True:            
        #connectTor()
        response = s.get(url, headers=request_headers)
        the_page = response.content.decode('utf-8',errors='ignore')
        the_soup = BeautifulSoup(the_page, 'html.parser')
        if "please verify you're a human to continue" in the_page.lower():
            print("error flag condition matched while url: ", url)
            #renew_tor()
        else:
            return the_soup
            break
