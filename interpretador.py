from modules.lexer import analise_lexica, tokens_da_linguagem
from modules.parser import Parser
from modules.ast import AtrSimples, Imprimir, Funcao, instaciarConstrucoes


class Run:
    def __init__(self):
        # self.code = '''
        #
        # B = 10;
        # C = [];
        # test(){
        #     A = B + 10;
        #     B = A;
        # }
        #
        # test();
        #
        # test();
        #
        # imprimir(A);
        #
        # '''

        self.code = '''
                A = [];
                append(A-teste-1);
                 
                imprimir(B);
                '''


        self.run()

    def run(self):
        tokens = analise_lexica(self.code, tokens_da_linguagem)
        # print(tokens)

        programa = Parser().analise_sintatica(tokens)
        print(programa)

        instanciasContrucoes = instaciarConstrucoes(programa, tokens)
        for insConst in instanciasContrucoes:
            insConst.interpretar()


if __name__ == "__main__":
    Run()
