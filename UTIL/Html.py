from bs4 import BeautifulSoup

def carrega_tabela(html):
    linhasRetorno = []
    linhas = html.findChildren(['tr'])
    for linha in linhas:
        colunas = linha.findChildren('td')
        colunasRetorno = []
        for coluna in colunas:
            colunasRetorno.append(coluna)
        linhasRetorno.append(colunasRetorno)
    
    return linhasRetorno