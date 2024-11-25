def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))

graph = {i: [] for i in range(num_nodes)}

print("Enter each edge (start and end node, separated by space):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  

start_node = int(input("Enter the starting node: "))

print("DFS traversal starting from node", start_node, ":")
dfs(graph, start_node)
