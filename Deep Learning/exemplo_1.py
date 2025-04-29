### IMPORTS

import torch
import numpy as np
import torch.distributions.uniform as urand #Numero aleatórios
from torch import nn
import torch.utils.data.dataloader as dataloader
import torch.utils.data.dataset as dataset


###
# we gon represent a line using a neuron
###

#We will inherit a super class function form PyTorch
class RedeLinear(nn.Module):
    # We need to assign the Super Class
    def __init__(self):
        super().__init__()

        #Alocating 1 neuron that uses 1 entry and gives 1 result
        self.layers = nn.Sequential(
            nn.Linear(1,1)
        )

    # this function takes an entry and pass to a function that's compute an entry
    def foward(self, entry_info):
        return self.layers(entry_info)


class AlgebraicDataset(dataset):
    #Função,intervalo e número de amostras
    def __init__(self, function, interval, nsamples):
        X = urand.Uniform(interval[0], interval[1]).sample([nsamples])
        self.data = [(x , function(x)) for x in X]
        pass

    #Tamanho do conjunto de dados
    def __len__(self):
        return len(self.data)

    #Retorna o item de acordo com o indice passado
    def __getitem__(self,idx):
        return self.data[idx]

def main():
    print("Testando rede linear")

    line = lambda x: 2*x + 3
    intervalo = (-10, 10)
    train_nsamples = 1000
    test_nsamples = 100

    train_dataset = AlgebraicDataset(line, intervalo, train_nsamples)
    test_dataset = AlgebraicDataset(line, intervalo, test_nsamples)

    train_dataloader = dataloader (train_dataset, train_nsamples, shuffle = True)

main()