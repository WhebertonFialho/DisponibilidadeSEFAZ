#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from UTIL import Browser, Autorizador

URL_SEFAZ = "http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx"

TABLE_V_3_10 = "ctl00_ContentPlaceHolder1_gdvDisponibilidade"
TABLE_V_4_00 = "ctl00_ContentPlaceHolder1_gdvDisponibilidade2"

def status(tag):
	status = ""
	if str(tag).find("verde") != -1:
		status = "Disponivel"
	elif str(tag).find("amarela") != -1:
		status = "Instavel"
	elif str(tag).find("vermelho") != -1:
		status = "Indisponivel"
	else:
		status = ""
	
	return status

def verifica_disponibilidade(versao, autorizador):
	result = {}
	autorizador = Autorizador.pega_autorizador_nfe(autorizador)

	if not Autorizador.existe_autorizador(autorizador):
		result['Erro'] = "Estado não encontrado"
		return result

	if not Autorizador.existe_versao_nfe(versao):
		result['Erro'] = "Versão não encontrada"
		return result

	html = Browser.carrega_pagina(URL_SEFAZ)
	table = html.find(id = TABLE_V_4_00 if versao == '4' else TABLE_V_3_10)
	rows = table.findChildren(['tr'])
	dataRows = []

	for row in rows:
		cells = row.findChildren('td')
		dataCells = []
		for cell in cells:
			dataCells.append(cell)
		dataRows.append(dataCells)

	for data in dataRows:
		if str(data).find(autorizador) != -1:
			result['Autorizador'] = data[0].text
			result['Autorizacao'] = status(data[1])
			result['RetornoAutorizacao'] = status(data[2])
			result['Inutilizacao'] = status(data[3])
			result['ConsultaProtocolo'] = status(data[4])
			result['StatusServico'] = status(data[5])
			result['TempoMedio'] = data[6].text
			result['ConsultaCadastro'] = status(data[7]) 
			result['RecepcaoEvento'] = status(data[8])
	
	return result