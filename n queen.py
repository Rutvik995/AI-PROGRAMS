def print_board(board, n):
    cell_width = 5

    print("\n       " + "".join(f"{c:^{cell_width}}" for c in range(1, n + 1)))
    print("      +" + "+".join(["-" * cell_width] * n) + "+")

    for r in range(n):
        print(f"  {r + 1:2}  |", end="")
        for c in range(n):
            symbol = "👑" if board[r][c] == 1 else "·"
            print(f"{symbol:^{cell_width}}|", end="")
        print()
        print("      +" + "+".join(["-" * cell_width] * n) + "+")


def is_safe(board, row, col, n):
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                if r == row and c == col:
                    continue

                if (r == row or c == col or
                    abs(r - row) == abs(c - col)):
                    return False
    return True


def can_complete(board, row, n):
    if row == n:
        return True

    # A queen is already fixed in this row
    if 1 in board[row]:
        return can_complete(board, row + 1, n)

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if can_complete(board, row + 1, n):
                board[row][col] = 0
                return True

            board[row][col] = 0

    return False


def main():
    try:
        n = int(input("Enter the size of the chessboard: "))

        if n < 1:
            print("Please enter a positive size.")
            return

        board = [[0] * n for _ in range(n)]
        queens = 0

        print(f"\n{'=' * 35}")
        print(f"       {n}-QUEEN CHALLENGE")
        print(f"{'=' * 35}")
        print("Place one queen in each row and column.")
        print("Enter row and column numbers starting from 1.")

        while queens < n:
            print_board(board, n)
            print(f"\nQueens placed: {queens}/{n}")

            try:
                row = int(input(f"Choose row (1-{n}): ")) - 1
                col = int(input(f"Choose column (1-{n}): ")) - 1
            except ValueError:
                print("Invalid input! Enter numbers only.")
                continue

            if not (0 <= row < n and 0 <= col < n):
                print("Invalid position! Choose a numbered cell on the board.")
                continue

            if board[row][col] == 1:
                print("That cell already contains a queen! Choose an empty cell.")
                continue

            if not is_safe(board, row, col, n):
                print("Unsafe position! Another queen can attack this cell.")
                print("Choose a different position.")
                continue

            # Temporarily place the queen
            board[row][col] = 1

            # Check whether the remaining queens can still be placed
            if not can_complete(board, 0, n):
                board[row][col] = 0
                print("This position blocks a complete solution!")
                print("Queen not fixed. Please choose another position.")
                continue

            queens += 1
            print(f"Queen fixed at Row {row + 1}, Column {col + 1}!")

        print_board(board, n)
        print("\nCongratulations! All queens placed successfully!")

    except ValueError:
        print("Please enter a valid integer for board size.")


if __name__ == "__main__":
    main()  