#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from UTIL import Browser, Autorizador

URL_SEFAZ_NFCE = "http://www.nfce.se.gov.br/portal/ConStatusAuto?Origem=1"

def status(tag):
	if str(tag).find("Ativo") != -1:
		status = "Disponivel"
	elif str(tag).find("Alerta") != -1:
		status = "Instavel"
	elif str(tag).find("Disponibilidade futura") != -1:
		status = "Não Liberado"
	else:
		status = "Não Encontrado"

	return status

def verifica_disponibilidade(autorizador):
	result = {}
	if not Autorizador.existe_autorizador(autorizador):
		result['Erro'] = "Estado não encontrado"
		return result

	html = Browser.carrega_pagina(URL_SEFAZ_NFCE)
	rows = html.findChildren(['tr'])
	dataRows = []

	for row in rows:
		cells = row.findChildren('td')
		dataCells = []
		for cell in cells:
			dataCells.append(cell)
		dataRows.append(dataCells)

	autorizador = Autorizador.pega_autorizador_nfce(autorizador)

	for data in dataRows:
		if str(data).find(autorizador) != -1:
			result['Autorizador'] = autorizador
			result['Status'] = status(data[1])
			result['Menor'] = data[2].text
			result['Maior'] = data[3].text
			result['Media'] = data[4].text
			break

	return result