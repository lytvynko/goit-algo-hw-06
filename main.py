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
for stop, connections in routes.items():
    for connection in connections:
        G.add_edge(stop, connection, weight=1)

def convert_graph_to_dict(graph):
    graph_dict = {}
    for node in graph.nodes():
        graph_dict[node] = {}
        for neighbor, attrs in graph[node].items():
            graph_dict[node][neighbor] = attrs['weight']
    return graph_dict

graph_dict = convert_graph_to_dict(G)        

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[start] = 0
    vertices = deque(graph)

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)

        for neighbour, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight
           
            if alternative_route < distances[neighbour]:
                distances[neighbour] = alternative_route
                previous_vertices[neighbour] = current_vertex

    return distances, previous_vertices
 
distances, _ = dijkstra(graph_dict, 'A')
print(f'Відстань від А: {distances}')
