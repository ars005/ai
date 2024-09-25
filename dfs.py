graph={
'A':set(['B','C','G']),
'B':set(['A','D','E']),
'C':set(['A','F','H']),
'D':set(['B']),
'E':set(['B','F']),
'F':set(['C','E','H']),
'G':set(['A']),
'H':set(['C','F'])
}

def dfs(graph,node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
        return visited
visited = dfs(graph,'A', [])
print(visited)