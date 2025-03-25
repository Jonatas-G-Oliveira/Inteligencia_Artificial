import collections.abc
collections.Mapping = collections.abc.Mapping
from pyknow import *


class RapNacional(KnowledgeEngine):
    #Classificacoes Gerais
    @Rule(AND(Fact('violao'), Fact('poesia')))
    def acustico(self):
        self.declare(Fact('acustico'))

    @Rule(OR(Fact(integrantes=4), Fact(Integrantes=5), Fact(integrantes=6)))
    def grupo(self):
        self.declare(Fact('grupo'))

    @Rule(Fact(integrantes=1))
    def solo(self):
        self.declare(Fact('individual'))

    @Rule(AND(Fact('hip hop'), Fact('antigo')))
    def lendas(self):
        self.declare(Fact('lendas'))

    #Classificacoes Especificas
    @Rule(Fact('lendas'), Fact('grupo'))
    def racionais(self):
        self.declare(Fact(rap='Racionais'))

    @Rule(Fact('lendas'), Fact('individual'), Fact(tag='lab fantasma'))
    def emicida(self):
        self.declare(Fact(rap='Emicida'))

    @Rule(Fact('lendas'), Fact('individual'), Fact('brooklyn'))
    def sabotage(self):
        self.declare(Fact(rap='Sabotage'))

    @Rule(Fact('grupo'), Fact('acustico'), Fact(tag='pineapple'))
    def poesia(self):
        self.declare(Fact(rap='Poesia Acustica'))

    @Rule(Fact('grupo'), Fact('violao'), Fact(tag='grito'))
    def grito(self):
        self.declare(Fact(rap='Grito Acustico'))

    @Rule(Fact('trap'),
          Fact('rock'),
          Fact('funk'),
          Fact('agressivo'))
    def major(self):
        self.declare(Fact(rap='Major RD'))

    def declaracao_fatos(self, lista_argumentos):
        for argumentos in lista_argumentos:
            self.declare(argumentos)

    @Rule(Fact(rap=MATCH.r))
    def print_result(self, r):
        print('O grupo é: {} '.format(r))


def main():
    print("Classificando Raps")
    RAP = RapNacional()
    RAP.reset()
    #RAP.declaracao_fatos([Fact(integrantes=6), Fact('violao'), Fact('poesia'), Fact(tag='pineapple')])
    #RAP.declaracao_fatos([Fact('antigo'), Fact('hip hop'), Fact(integrantes=4)])
    #RAP.declaracao_fatos([Fact('antigo'), Fact('hip hop'), Fact(integrantes=1), Fact(tag='lab fantasma')])
    RAP.run()
    print(RAP.facts)


main()