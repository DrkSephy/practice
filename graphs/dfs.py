graph = {
  0: [1, 5],
  1: [0, 2, 3],
  2: [1, 4],
  3: [1, 4, 5],
  4: [2, 3, 5],
  5: [0, 3, 4]
}

def dfs(graph, root):
  visited = []
  stack = [root]

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      stack.extend([x for x in graph[node] if x not in visited])
  return visited

print dfs(graph, 0)