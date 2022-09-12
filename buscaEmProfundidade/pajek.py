######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
#
######################################

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
                self.edges.append([int(aux[0]), int(aux[1])])
        

    def getEdges(self):
        return self.edges

    def getNumNodes(self):
        return self.numNodes

    def isDirected(self):
        return self.directed