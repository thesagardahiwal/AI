"""
Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
structure.
"""

from collections import deque

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Depth First Search (Recursive)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Breadth First Search (Using Queue)
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
print("DFS traversal:")
dfs(graph, 'A')
print("\nBFS traversal:")
bfs(graph, 'A')
