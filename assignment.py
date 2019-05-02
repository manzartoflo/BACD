#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:10:53 2019

@author: manzar
"""
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
url = "http://www.bacd.be/en/leden/default.asp?page="
header = "Company name, Telephone, Email, Website, Country\n"
file = open("assignment.csv", "w")
file.write(header)
for i in range(1,3):
    req = requests.get(url + str(i))
    soup = BeautifulSoup(req.text, "lxml")
    links = soup.findAll("tr")
    for link in links[:-1]:
        rqst = requests.get(urljoin(url, link.a.attrs['href']))
        soup_inside = BeautifulSoup(rqst.text, "lxml")
        divs = soup_inside.findAll("tr")
        name = divs[0].contents[3].text
        #print(name)
        telephone = divs[0].contents[7].text
        #print(telephone)
        country = divs[3].contents[3].text
        #print(country)
        email = divs[5].contents[3].text 
        #print(email)
        website = divs[6].contents[3].text 
        #print(website)
        file.write(name.replace(",", "") + ", " + telephone.replace(",", "") + ", " + email.replace(",", "") + ", " + website.replace(",", "").replace("\n\t\t\t\t\t\xa0", "") + ", " + country.replace(",", "") + "\n " )
        print("wait...")
file.close()
        

import pandas 
file = pandas.read_csv("assignment.csv")