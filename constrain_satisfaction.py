"""
Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
Backtracking for n-queens problem or a graph coloring problem.
"""


def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            line = '.' * col + 'Q' + '.' * (n - col - 1)

            backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}, board + [line])

    solutions = []
    backtrack(0, set(), set(), set(), [])
    return solutions

# Usage
n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    for row in sol:
        print(row)
    print()

