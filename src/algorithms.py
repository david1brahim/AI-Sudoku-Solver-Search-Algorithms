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
