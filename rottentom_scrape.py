# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:33:38 2018

@author: saranshmohanty
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:28:56 2018

@author: saranshmohanty
"""

#important imports
#from __future__ import division
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import nltk

#os.chdir('C:/Users/x/Desktop/Post Campaign/sicario-2/movie')
os.chdir('C:/Users/saranshmohanty/Desktop')
movie_name = "sicario_day_of_the_soldado"
movie_name = movie_name.lower()
movie_name = movie_name.strip()
movie_name = re.sub("[ ,.]", "_", movie_name)

num_page  = []
#x = "https://www.rottentomatoes.com/m/sicario_day_of_the_soldado/reviews/?page=2&sort="
x = "https://www.rottentomatoes.com/m/"+movie_name+"/reviews/?page=2&sort="

response1 = requests.get(x)
soup = BeautifulSoup(response1.text,'html.parser')
num_page = soup.find_all(class_='pageInfo')
num_page = pd.DataFrame(num_page)
num_page.columns = ['try']
num_page1 = str(num_page)
#num_page1 = list(set(num_page[0][0]))
num_page2 = [l.split(' ') for l in num_page1.split('\n') if l]
num_page3 = num_page2[1]
num_page4 = num_page3[6]
num_page5 = num_page4[0:-7]
num_page5 = int(num_page5)



url = []
for i in range(1,num_page5+1):
    x = "https://www.rottentomatoes.com/m/"+movie_name+"/reviews/?page="+str(i)+"&sort="
    url.append(x)




review = []
for i in range(len(url)):
    response1 = requests.get(url[i])
    soup = BeautifulSoup(response1.text,'html.parser')
    #review_list = soup.find_all(class_='content')
    review_list = soup.find_all(class_='the_review')
    review.append(review_list)


    
final_review = []
for i in range(len(review)):
    for j in range(len(review[i])):
        review_list = review[i][j]
        final_review.append(review_list)
        
final_review = pd.DataFrame(final_review)        
final_review.columns = ['review']
final_review.to_csv("review.csv",index=False,encoding='utf-8')



