#coding:utf-8
import requests
import re
import urllib
import urllib.request
import time

file_path='E:/img'
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
def getimg(url):
    html = requests.get(url)
    site = re.findall(re.compile('<a class="zoom icon-zoom" target="_blank" href="(.*?)"'),html.text)
    for each in site:
        urllib.request.urlretrieve(each, "E:/img/"+str(round(time.time() * 1000))+".png") 

for num in a:
    html = requests.get("https://isujin.com/page/"+num)
    site = re.findall(re.compile('class="posttitle" href="(.*?)">'),html.text)
    for each in site:
        print(each)
        getimg(each)
