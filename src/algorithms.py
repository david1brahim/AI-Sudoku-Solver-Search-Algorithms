def solve_dfs(env):
    empty = env.find_empty()
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if env.is_valid(row, col, num):
            env.board[row][col] = num
            if solve_dfs(env):
                return True
            env.board[row][col] = 0
    return False
# أضف هذا داخل src/algorithms.py
def get_mrv_cell(env):
    best_cell = None
    min_options = 10
    for r in range(9):
        for c in range(9):
            if env.board[r][c] == 0:
                options = sum(1 for n in range(1, 10) if env.is_valid(r, c, n))
                if options < min_options:
                    min_options = options
                    best_cell = (r, c)
    return best_cell

def solve_astar(env):
    cell = get_mrv_cell(env)
    if not cell: return True
    r, c = cell
    for num in range(1, 10):
        if env.is_valid(r, c, num):
            env.board[r][c] = num
            if solve_astar(env): return True
            env.board[r][c] = 0
    return False
