#-*- coding: utf-8 -*-

import re
import sys
import HTMLParser
reload(sys)
sys.setdefaultencoding('utf8')
import requests
if len(sys.argv) !=2 or not sys.argv[1].isdigit():
    print "请使用python {name} 1024 的方式启动脚本.".format(name=sys.argv[0])
    exit(0)

base_url = "https://www.exploit-db.com/ghdb/{page}/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
def parse_content(r,f):
    we_need = re.findall(r"rel=\"nofollow\">(.*)</a>",r.content)
    if we_need:
        html_parser = HTMLParser.HTMLParser()
        print "存入内容：",html_parser.unescape(we_need[0])
        f.write(html_parser.unescape(we_need[0])+"\n")
    else:
        print r.content
        f.write("\n")
        print "未匹配到内容"

with open('content.txt','w') as f:
    for i in range(int(sys.argv[1])):
        if i == 0:
            f.truncate()
        print "发起get请求",base_url.format(page=i+1)
        try:
            r = requests.get(base_url.format(page=i+1),headers=headers)
        except Exception,e:
            print "错误:",e
            continue
        if r.status_code == 200:
            parse_content(r,f)
        else:
            print "返回错误码:",r.status_code


