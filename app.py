from API import BuscarDisponibilidadeNFe as NFe
from API import BuscarDisponibilidadeNFCe as NFCe
from flask import Flask, jsonify, request, render_template
from flask_bootstrap import Bootstrap
from forms import forms as NF
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'development key'
bootstrap = Bootstrap(app)

#PAGINAS
@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NF.NFConsultaForm()
	if request.method == 'POST':
		tipo = form.tipo.data
		estado = form.estados.data
		if tipo == 'nfe':
			nfe = NFe.verifica_disponibilidade('4', estado.upper())
			return render_template('nfe.html', data=nfe)
		else:
			nfce = NFCe.verifica_disponibilidade(estado.upper())
			return render_template('nfce.html', data=nfce)
	elif request.method == 'GET':
		return render_template('index.html', form=form)

@app.route('/api')
def api():
    return render_template('api.html')
	
#API	
@app.route('/nfe/', methods=['GET'])
def buscar_disponibilidade_nfe():
	versao = request.args.get('versao', default = '4', type=str)
	autorizador = request.args.get('autorizador', default = '', type=str)

	json = NFe.verifica_disponibilidade(versao, autorizador.upper())
	return jsonify(json)


@app.route('/nfce/', methods=['GET'])
def buscar_disponibilidade_nfce():
	autorizador = request.args.get('autorizador', default='', type=str)
	
	json = NFCe.verifica_disponibilidade(autorizador.upper())
	return jsonify(json)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)