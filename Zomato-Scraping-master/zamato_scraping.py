    from  selenium  import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
import json,os
def zamato():
	list1=[]
	browser = webdriver.Chrome()
	browser.get("https://www.zomato.com/ncr")
	driver=browser.execute_script("return document.documentElement.outerHTML")
	soup=BeautifulSoup(driver,"html.parser")
	main_div=soup.find("div",class_="ui segment row")
	lin=main_div.find_all("a",class_="col-l-1by3 col-s-8 pbot0")
	for i in lin:
		link=i.get("href")
		list1.append(link)
	browser.quit()
	return list1

url=zamato()
a=0
for j in url:
	browser1=webdriver.Chrome()
	browser1.get(j)
	driver1=browser1.execute_script("return document.documentElement.outerHTML")
	soup1=BeautifulSoup(driver1,"html.parser")
	name=soup1.find_all("div",class_="col-s-12")
	all_name=[]
	for i in name:
		n=i.find("a",class_="result-title")
		name1=n.get("title")
		all_name.append(name1)
	pl=soup1.find_all("div",class_="row")
	plecs_name=[]
	for j in pl:
		try:
			plecs=j.find("div",class_="col-m-16 search-result-address grey-text nowrap ln22")
			a=plecs.get("title")
			plecs_name.append(a)
		except AttributeError:
			continue
	rate=soup1.find_all("span",class_="col-s-11 col-m-12 pl0")
	price_list=[]
	for l in rate:
		p=(l.text)
		price_list.append(p)
	ra=soup1.find_all("div",class_="rating-popup")
	rating_list=[]
	for k in ra:
		rating=(k.text.strip())
		rating_list.append(rating)
	vot=soup1.find_all("span",class_="ta-right")
	print(vot)
	browser1.quit()


