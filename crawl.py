#! /usr/bin/env python
from bs4 import BeautifulSoup
import requests
import json
import time
import re

session = requests.Session()
GET = '0'
POST = '1'
TABLE_URL = "https://www.fishbase.se/Country/CountryChecklist.php?resultPage=1&c_code=076&vhabitat=all2&cpresence=present&ext_pic=on"
FISH_BIO="https://www.fishbase.se/Country/CountrySpeciesSummary.php?c_code=076&id=" #Just append fish_id to url
FISH_PICS="https://www.fishbase.se/photos/ThumbnailsSummary.php?ID=" #Just append fish_id to url

def get_tvalues(session, url):
	response = session.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	values = soup.body.find_all("tr", "t_value1")
	return values
	

def get_page_json(page_n, url):
	page_data={}
	l_url = list(url)
	l_url[64] = str(page_n)
	#try:
		
	page = get_tvalues(session, ''.join(l_url))
	# print(page)

		
	# except:
	# 	return {"0":"error"}
	cont=0
	for fish in fish_gen(page):
		
		l = list(fish)
		# print(cont)
		try:
			pic = l[8].img['src']
		except:
			pic = 'N/A'
		f=Fish(
			order = l[0].contents[0] or 'N/A',
			family = l[2].contents[0] or 'N/A',
			species = l[4].a.contents[0]  or 'N/A',
			ocurrence = l[5].contents[0]  or 'N/A',
			fishbase_name = l[6].contents[0]  or 'N/A',
			name = l[7].contents[0] or 'N/A',
			link = l[4].a['href'] or 'N/A',
			pic = pic,
			_id= re.search('id=[0-9]+',l[4].a['href']).group()[3:] or 'N/A' #
		
		)
		cont+=1
		page_data[f._id] = f.__dict__
	return page_data

def get_all_tables():
	cont = 0
	table_all_fish = {}
	for i in range(1,96):
		# print(cont)
		cont+=1
		table_all_fish.update(get_page_json(i, TABLE_URL))

	return table_all_fish

#def get_fresh_tables():
#	table_fresh_fish = {}
#	for i in range(1,72):
		# table_fresh_fish.update(get_page_json(i, TABLE_URL.replace("all2", "fresh")))

	#return table_fresh_fish

#NOVAS FUNÇÕES
def get_fish_id(page_n, url):
	l_url = list(url)
	l_url[64] = str(page_n)
	#try:		
	page = get_tvalues(session, ''.join(l_url))
	# print(page)	
	# except:
	# 	return {"0":"error"}
	cont=0
	for fish in fish_gen(page):
		l = list(fish)
		_id = re.search('id=[0-9]+',l[4].a['href']).group()[3:] or 'N/A'		
		cont+=1

	return _id

def get_freshwater_list():
	fresh_fish_list = []
	for i in range(1,72):
		fresh_fish_list.append(get_fish_id(i, TABLE_URL.replace("all2", "fresh")))

	return fresh_fish_list

def get_saltwater_list():
	salt_fish_list = []
	for i in range(1,72):
		salt_fish_list.append(get_fish_id(i, TABLE_URL.replace("all2", "fresh")))

	return 	salt_fish_list

def get_introduced_list():
	introduced_fish_list = []
	for i in range(1,72):
		introduced_fish_list.append(get_fish_id(i, TABLE_URL.replace("all2", "fresh")))

	return introduced_fish_list

def get_endemic_list():
	endemic_fish_list = []
	for i in range(1,72):
		endemic_fish_list.append(get_fish_id(i, TABLE_URL.replace("all2", "fresh")))

	return endemic_fish_list

#ALTERNATIVA AGIL
def get_fish_list_by_atribute(pages_n, atribute):
	#dict com 'atributo','key','page_n','lista'
	# for atributo in dict:
	# 	for i in range(atributo.page_n):
	# 		atributo.lista.append(get_fish_id(i, TABLE_URL.replace("all2", atribute.key)))
	# return dict
	atribute_fish_list = []
	for i in range(1,pages_n):
		atribute_fish_list.append(get_fish_id(i, TABLE_URL.replace("all2", atribute)))

	return atribute_fish_list




def enter_fish_bio(id):
	pass
def more_images_fish(id):
	pass

def fish_gen(page):
	for fish_row in page:
		yield fish_row

class Fish():
        
	def __init__(self, order='', family='', species='', ocurrence='', fishbase_name='', name='', link='', _id='', pic=''):
		
		self.order = order
		self.family = family
		self.species = species
		self.ocurrence = ocurrence
		self.fishbase_name = fishbase_name
		self.name = name
		self.link = link
		self._id = _id
		self

		
def get_images():
	pass
		
def get_bio():
	pass

def t():
	class Struct:
	    def __init__(self, **entries):
    		self.__dict__.update(entries)

		
	#with open("fishbase.json", "w") as f:
	#	json.dump(data, f)


# def pages_gen():
# 	l_url = list(URL)
# 	for i in range(1,96):
# 		l_url[64] = str(i) # iterates through the result_page url variable 
# 		print(''.join(l_url))
# 		yield get_tvalues(session, ''.join(l_url))	# soup.find_all returns a list, so
# 			#print(type(page)

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
