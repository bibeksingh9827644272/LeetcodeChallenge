class Solution:
    def permute(self, nums):
        result = []

        def backtrack(current):
            # A complete permutation
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                # Don't use the same number twice
                if num in current:
                    continue

                current.append(num)

                # Continue building the permutation
                backtrack(current)

                # Undo the choice
                current.pop()

        backtrack([])
        return result