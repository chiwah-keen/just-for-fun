#coding=utf-8
import sys
import webbrowser
import requests
#sys.path.append("libs")

user_input=raw_input('please input domain:')

READ_FILE = "content.txt"
HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6    4 Safari/537.11'}


f = open(READ_FILE,"r") 
sline = f.readline()
while sline:
    exps = sline+' '+"site:"+user_input
    url = "https://www.baidu.com/s?wd="+exps
    sline = f.readline()
    r = requests.get(url,headers=HEADER)
    print r.content
