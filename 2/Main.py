######################################
#
# Nome: João Pedro Rodrigues Freitas, 11316552
# Nome: Rafael Kuhn Takano, 11200459
#
######################################

import sys

class Pajek():
    def __init__(self, path):
        f = open(path, 'r')

        string = f.read().replace('/\r\n/g', '\n').split('\n') # faz a leitura da entrada no formato pajek
        
        f.close()

        # armazena o número de nós
        aux = string[0].split(' ')
        self.numNodes = int(aux[1])

        # verifica se o grafo é direcionado
        if (string[1] == '*Arcs'):
            self.directed = True
        else:
            self.directed = False

        self.edges = []

        # armazena as arestas
        for i in range(2, len(string)):
            if (string[i] != ''): # Verifica se a linha não é vazia
                aux = string[i].split(' ')
                if len(aux) == 2: # Grafo sem pesos
                    self.edges.append([int(aux[0]), int(aux[1])])
                elif len(aux) == 3: # Grafo com pesos
                    self.edges.append([int(aux[0]), int(aux[1]), int(aux[2])])
        
    def getEdges(self):
        return self.edges

    def getNumNodes(self):
        return self.numNodes

    def isDirected(self):
        return self.directed

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

    # Retorna o grafo
    def getGraph(self):
        return self.graph

    # Retorna o número de nós do grafo
    def getNumNodes(self):
        return self.numNodes

    # Obtém a árvore geradora mínima do grafo por meio do algoritmo de Prim
    # Retorna uma lista de arestas com os pesos
    def primMST(self, start):
        parent = []

        # Inicia o vetor de pai com arrays [None, 0] para cada nó
        for i in range(self.numNodes):
            parent.append([None, 0])

        H = [] # Lista de prioridade

        # Preenche a lista com os valores iniciais
        for i in range(self.numNodes):
            if i + 1 == start:
                H.append([0, start])
            else:
                H.append([sys.maxsize, i + 1])

        # Retorna a posição do nó na lista de prioridade
        def getPosInH(H, node):
            for i in H:
                if i[1] == node:
                    return i
            return None

        while len(H) > 0:
            H.sort(key=lambda x: x[0]) # Ordena a lista de acordo com os pesos
            u = H.pop(0) # Remove o nó com o menor peso
            
            for v in self.graph[u[1]]: # Para cada vértice v adjacente a u
                if list(filter(lambda x: x[1] == v[0], H)) != []: # se v está na heap
                    if v[1] < getPosInH(H, v[0])[0]: # Se o peso de v for menor que o peso do nó na heap
                        getPosInH(H, v[0])[0] = v[1] # Atualiza o peso do nó na heap
                        parent[v[0] - 1][1] = v[1] # Atualiza o peso na lista de pai
                        
                    parent[v[0] - 1][0] = u[1] # Atualiza o pai do nó v

        return parent # Retorna a lista de arestas com os pesos
        

if __name__ == "__main__":
    fileName = input() # Lê o nome do arquivo

    graph = Graph(fileName) # Cria o grafo

    list = graph.primMST(1) # Chama o algoritmo de Prim, retornando a lista de arestas com os pesos

    soma = 0
    for pos in list: # Soma os pesos das arestas
        soma += pos[1]

    print(soma)