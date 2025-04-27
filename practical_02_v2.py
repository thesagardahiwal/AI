"""
Implement A star Algorithm for any game search problem.
"""

import heapq

def astar(start, goal, graph, heuristic):
    open_set = [(heuristic[start], 0, start, [])]
    visited = set()
    while open_set:
        est_total, cost, node, path = heapq.heappop(open_set)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor, step_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_set, (cost + step_cost + heuristic[neighbor], cost + step_cost, neighbor, path))
    return None

# Graph with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Predefined heuristic values for each node
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

# Usage
path = astar('A', 'G', graph, heuristic)
print("Path found:", path)
