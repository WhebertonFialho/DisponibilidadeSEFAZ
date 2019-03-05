#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from UTIL import Browser, Autorizador, Html

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
	linhas = Html.carrega_tabela(table)
	
	for linha in linhas:
		if str(linha).find(autorizador) != -1:
			result['Autorizador'] = linha[0].text
			result['Autorizacao'] = status(linha[1])
			result['RetornoAutorizacao'] = status(linha[2])
			result['Inutilizacao'] = status(linha[3])
			result['ConsultaProtocolo'] = status(linha[4])
			result['StatusServico'] = status(linha[5])
			result['TempoMedio'] = linha[6].text
			result['ConsultaCadastro'] = status(linha[7]) 
			result['RecepcaoEvento'] = status(linha[8])
	
	return result