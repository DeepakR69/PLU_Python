# 18.Check whether there is a direct edge between two given vertices.
u = input("Enter first vertex: ")
v = input("Enter second vertex: ")

if v in graph[u]:
    print("Direct Edge Exists")
else:
    print("No Direct Edge")