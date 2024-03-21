#pip install networkx
import networkx as nx

def func(v):
    g = nx.Graph()
    g.add_nodes_from(range(v))

    for i in range(v):
        for j in range(i+1, v):
            g.add_edge(i,j)
    return g

v = int(input('Digite o número de vértices desejado: '))
grafo = func(v)

print('Vértices do grafo: ',grafo.nodes())
print('Arestas do grafo: ',grafo.edges())