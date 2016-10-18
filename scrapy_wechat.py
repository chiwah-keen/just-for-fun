# coding: UTF-8
'''
达观 批量请求接口脚本
'''
import requests
from urllib import urlencode, quote
import unittest
import json


def read_from_file(fname):
    with open(fname) as f:
        l = f.readline()
        while l:
            yield l
            l = f.readline()


def get_json(burl):
    json_text = requests.get(burl).text
    return {} if not json_text else json.loads(json_text)


def print_result(format_json):
    print "Status", format_json.get('status'), format_json


class testDataScrapyApi(unittest.TestCase):
    def __init__(self):
        self.appid = 2159877
        self.appname = 'fdsm'

    def test_articles(self, pos=0, cnt=2, tag='搞笑'):
        burl = "http://spiderapi.datagrand.com/articles/{appname}?" \
               "pos={pos}&cnt={cnt}&tag={tag}&appid={appid}".format(
               appname=self.appname, appid= self.appid, pos=pos, cnt=cnt, tag=tag)
        print_result(get_json(burl))

    def test_gzh_articles(self, gzhid, pos=0, cnt=2):
        burl = "http://spiderapi.datagrand.com/articles/{appname}?" \
               "pos={pos}&cnt={cnt}&gzhid={gzhid}&appid={appid}".format(
                appname=self.appnamem, appid=self.appid, pos=pos, cnt=cnt, gzhid=gzhid)
        print_result(get_json(burl))

    def test_gzhs(self, pos=0, cnt=20):
        burl = "http://spiderapi.datagrand.com/gzhs/{appname}?" \
               "appid={appid}&pos={pos}&cnt={cnt}".format(
            appname=self.appname, appid=self.appid, pos=pos, cnt=cnt)
        print_result(get_json(burl))

    def test_article_host(self, cateid=''):
        burl = "http://spiderapi.datagrand.com/article_hot/{appname}?" \
               "appid={appid}&cateid={cateid}".format(
            appname=self.appname, appid=self.appid, cateid=cateid)
        print_result(get_json(burl))

    def test_gzh_host(self, articleid):
        burl = "http://spiderapi.datagrand.com/gzh_hot/{appname}" \
               "?articleid={articleid}&appid={appid}".format(
            appname=self.appname, appid=self.appid, articleid=articleid)
        print_result(get_json(burl))

    def test_article_page(self, articleid):
        burl = "http://spiderapi.datagrand.com/article_page/{appname}?" \
               "appid={appid}&articleid={articleid}".format(
            appid=self.appid, appname=self.appname, articleid=articleid)
        print_result(get_json(burl))

    def test_subscrible(self, fname='fudan_wechat.txt'):
        for redirect_url in read_from_file(fname):
            try:
                burl = "http://spiderapi.datagrand.com/subscribe/{appname}?" \
                       "appid={appid}&article_url={encode_url}".format(
                    appid=self.appid, appname=self.appname, encode_url=quote(redirect_url))
                rst = get_json(burl)
                print "STATUS", rst.get('status'), rst, "Redirect_url", redirect_url
            except Exception as e:
                print "status FAIL", e


def main():
    tdsa = testDataScrapyApi()
    tdsa.main()

if __name__ == "__main__":
    main()

