import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs_recursive
from collections import deque
from dfs import dfs_recursive

#Завдання 1
G = nx.Graph()
routes = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
} #маршрути між зупинками

for stop, connections in routes.items():
    for connection in connections:
        G.add_edge(stop, connection)

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = G.degree()
print('кількість вузлів у графі: ', num_nodes)
print('кількість ребер у графі: ', num_edges)
print('вершина та її ступінь ', degrees)

#Завдання 2
print('BFS: ')
bfs_recursive(routes, deque(["A"]))
print('\nDFS: ')
dfs_recursive(routes, 'A')
print('\n')
#Завдання 3
routes = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('D', 1), ('E', 1)],
    'C': [('A', 1), ('F', 1)],
    'D': [('B', 1)],
    'E': [('B', 1)],
    'F': [('C', 1)]
}
for stop, connections in routes.items():
    for connection, weight in connections:
        G.add_edge(stop, connection, weight=weight)

source = 'E'
target = 'D'
shortest_path = nx.dijkstra_path(G, source, target, weight='weight')
shortest_path_length = nx.dijkstra_path_length(G, source, target, weight='weight')

print(f"Найкоротший шлях від {source} до {target}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length}")