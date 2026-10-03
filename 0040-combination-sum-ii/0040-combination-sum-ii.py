class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, remaining - candidates[i], current)

                # Undo choice
                current.pop()

        backtrack(0, target, [])
        return result