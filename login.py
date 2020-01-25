import requests
import filecmp
from bs4 import BeautifulSoup
from requests.auth import HTTPDigestAuth
from getpass import getpass
from requests import session

web_text = open("text_aux","w")


USENAME='mihail.maracine0605'
PASSWORD=getpass()
POST_LOGIN_URL = 'https://acs.curs.pub.ro/2019/login/index.php'
REQUEST_URL = 'https://acs.curs.pub.ro/2019/course/view.php?id=122'
with session() as session:
	req = session.get(POST_LOGIN_URL).text
	html = BeautifulSoup(req,'lxml')
	token = html.find("input", {"name": "logintoken"}).attrs['value']
	button = html.find_all("button", class_= "btn btn-primary btn-block mt-3")
	payload = {
	'username': USENAME,
	'password': PASSWORD,
	'logintoken': token
	}
	payload["button"]="Login"
	post = session.post(POST_LOGIN_URL, data=payload)
	r = session.get(REQUEST_URL)
	soup = BeautifulSoup(r.text, "lxml")
	# print(soup.get_text())

	web_text.write(soup.text)
	web_text.close()
	text_list1 = open("text_aux").readlines()
	updates = open("Updates","w")
	for i in range(200,300):
		if text_list1[i] != '\n':
			updates.write(text_list1[i])
	updates.close()
	print("Choose your optinon:")
	print("1. Update base form of site")
	print("2. Check if site updated")
	OPTIONS = int(input())

	if OPTIONS == 1:
		updates = open("NoUpdates","w")
		for i in range(200,300):
			if text_list1[i] != '\n':
				updates.write(text_list1[i])
		updates.close()
	elif OPTIONS == 2:
		print(filecmp.cmp("Updates","NoUpdates"))
#array cmp