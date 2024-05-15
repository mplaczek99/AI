def is_safe(board, row, col, counter):
    # Check if the column or diagonals already have a queen
    for i in range(row):
        counter[0] += 1  # Count this check for conflicts
        if (
            board[i] == col  # Same column
            or board[i] - i == col - row  # Same major diagonal
            or board[i] + i == col + row  # Same minor diagonal
        ):
            return False
    return True


def solve_queens(board, row, counter):
    if row == len(board):
        return True  # All queens successfully placed

    for col in range(len(board)):
        if is_safe(board, row, col, counter):
            board[row] = col  # Place queen
            if solve_queens(board, row + 1, counter):
                return True  # Solution found, propagate success back up
            board[row] = -1  # Backtrack: Remove queen and try next column

    return False  # No valid position found for this row


def eight_queens_backtracking():
    board = [-1] * 8  # Initialize the board with -1 indicating no queens present
    counter = [0]  # Operation counter
    if solve_queens(board, 0, counter):
        return board, counter[0]
    return (
        [],
        counter[0],
    )  # Return an empty solution if not solvable (though solvable for 8x8)


def format_chess_notation(board):
    positions = []
    n = len(board)
    for row in range(n):
        column = board[row]
        positions.append(chr(column + ord("a")) + str(n - row))
    return positions


# Run the backtracking solution
backtracking_solution, backtracking_work = eight_queens_backtracking()
formatted_positions = format_chess_notation(backtracking_solution)
print("Backtracking Solution: ", formatted_positions)
print("Operations: ", backtracking_work)
