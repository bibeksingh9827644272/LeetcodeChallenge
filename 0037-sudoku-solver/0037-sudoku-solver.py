class Solution:
    def solveSudoku(self, board):
        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack():
            best_row = -1
            best_col = -1
            best_nums = None

            # Find the empty cell with the fewest choices
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        possible = []

                        for num in "123456789":
                            if isValid(row, col, num):
                                possible.append(num)

                        # No number can be placed here
                        if len(possible) == 0:
                            return False

                        # Choose the cell with minimum choices
                        if best_nums is None or len(possible) < len(best_nums):
                            best_nums = possible
                            best_row = row
                            best_col = col

                            # Only one choice - best possible case
                            if len(best_nums) == 1:
                                break

                if best_nums is not None and len(best_nums) == 1:
                    break

            # No empty cells -> Sudoku solved
            if best_nums is None:
                return True

            # Try possible numbers
            for num in best_nums:
                board[best_row][best_col] = num

                if backtrack():
                    return True

                # Undo
                board[best_row][best_col] = "."

            return False

        backtrack()