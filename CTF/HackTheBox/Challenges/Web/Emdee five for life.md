# Emdee five for life

date: `2021-09-09`

题目很简单, 就是给你一个字符串, 求它的md5, 手动提交的话, 会提醒太慢了. 那就上脚本呗...

```python
import sys
import hashlib
import requests
url = "http://178.128.160.242:32735/"

string_tag = "<h3 align='center'>"
flag_tag = "<p align='center'>"
end_char = "<"

def get_msg(tag, text):
	text = text[text.find(tag) + len(tag):]
	text = text[:text.find(end_char)]

	return text



def check():

	with requests.get(url) as response:
		cookie = response.headers['Set-Cookie'].split(';')[0]

		# print(cookie)

		html = response.text

		# print('[!] body is:\n {}'.format(html))

		string = get_msg(string_tag, html)


		# print('[!] string: {}'.format(string))


		md5 = hashlib.md5(string.encode('utf-8')).hexdigest()
		print('[!] md5 of {} is {}'.format(string, md5))


		headers = {"Cookie":cookie}
		data = {"hash":md5}

		with requests.post(url, data=data, headers=headers) as response:
			if "HTB" in response.text:
				print('[+] flag is: {}'.format(get_msg(flag_tag, response.text)))
				exit()


while(True):
	check()
```