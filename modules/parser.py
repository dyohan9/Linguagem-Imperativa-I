import sys
from modules.lexer import analise_lexica, tokens_da_linguagem
from modules.simbolos import adicionarFuncao, appendDict


class Parser:
    def __init__(self):
        self.construcoes = [
            (['VAR', 'IGUAL', 'DICIONARIO_ABRE', 'DICIONARIO_FECHA', 'SEPARADOR'], 'DICIONARIO'),
            (['APPEND', 'ABRIR', 'VAR', 'SEPARADOR_DICT', 'VAR', 'SEPARADOR_DICT', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'Append'),
            (['VAR', 'IGUAL', 'VAR', 'SEPARADOR'], 'AtrSimples'),
            (['VAR', 'IGUAL', 'DIGITO', 'SEPARADOR'], 'AtrSimples'),
            (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
            (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
            (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
            (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
            (['IMPRIMIR', 'ABRIR', 'VAR', 'FECHAR', 'SEPARADOR'], 'Imprimir'),
            (['VAR', 'ABRIR', 'FECHAR', 'SEPARADOR'], 'Funcao'),
        ]

    def consumirTokens(self, tokens, pos):
        indice = pos
        for construcao in self.construcoes:
            for token in construcao[0]:
                # print(tokens[indice][1])
                if token != tokens[indice][1]:
                    indice = pos
                    break
                else:
                    indice = indice + 1
            if indice != pos:
                return (indice, construcao[1])
        return (pos, None)

    def analise_sintatica(self, tokens):
        pos = 0
        programa = []
        while pos < len(tokens):

            lookAhead = pos + 3
            if lookAhead < len(tokens):
                inicio = pos

                if tokens[lookAhead][1] == 'ABRIR_FUNC':
                    termino = lookAhead
                    while tokens[termino][1] != 'FECHAR_FUNC':
                        termino = termino + 1

                    blocos = []
                    pos = pos + 4
                    while pos < termino:
                        posAtual, construcao = self.consumirTokens(tokens, pos)
                        if pos != posAtual:
                            blocos.append((str(pos) + '-' + str(posAtual-1), construcao))
                            pos = posAtual
                        else:
                            sys.stderr.write('Problema na funcao: %s\n' % pos)
                            sys.exit(1)
                    adicionarFuncao(tokens[inicio][0], blocos)

                    pos = pos + 1
                    posAtual = pos

                print("teste: " + str(tokens))
                print("teste2: " + tokens[inicio-9][0])

                if tokens[lookAhead-1][1] == 'DICIONARIO_ABRE':
                    termino = lookAhead-1

                    while tokens[termino][1] != 'DICIONARIO_FECHA':
                        # print("entrou")
                        termino = termino + 1

                    blocos = []
                    pos = pos + 4
                    while pos < termino:
                        posAtual, construcao = self.consumirTokens(tokens, pos)
                        if pos != posAtual:
                            blocos.append((str(pos) + '-' + str(posAtual-1), construcao))
                            pos = posAtual
                        else:
                            sys.stderr.write('Problema na leitura do dicionario: %s\n' % pos)
                            sys.exit(1)
                    # print(tokens[inicio-9][0])
                    appendDict(tokens[inicio-9][0], blocos)

                    pos = pos + 1
                    posAtual = pos

            if pos < len(tokens):
                posAtual, construcao = self.consumirTokens(tokens, pos)
                # print(construcao)
                if pos != posAtual:
                    programa.append((str(pos) + '-' + str(posAtual-1), construcao))
                    pos = posAtual
                else:
                    sys.stderr.write('Problema no programa: %s\n' % pos)
                    sys.exit(1)
        return programa
