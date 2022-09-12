######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
#
######################################

from graph import Graph

fileName = input() # Lê o nome do arquivo

graph = Graph(fileName)

matrix = []
for i in range(graph.getNumNodes()): # Realiza o algoritmo de Dijkstra em cada nó
    line, prev = graph.dijkstra(i + 1)
    matrix.append(line)

maxColumnList = list(map(max, zip(*matrix))) # Lista com os valores máximos por coluna
maxColumnList = list(map(lambda x: len(str(x)), maxColumnList)) # Lista com o max de digitos por coluna

for i in range(graph.getNumNodes()):
    for j in range(graph.getNumNodes()):
        print(f'{matrix[i][j]:>{maxColumnList[j]}}', end=' ') # Printa a matriz com os espaços necessários para alinhar os valores
    print()
