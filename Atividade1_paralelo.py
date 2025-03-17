import networkx as nx
import matplotlib.pyplot as plt


def criarArvore():
    print('Criando Árvore')
    arvore = {
        'SP'  : ['RJ', 'SSA', 'AJU', 'FOR', 'MAO', 'POA'],
        'RJ'  : ['SP', 'POA', 'AJU', 'CGB'],
        'CWB' : ['CGR', 'FLN'],
        'FLN' : ['CWB', 'SP', 'CGB'],
        'POA' : ['RJ', 'SP'],
        'BHZ' : ['AJU'],
        'SSA' : ['AJU', ],
        'CGR' : [],
        'CGB' : [],
        'AJU' : ['SSA', 'BHZ', 'CGR'],
        'FOR' : ['AJU', 'SP'],
        'MAO' : [],
    }

    return arvore


#Declaração do tipo grafo
def criarGrafo(arvore):
    print('Criando grafo')
    G = nx.MultiDiGraph()

    distancias = {
        ('SP', 'RJ'): 26,
    }


    for cidadeSaida, cidadeEntrada in arvore.items():
        for cidade in cidadeEntrada:
            G.add_edge(cidadeSaida, cidade, peso=1)

    return G


def imprimirGrafo(G):
    print('imprimindo o Grafo')
    plt.figure(1)
    pos = nx.shell_layout(G)
    pesos = nx.get_edge_attributes(G, 'peso')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos,font_size=5)
    nx.draw(G, pos, with_labels=True, arrows=True, font_size=10, node_color='lightblue', node_size=2000)
    plt.show()


def main():
    print('Grafo de testes na matéria de IA')
    arvore = criarArvore()
    G = criarGrafo(arvore)
    imprimirGrafo(G)


main()