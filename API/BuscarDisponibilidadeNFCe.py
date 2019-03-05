#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from UTIL import Browser, Autorizador, Html

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
	linhas = Html.carrega_tabela(html)
	autorizador = Autorizador.pega_autorizador_nfce(autorizador)

	for linha in linhas:
		if str(linha).find(autorizador) != -1:
			result['Autorizador'] = autorizador
			result['Status'] = status(linha[1])
			result['Menor'] = linha[2].text
			result['Maior'] = linha[3].text
			result['Media'] = linha[4].text
			break

	return result