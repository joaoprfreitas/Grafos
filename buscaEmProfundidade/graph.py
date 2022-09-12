######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
#
######################################

import sys
from pajek import Pajek

class Graph():

    def __init__(self, path):
        pajek = Pajek(path)

        self.numNodes = pajek.getNumNodes()
        self.graph = {}
        self.directed = pajek.isDirected()
        self.cycle = False

        # Cria o grafo no formato de lista de adjacências
        # Se um nó não estiver no grafo, ele é adicionado
        # Para cada nó, é adicionado uma lista de adjacências com os nós vizinhos
        for edge in pajek.getEdges():
            if edge[0] not in self.graph:
                self.graph[edge[0]] = []

            self.graph[edge[0]].append(edge[1])
            
            # Adiciona o caminho reverso se o grafo não for direcionado
            if not self.directed:
                if edge[1] not in self.graph:
                    self.graph[edge[1]] = []

                self.graph[edge[1]].append(edge[0])

        # Ordena a lista de adjacências de cada nó
        for edge in self.graph:
            self.graph[edge].sort()


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

    # Realiza a busca em profundidade a partir de um determinado nó,
    # retornando uma lista com os nós percorridos, a lista com nós não percorridos
    # e uma flag para indicar a existência ou não ciclos.
    # É opcional a passagem da lista branca a ser percorrida.
    def DFS(self, start, whiteList = None):
        white = [] # list

        # Verifica se a lista branca foi passada
        if whiteList != None:
            white = whiteList

        gray = [] # stack
        black = [] # list

        # Adiciona na lista branca todos os nós do grafo se não houver nós na lista branca
        if len(white) == 0:
            for node in self.graph:
                white.append(node)

        # Passo recursivo da DFS
        def recursiveDFS(node):
            white.remove(node)
            gray.append(node)

            # Percorre todos os vizinhos de um determinado nó
            for neighbour in self.graph[node]:
                if neighbour in white:
                    recursiveDFS(neighbour)
                elif neighbour in gray and neighbour != node: # se o vizinho não for pai e estiver cinza, há ciclo
                    self.cycle = True

            # Não há mais nós brancos, então o nó atual é preto
            gray.pop() # Remove o elemento mais recente da pilha
            black.append(node)

        
        recursiveDFS(start)

        return black, white

    # Realiza a busca em profundidade até que todos os vértices tenham sido percorridos
    # Retorna uma lista com os nós percorridos em cada componente do grafo
    def getConnectedComponentList(self):
        startNode = list(self.graph.keys())[0] # Primeiro nó do grafo
        white = [] # list
        componentList = []

        # Loop infinito até percorrer todos os nós do grafo
        while True:
            black, white = self.DFS(startNode, white)
            componentList.append(black)

            if len(white) == 0: break # Se todos os nós foram percorridos, sai do loop

            startNode = white[0] # Se não, realiza a busca em profundidade a partir do primeiro nó da lista branca

        return sorted(componentList, key=len, reverse=True)

    # Retorna uma lista com os nós percorridos em cada componente do grafo,
    # retornando true se houver ciclo e false se não houver
    def hasCycle(self):
        startNode = list(self.graph.keys())[0] # Primeiro nó do grafo
        white = [] # list

        # Loop infinito até percorrer todos os nós do grafo
        while True:
            black, white = self.DFS(startNode, white)

            if len(white) == 0 or self.cycle: break # Se todos os nós foram percorridos ou achou um ciclo, sai do loop

            startNode = white[0] # Se não, realiza a busca em profundidade a partir do primeiro nó da lista branca

        return self.cycle

