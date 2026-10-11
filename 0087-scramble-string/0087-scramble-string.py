
from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        @lru_cache(None)
        def solve(a: str, b: str) -> bool:
            if a == b:
                return True

            # Prune if character frequencies differ
            if Counter(a) != Counter(b):
                return False

            n = len(a)

            for i in range(1, n):
                # Case 1: No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    return True

                # Case 2: Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    return True

            return False

        return solve(s1, s2)
