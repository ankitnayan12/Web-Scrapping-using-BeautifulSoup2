# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 06:58:17 2019

@author: ankit
"""

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context


# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "bhgxx2 col-12-12"})
print(len(containers))
# name the output file to write to local disk
out_filename = "flipkart7.csv"
# header of csv file to be written
headers = "product_name,Rating,Price \n"

# opens file, and writes headers
f = open(out_filename, "w",encoding="utf-8")
f.write(headers)


for container in containers:
    product_name = container.find("div", {"class":"_3wU53n"})
    product_rating = container.find("div", {"class":"hGSR34"})
    product_price = container.find("div", {"class":"_1vC4OE _2rQ-NK"})
    if product_name:
        x='Product Name:{}, Rating:{}, Price:{}\n'.format(product_name.get_text(),product_rating.get_text(), product_price.get_text())
        print(x)
    f.write(x)
    
f.close()
"""
for container in containers:
    product_name = container.find("div", {"class":"_3wU53n"})
    product_rating = container.find("div", {"class":"hGSR34"})
    product_price = container.find("div", {"class":"_1vC4OE _2rQ-NK"})
    if product_name:
        x='Product Name:{}, Rating:{}, Price:{}'.format(product_name.get_text(),product_rating.get_text(), product_price.get_text())
        print(x)
"""