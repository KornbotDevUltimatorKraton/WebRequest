from gsearch.googlesearch import search # google search auto 
from googlesearch import search
import webbrowser
import textract # Content extract  
import pydf 
import pyce3
import requests
import time 
for url in search('Servo driver ic Texas instrument'+'.html'):
    print(url)
    print(len(url))
    print(url[int(len(url))-4])
    if str(url[int(len(url))-4]) == 'h':
      try:   
         html = requests.get(url).content
         encoding, time, title, text, next_link = pyce3.parse(url, html)
         print("Encoding："+ encoding)
         print('='*10)
         print("Title："+title)
         print("time："+time)
         print('='*10)
         print("Text："+text)
         print("NextPageLink: ", next_link)
         time.sleep(0.3)
         # Search from the content best on components price 
         for url2 in search(str(title)+'price'):
                 print("Compoent search for price")
                 print(url2)
                 try:   
                   html = requests.get(url2).content
                   encoding, time, title, text, next_link = pyce3.parse(url2, html)
                   print("Encoding："+ encoding)
                   print('='*10)
                   print("Title："+title)
                   print("time："+time)
                   print('='*10)
                   print("Text："+text)
                   print("NextPageLink: ", next_link)
                   time.sleep(0.002)
                 except:
                     print("Different webpage with other document file")
                     #time.sleep(0.002)
      except: 
           print("Different webpage with other document file")
    else: 
       print("Different webpage with other document file")
   
