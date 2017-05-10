# 4.1: given a directed graph, design an algorithm to find out whether there is 
#      a route between two nodes.


# 0 : 1
# 1 : 2
# 2 : 0, 3
# 3 : 2

graph = {
  '0': set(['1']),
  '1': set(['2']),
  '2': set(['0', '3']),
  '3': set(['2'])
}


# Use DFS to find path from start to end
# Runtime: O(|V| + |E|)
def isRoute(start, end):
  # Use stack to keep track of nodes during DFS traversal
  stack = []

  # Use hash set to see if we visited the node already
  isVisited = set()

  stack.append(start)
  while stack:
    currentNode = stack.pop()

    # Check if current node is the end node
    if currentNode == end:
      return True
     
    if currentNode not in isVisited:
      # Mark node as visited
      isVisited.add(currentNode)


    stack.extend(graph[currentNode] - isVisited)
  return False

print isRoute('0', '3')