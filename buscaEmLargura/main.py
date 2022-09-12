######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
# Exercício: Busca em largura (BFS)
#
######################################

from graph import Graph

g = Graph()
matrix = g.distanceMatrix()

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=' ')
    print()
