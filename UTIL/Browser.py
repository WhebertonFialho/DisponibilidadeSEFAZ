from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

headers = {	'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}

def carrega_pagina(url):
	html_doc = urlopen(url).read()
	html_dom = BeautifulSoup(html_doc, "html.parser")
	return html_dom