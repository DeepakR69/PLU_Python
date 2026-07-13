
# 19.Perform a Breadth-First Search (BFS) traversal starting from vertex A

from collections import deque

visited = set()
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])

