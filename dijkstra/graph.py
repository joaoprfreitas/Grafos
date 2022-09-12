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

            if len(edge) == 2: # grafo sem pesos
                self.graph[edge[0]].append(edge[1])
            elif len(edge) == 3: # grafo com pesos
                self.graph[edge[0]].append([edge[1], edge[2]])
            
            # Adiciona o caminho reverso se o grafo não for direcionado
            if not self.directed:
                if edge[1] not in self.graph:
                    self.graph[edge[1]] = []

                if len(edge) == 2: # grafo sem pesos
                    self.graph[edge[1]].append(edge[0])
                elif len(edge) == 3: # grafo com pesos
                    self.graph[edge[1]].append([edge[0], edge[2]])

        # Ordena a lista de adjacências de cada nó
        for edge in self.graph:
            self.graph[edge].sort()

        # Ordena os nós
        self.graph = dict(sorted(self.graph.items()))


    def getGraph(self):
        return self.graph

    def getNumNodes(self):
        return self.numNodes

    # Algoritmo de dijkstra a partir de um nó inicial
    def dijkstra(self, start):
        dist = [] # distancia
        prev = [] # antecessor
        priorityQueue = [] # fila de prioridade

        # Inicializa a distância de todos os nós como infinito
        # Inicializa o antecessor de todos os nós como None
        # Insere na lista de prioridade o nó inicial
        def initialize(start):
            for i in range(self.getNumNodes()):
                dist.append(sys.maxsize)
                prev.append(None)

            dist[int(start) - 1] = 0 # Distância do nó inicial é 0
            priorityQueue.append([0, start])

        # Realiza o relaxamento do nó vizinho a 'u'
        def relax(u, node):
            v = node[0] # numero do nó
            weight = node[1] # peso do nó

            if dist[v - 1] > dist[u - 1] + weight: # Relaxamento
                dist[v - 1] = dist[u - 1] + weight
                prev[v - 1] = u
                priorityQueue.append([dist[v - 1], v]) # Atualiza lista de prioridade
                priorityQueue.sort(key=lambda x: x[0]) # Ordena a lista de prioridade

        initialize(start) # Inicializa as variveis

        # Enquanto houver nós na lista de prioridade
        while len(priorityQueue) != 0:
            u = priorityQueue.pop(0)[1] # nó atual

            for node in self.graph[u]: # Para cada vizinho
                relax(u, node)
                
        return dist, prev


        
