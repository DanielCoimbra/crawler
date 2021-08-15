#! /usr/bin/env python
from bs4 import BeautifulSoup
import requests
import json
import time
import re

session = requests.Session()
GET = '0'
POST = '1'
URL = "https://www.fishbase.se/Country/CountryChecklist.php?resultPage=1&c_code=076&vhabitat=all2&cpresence=present"

def get_tvalues(session, url):
	response = session.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	values = soup.body.find_all("tr", "t_value1")
	return values
	

def pages_gen():
	l_url = list(URL)
	for i in range(1,96):
		l_url[64] = str(i) # iterates through the result_page url variable 
		print(''.join(l_url))
		yield get_tvalues(session, ''.join(l_url))	# soup.find_all returns a list, so
			#print(type(page)

def fish_gen(page):
	for fish_row in page:
		yield fish_row

class Fish():
        
	def __init__(self, order='', family='', species='', ocurrence='', fishbase_name='', name='', link='', _id=''):
		
		self.order = order
		self.family = family
		self.species = species
		self.ocurrence = ocurrence
		self.fishbase_name = fishbase_name
		self.name = name
		self.link = link
		self._id = _id

		def get_images():
			pass

def main():
	with open("fishbase.json","r") as f:
		data = json.load(f)
	
	
	for page in pages_gen():
		for fish in fish_gen(page):
			l = list(fish)
			print(l[4].a['href'])
			regex = re.match('id=[0-9]+', l[4].a['href'])
			print(regex)
			f=Fish(
				order = l[0].contents[0] or 'N/A',
				family = l[2].contents[0] or 'N/A',
				species = l[4].a.contents[0]  or 'N/A',
				ocurrence = l[5].contents[0]  or 'N/A',
				fishbase_name = l[6].contents[0]  or 'N/A',
				name = l[7].contents[0] or 'N/A',
				link = l[4].a['href'] or 'N/A',
				#_id= re.match('id=[0-9]+',l[4].a['href']).group()[3:] or 'N/A' #
			
			)
			print(f.__dict__)


main()
	

#now = time.localtime()
#f_name = f"{now.tm_year}_{now.tm_mon}_{now.tm_mday}_{now.tm_hour}_{now.tm_min}_{now.tm_sec}"

#with open("t_values.txt", "a") as f:
#	f.write(?)

#def get_soup(url, action=GET, params={}):
#	request = None
#	success_request = True
#	if action == GET:
#		try:
#			request = session.get(url)
#		except requests.exceptions.RequestException:
#			sucess_request = False
#	elif action == POST:
#		try:
#			request.session.post(url,params)
#		except request.exceptions.RequestException:
#			sucess_request = False
#	else: 
#		return None
#
#	if success_request:
#		html = request.text
#	else:
#		html = ''
#	soup = BeautifulSoup(html, features="html.parser")
