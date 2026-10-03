class Solution:
    def combine(self, n: int, k: int):
        result = []
        current = []

        def backtrack(start):
            # If we selected k numbers, save the combination
            if len(current) == k:
                result.append(current.copy())
                return

            # Try every possible next number
            for num in range(start, n + 1):
                current.append(num)

                # Continue with numbers after num
                backtrack(num + 1)

                # Remove the last number (backtrack)
                current.pop()

        backtrack(1)
        return result