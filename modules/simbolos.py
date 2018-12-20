tabela = {}
funcoes = {}

dicionario = {}

def adicionar(nome, valor):
    tabela[nome] = valor

def ler(nome):
    return tabela[nome]

def adicionarFuncao(nome, comandos):
    funcoes[nome] = comandos

def lerFuncao(nome):
    return funcoes[nome]

def appendDict(nome, comandos):
    dicionario[nome] = comandos

def getDict(nome):
    return dicionario[nome]