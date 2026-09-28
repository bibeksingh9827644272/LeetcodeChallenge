from collections import Counter

class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        # Frequency pruning
        board_freq = Counter()
        for row in board:
            board_freq.update(row)

        word_freq = Counter(word)

        for ch, count in word_freq.items():
            if board_freq[ch] < count:
                return False

        # Start from the rarer end of the word
        if board_freq[word[0]] > board_freq[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            # Word completely matched
            if i == len(word):
                return True

            # Boundary check
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            # Character mismatch / already visited
            if board[r][c] != word[i]:
                return False

            # Mark visited
            char = board[r][c]
            board[r][c] = '#'

            next_char = word[i + 1] if i + 1 < len(word) else None

            # Check neighbors
            if next_char is None:
                found = True
            else:
                found = False

                # Down
                if (r + 1 < m and
                    board[r + 1][c] == next_char and
                    dfs(r + 1, c, i + 1)):
                    found = True

                # Up
                elif (r > 0 and
                      board[r - 1][c] == next_char and
                      dfs(r - 1, c, i + 1)):
                    found = True

                # Right
                elif (c + 1 < n and
                      board[r][c + 1] == next_char and
                      dfs(r, c + 1, i + 1)):
                    found = True

                # Left
                elif (c > 0 and
                      board[r][c - 1] == next_char and
                      dfs(r, c - 1, i + 1)):
                    found = True

            # Restore cell
            board[r][c] = char

            return found

        # Try possible starting cells
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False