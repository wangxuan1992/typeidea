
import requests

url ='https://m701.music.126.net/20190611174941/a248a8a52044cdbbb717804765e43c87/jdyyaac/065a/0309/0509/10b0671ffc4c2448a7df2c472b3dca4d.m4a'

headers = {
    'UserAgent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

resp = requests.get(url=url,headers=headers).content

with open('pingfanzhilu.m4a','wb') as fp:
    fp.write(resp)

# print(resp)