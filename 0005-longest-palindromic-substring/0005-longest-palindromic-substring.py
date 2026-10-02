class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(n):
            # Odd-length palindrome
            left, right = expand(i, i)

            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1

            # Even-length palindrome
            left, right = expand(i, i + 1)

            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1

        return s[start:start + max_len]