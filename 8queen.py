def print_board(queens):
    for row in range(8):
        line = ""
        for col in range(8):
            if queens[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def is_safe(queens, row, col):
    for r in range(row):
        if queens[r] == col or \
           queens[r] - r == col - row or \
           queens[r] + r == col + row:
            return False
    return True

def solve(queens, row=0):
    if row == 8:
        print_board(queens)
        print()
        return  # Print one solution and continue to find others

    for col in range(8):
        if is_safe(queens, row, col):
            queens[row] = col
            solve(queens, row + 1)
            queens[row] = -1  # Backtrack

# Initialize the queens array to indicate no queens are placed (-1)
queens = [-1] * 8
solve(queens)
