class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        # Frequency pruning
        count = {}
        for row in board:
            for ch in row:
                count[ch] = count.get(ch, 0) + 1

        need = {}
        for ch in word:
            need[ch] = need.get(ch, 0) + 1

        for ch in need:
            if count.get(ch, 0) < need[ch]:
                return False

        # Start from the rarer character
        if count.get(word[0], 0) > count.get(word[-1], 0):
            word = word[::-1]

        length = len(word)

        def dfs(r, c, i):
            if i == length:
                return True

            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            if board[r][c] != word[i]:
                return False

            # Mark visited
            temp = board[r][c]
            board[r][c] = '#'

            # Search four directions
            if (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)):
                
                board[r][c] = temp
                return True

            # Backtrack
            board[r][c] = temp
            return False

        # Try every starting cell
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False