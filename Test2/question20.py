
# 20.Perform a Depth-First Search (DFS) traversal starting from vertex A.
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfs(i)

dfs('A')