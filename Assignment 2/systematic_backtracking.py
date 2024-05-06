def is_safe(board, row, col, counter):
    for i in range(row):
        counter[0] += 1  # Count this check for conflicts
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_queens(board, row, counter):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col, counter):
            board[row] = col
            if solve_queens(board, row + 1, counter):  # Detects if queen is present
                return True
            board[row] = -1  # Backtrack
    return False


def eight_queens_backtracking():
    board = [-1] * 8
    counter = [0]  # Operation counter
    if solve_queens(board, 0, counter):
        return board, counter[0]
    return [], counter[0]


def format_chess_notation(board):
    positions = []
    n = len(board)
    for row in range(n):
        column = board[row]
        positions.append(chr(column + ord('a')) + str(n - row))
    return positions


# Run the backtracking solution
backtracking_solution, backtracking_work = eight_queens_backtracking()
formatted_positions = format_chess_notation(backtracking_solution)
print("Backtracking Solution: ", formatted_positions)
print("Operations: ", backtracking_work)
