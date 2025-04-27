"""
Implement A star Algorithm for any game search problem.
"""

import heapq

def astar(start, goal, neighbors_fn, heuristic_fn):
    open_set = [(0 + heuristic_fn(start, goal), 0, start, [])]
    visited = set()
    while open_set:
        est_total, cost, node, path = heapq.heappop(open_set)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor, step_cost in neighbors_fn(node):
            if neighbor not in visited:
                heapq.heappush(open_set, (cost + step_cost + heuristic_fn(neighbor, goal), cost + step_cost, neighbor, path))
    return None

# Example for 2D Grid (no walls)
def neighbors(node):
    x, y = node
    moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    valid = [(nx, ny) for nx, ny in moves if 0 <= nx < 5 and 0 <= ny < 5]
    return [(n, 1) for n in valid]  # cost to move = 1

def heuristic(a, b):  # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Usage
start = (0, 0)
goal = (4, 4)
path = astar(start, goal, neighbors, heuristic)
print("Path found:", path)
