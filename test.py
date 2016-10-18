import urlparse
import urllib
# url = "https://mp.weixin.qq.com/mp/appmsgreport?action=page_time&uin=MTA5ODgyODIxOQ%253D%253D"
url = "https://mp.weixin.qq.com/mp/appmsgreport?" \
      "action=page_time&uin=MTA5ODgyODIxOQ%253D%253D" \
      "&key=502b9ab53198616f2434bd77d7ef23a2310cd82c7943" \
      "2a223001322d161a8ba7139e896da8e6ab1a888035b3209f2bb5" \
      "&pass_ticket=5hwsCURiRkvnYE%25252Bi46t3LWFRsLUD5lBxFmuA" \
      "AA6bb1E5WbevN%25252FadGm1LcZa%25252FBmyC&wxtoken=1444852650" \
      "&devicetype=Windows-QQBrowser&clientversion=61030004&x5=0"
print urllib.unquote(urllib.unquote(url))
