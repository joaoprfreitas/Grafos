######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
# Exercício: Busca em largura (BFS)
#
######################################

import sys
from pajek import Pajek

class Graph():

    def __init__(self):
        pajek = Pajek()
        self.numNodes = pajek.getNumNodes()
        self.graph = {}

        # Cria o grafo no formato de lista de adjacências
        # Se um nó não estiver no grafo, ele é adicionado
        # Para cada nó, é adicionado uma lista de adjacências com os nós vizinhos
        for edge in pajek.getEdges():
            if edge[0] not in self.graph:
                self.graph[edge[0]] = []
            if edge[1] not in self.graph:
                self.graph[edge[1]] = []

            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    def getGraph(self):
        return self.graph

    def getNumNodes(self):
        return self.numNodes

    # Realiza a busca em largura, passando o nó inicial como parâmetro
    def BFS(self, start):
        d = [] # distance
        white = [] # list
        gray = [start] # queue
        black = [] # list

        # Adiciona na lista branca todos os nós do grafo, exceto o inicial
        for key in self.graph:
            if key != start:
                white.append(key)

        # Seta as distâncias de todos os nós como infinito
        for i in range(self.getNumNodes()):
            d.append(sys.maxsize)

        d[int(start) - 1] = 0 # A distância do nó inicial em relação a si mesmo é 0
        
        # Enquanto a lista cinza não estiver vazia, ou seja, enquanto houver nós a serem visitados
        while len(gray) != 0:
            black.append(gray[0])
            node = gray.pop(0)

            # Busca os vizinhos do nó atual
            for neighbour in self.graph[node]:
                if neighbour in white:
                    white.remove(neighbour)
                    gray.append(neighbour)
                    d[int(neighbour) - 1] = d[int(node) - 1] + 1 # Incrementa a distância do vizinho em relação ao nó atual

        return black, d
        
    # Realiza a busca em largura de todos os vértices, retornando
    # a matriz de distâncias
    def distanceMatrix(self):
        d = []
        
        for i in self.graph:
            tupleAux = self.BFS(i)
            d.append(tupleAux[1])

        return d