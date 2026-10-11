
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        required = len(t)
        left = 0
        min_len = float("inf")
        start = 0

        for right, char in enumerate(s):
            if need[char] > 0:
                required -= 1

            need[char] -= 1

            # All characters from t are included
            while required == 0:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    start = left

                # Remove the leftmost character
                left_char = s[left]
                need[left_char] += 1

                if need[left_char] > 0:
                    required += 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
