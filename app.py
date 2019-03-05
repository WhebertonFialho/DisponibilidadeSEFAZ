#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from API import BuscarDisponibilidadeNFe as NFe
from API import BuscarDisponibilidadeNFCe as NFCe
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/nfe/disponibilidade/', methods=['GET'])
def buscar_disponibilidade_nfe():
	versao = request.args.get('versao', default = '4', type=str)
	autorizador = request.args.get('autorizador', default = '', type=str)

	json = NFe.verifica_disponibilidade(versao, autorizador.upper())
	return jsonify(json)

@app.route('/nfce/disponibilidade/', methods=['GET'])
def buscar_disponibilidade_nfce():
	autorizador = request.args.get('autorizador', default='', type=str)
	
	json = NFCe.verifica_disponibilidade(autorizador.upper())
	return jsonify(json)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)