import requests
res=requests.get("www.google.com, adwords.googleblog.com, and http://www.google.com/intl/en/privacy.")
print(res.text)