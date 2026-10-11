
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            current = []
            i = 0

            while i < len(result):
                count = 1

                # Count consecutive identical digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1

                # Append count followed by the digit
                current.append(str(count))
                current.append(result[i])

                i += 1

            result = "".join(current)

        return result
