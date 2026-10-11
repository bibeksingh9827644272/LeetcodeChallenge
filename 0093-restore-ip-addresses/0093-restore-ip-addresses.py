
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start: int, parts: list[str]) -> None:
            # A valid IP must contain exactly 4 parts
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Try segments of length 1, 2, or 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                # Leading zeros are not allowed
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # Each segment must be between 0 and 255
                if int(segment) > 255:
                    continue

                parts.append(segment)
                backtrack(start + length, parts)
                parts.pop()

        # An IP address has 4 parts, each containing 1–3 digits
        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result
