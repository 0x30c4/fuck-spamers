#!/usr/bin/python3
from requests import post
import random, string, urllib.parse

def makeFakeEmailPass(name):
	name = name.strip().lower()
	if name == '':
		name = "YoMotherFucker"
	email_domains = ["gmail", "hotmail", "yahoo", "outlook"]
	email = "{}{}@{}.com".format(name, random.randint(665, 958), random.choice(email_domains))
	pas = "".join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
	if random.randint(0, 1) == 0:
		pas = name + pas
	else:
		pas = pas + name
		
	print(email + " : " + pas + " : ", end="")
	return [email, pas]

def postData(server, data):
	headers = {
		"Host": "pomemxpghi.servegame.com",
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "http://pomemxpghi.servegame.com/login/",
		"Content-Type": "application/x-www-form-urlencoded",
		"Content-Length": str(len(data)),
		"Origin": "http://pomemxpghi.servegame.com",
		"Connection": "keep-alive",
		"Cookie":"m_pixel_ratio=1; wd=1366x768; _ga=GA1.3.50985375.1580722053; _gid=GA1.3.1386484211.1580722053",
		"Upgrade-Insecure-Requests": "1"
	}
	rep = post(server, data=data, headers=headers)
	# print(rep.text)
	print(rep.ok)

def main():
	data = "lsd=AVqkYwEU&charset_test=€,´,€,´,水,Д,Є&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts=1444981372&li=fKogVnFYklxjk1zuKIBvk-jr&email={}&pass={}&login=Đăng+nhập"
	# data = "lsd=AVqkYwEU&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts=1444981372&li=fKogVnFYklxjk1zuKIBvk-jr&email={}&pass={}&login=%C4%90%C4%83ng+nh%E1%BA%ADp"
	with open("names") as names:
		for name in names.readlines():
			data = urllib.parse.quote_plus(data.format(*makeFakeEmailPass(name)))

			postData("http://pomemxpghi.servegame.com/login/#", data)#.replace("@", "%40"))


if __name__ == '__main__':
	main()


# http://pomemxpghi.servegame.com/login/#
# curl 'http://pomemxpghi.servegame.com/login/#' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://pomemxpghi.servegame.com/login/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://pomemxpghi.servegame.com' -H 'Connection: keep-alive' -H 'Cookie: m_pixel_ratio=1; wd=1366x768; _ga=GA1.3.50985375.1580722053; _gid=GA1.3.1386484211.1580722053' -H 'Upgrade-Insecure-Requests: 1' --data 'lsd=AVqkYwEU&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts=1444981372&li=fKogVnFYklxjk1zuKIBvk-jr&email=sa%40fuck.com&pass=asdasdasdasd&login=%C4%90%C4%83ng+nh%E1%BA%ADp'

'''
Discovered open port 110/tcp on 172.96.191.84
Discovered open port 22/tcp on 172.96.191.84
Discovered open port 993/tcp on 172.96.191.84
Discovered open port 80/tcp on 172.96.191.84
Discovered open port 587/tcp on 172.96.191.84
Discovered open port 995/tcp on 172.96.191.84
Discovered open port 25/tcp on 172.96.191.84
Discovered open port 53/tcp on 172.96.191.84
Discovered open port 443/tcp on 172.96.191.84
Discovered open port 21/tcp on 172.96.191.84
Discovered open port 143/tcp on 172.96.191.84
Discovered open port 3306/tcp on 172.96.191.84
Discovered open port 26/tcp on 172.96.191.84
Discovered open port 465/tcp on 172.96.191.84
'''