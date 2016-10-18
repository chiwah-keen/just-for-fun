import requests
# =http://mp.weixin.qq.com/\/\/mp.weixin.qq.com\/s?__biz=MzA5MjczNzg1MQ==&mid=2247485006&idx=4&sn=7b3086182d210f588733be3c9628046a&chksm=9069de1aa71e570c23ed6d9d3570aaf72c0ba2178010859da5721a8a2ac35c0392d497614e16&scene=27#wechat_redirect
url = "http://mp.weixin.qq.com/mp/getappmsgext?__biz=MzA5MjczNzg1MQ==&appmsg_type=9&mid=2247485006&sn=7b3086182d210f588733be3c9628046a&idx=1&scene=4&title=dddd&ct=1468477176&devicetype=Windows-QQBrowser&version=/mmbizwap/zh_CN/htmledition/js/appmsg/index31133c.js&f=json&r=0.9989595734514296&is_need_ad=0&comment_id=0&is_need_reward=0&both_ad=0&reward_uin_count=0&uin=MTA5ODgyODIxOQ%253D%253D&key=c3acc508db720376a1ec3ef923e474fc3332f72d8b078ef3e7fed23fd4eddcf7cd773ebcf7d8b9946730bb6695de8774&pass_ticket=KPTw%25252FtQ9q%25252BbqJ%25252By9RnPbeJssMAifEmo2GNbJCE%25252FuY45TgwneNjPdiESWDBmh0vvT&wxtoken=2856882382&devicetype=Windows-QQBrowser&clientversion=61030004&x5=0 HTTP/1.1"
headers = {
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    'Content-Length': '60',
    'Origin': 'https://mp.weixin.qq.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':  'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.640.400 QQBrowser/9.4.8309.400',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'https://mp.weixin.qq.com/s?__biz=MzA5NTQ4NjE1MQ==&mid=2652647601&idx=1&sn=6af177683b4d46ded9e03838d3155223&scene=4&key=c3acc508db720376a1ec3ef923e474fc3332f72d8b078ef3e7fed23fd4eddcf7cd773ebcf7d8b9946730bb6695de8774&ascene=1&uin=MTA5ODgyODIxOQ%3D%3D&devicetype=Windows-QQBrowser&version=61030004&pass_ticket=KPTw%2FtQ9q%2BbqJ%2By9RnPbeJssMAifEmo2GNbJCE%2FuY45TgwneNjPdiESWDBmh0vvT',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'wxtokenkey=4b49ebaedabde2ec88c411bfbdaee35b4eba2de6afb9f9a568fee7ceef4ccae1; wxticket=2257020227; wxticketkey=de53f2493d5ae0a814d0bf306bfbc72a4eba2de6afb9f9a568fee7ceef4ccae1; wap_sid=CLuT+4sEEkBRV0s3MFFoQVRlQ2ZLc3o3cUJPc2dkblJ3WnZsaGNBaGplRExocUxVVVg1cWp4emxTdDJNNHNOUGJMLWNycFpEGAQg/BEox72FxAswrK+CwAU='
}


r = requests.post(url=url, data="is_only_read=1&req_id=13170QRWHHoAg3AZ7lJC64bC&is_temp_url=0", headers=headers)
print r.content
