#  17.Create an undirected graph with the following edges:
# * A – B
# * A – C
# * B – D
# * C – D
# Display the adjacency list of the graph.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for vertex in graph:
    print(vertex, ":", graph[vertex])