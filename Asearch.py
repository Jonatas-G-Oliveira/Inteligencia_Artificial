# Seleciona o item de acordo com o menor custo
from queue import PriorityQueue

from pyamaze import maze, agent


#Estimativa de quantos passos ate chegar ao final
def h_score(celula, destino):
    linhac = celula[0]
    colunac = celula[0]
    linhad = destino[0]
    colunad = destino[1]
    return abs(colunac - colunad) + abs(linhac - linhad)

# Quantos passos eu já andei
def g_score(celula, origem):
    linhaC = celula[0]
    colunaC = celula[1]
    linhaO = origem[0]
    colunaO = origem[1]
    return linhaO - linhaC + colunaO - colunaC


def aStar(labirinto):
    destino = (1, 1)
    origem = (labirinto.rows, labirinto.cols)
    caminho = {}

    #Criar o tabuleiro com o f_score infito
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    g_score[origem] = 0

    #Calcular o valor da celula inicial
    f_score[origem] = g_score[origem] + h_score(origem, destino)

    #Criando uma estrura de dados
    fila = PriorityQueue()
    item = (f_score[origem], h_score(origem, destino), origem)
    fila.put(item)


    while not fila.empty():
        celula = fila.get()[2]



        if celula == destino:
            break

        for direcao in "NSEW":
            if labirinto.maze_map[celula][direcao] == 1:
                linha_celula = celula[0]
                coluna_celula = celula[1]
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                if direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                if direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)
                if direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)

                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score((proxima_celula), destino)

                if(novo_f_score < f_score[proxima_celula]):
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score((proxima_celula), destino), proxima_celula)
                    fila.put(item)
                    caminho[proxima_celula] = celula #Vai ter todas as celulas que foram passadas

    caminho_final = {}
    celula_analisada = destino
    while celula_analisada != origem:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]
    return caminho_final

    #Caminhar a partir da celula inicial explorando os proximos caminhos
       #Para cada possibilidade de caminho
          # Se o caminho é possível (Não tem parede)
          # Se o caminho for possível
             # calcular o f_score dos caminhos possíveis
             # se o f_score calculado < f_score antigo do caminho
                # substituir o f_score antigo pelo calculado
                # escolher o caminho para seguir que tem:
                    # O menor f_score
                    # Se os f_score for igual escolher o que tem menor h_score


    print(f_score)
    return caminho


def main():

    labirinto = maze()
    labirinto.CreateMaze()
    agente = agent(labirinto, filled=True, footprints=True)

    caminho = aStar(labirinto)
    print(caminho)
    labirinto.tracePath({agente: caminho}, delay=300)
    labirinto.run()
main()