######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
# Exercício: Busca em largura (BFS)
#
######################################

import sys

class Pajek():
    
    def __init__(self):
        string = sys.stdin.read().split('\r\n') # faz a leitura da entrada no formato pajek

        # armazena o número de nós
        aux = string[0].split(' ')
        self.numNodes = int(aux[1])

        self.edges = []

        # armazena as arestas
        for i in range(2, len(string)):
            if (string[i] != ''): # Verifica se a linha não é vazia
                aux = string[i].split(' ')
                self.edges.append([int(aux[0]), int(aux[1])])
        

    def getEdges(self):
        return self.edges

    def getNumNodes(self):
        return self.numNodes