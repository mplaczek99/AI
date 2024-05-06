import random

def count_conflicts(board, row, col, counter):
    conflicts = 0
    for i in range(len(board)):
        if i != row:
            counter[0] += 1 # Count this conflict check
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    conflicts += 1
    return conflicts

def eight_queens_random():
    board = [random.randint(0, 7) for _ in range(8)]
    counter = [0]  # Operation counter
    while True:
        conflicts = [count_conflicts(board, i, board[i], counter) for i in range(8)]
        max_conflicts = max(conflicts)
        if max_conflicts == 0:
            return board, counter[0]
        conflict_indices = [i for i, x in enumerate(conflicts) if x == max_conflicts]
        queen = random.choice(conflict_indices)
        new_col = random.randint(0, 7)
        board[queen] = new_col

def format_chess_notation(board):
    positions = []
    n = len(board)
    for row in range(n):
        column = board[row]
        positions.append(chr(column + ord('a')) + str(n - row))
    return positions

# Run the random placement solution
random_solution, random_work = eight_queens_random()
formatted_positions = format_chess_notation(random_solution)
print("Random Placement Solution: ", formatted_positions)
print("Operations: ", random_work)
