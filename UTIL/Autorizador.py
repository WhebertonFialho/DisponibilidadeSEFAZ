AUTORIZADOR = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','SVAN', 'SVRS', 'SVC-AN', 'SVC-RS']

SVAN = ['MA', 'PA']
SVRS = ['AC', 'AL', 'AP', 'DF', 'ES', 'PB', 'PI', 'RJ', 'RN', 'RO', 'RR', 'SC', 'SE', 'TO']
VIRTUAL_RS = ['RO', 'AC', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'RN', 'PB', 'AL', 'SE', 'BA', 'ES', 'RJ', 'DF']

ESTADOS = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goias',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

def existe_versao_nfe(versao):
    if versao == '4' or versao == '3':
        return True
    else: 
        return False;

def existe_autorizador(autorizador):
    return autorizador in AUTORIZADOR

def pega_autorizador_nfe(autorizador):
    if autorizador in SVAN:
        return "SVAN"
    elif autorizador in SVRS:
        return "SVRS"
    else:
        return autorizador

def pega_autorizador_nfce(autorizador):
    if autorizador in VIRTUAL_RS:
        return "Virtual RS"
    else:
        return pega_nome_estado(autorizador)

def pega_nome_estado(sigla):
    return ESTADOS[sigla]