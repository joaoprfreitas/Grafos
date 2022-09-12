######################################
#
# Nome: João Pedro Rodrigues Freitas
# N USP: 11316552
#
######################################

from graph import Graph

fileName = input() # Lê o nome do arquivo

graph = Graph(fileName)

print("S") if graph.hasCycle() else print("N")
