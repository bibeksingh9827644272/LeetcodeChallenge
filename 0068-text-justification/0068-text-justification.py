
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Greedily fit as many words as possible
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            # Last line or a line with only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = num_words - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                parts = []
                for k in range(gaps):
                    parts.append(words[i + k])
                    spaces = spaces_per_gap
                    if k < extra_spaces:
                        spaces += 1
                    parts.append(" " * spaces)

                parts.append(words[j - 1])
                line = "".join(parts)

            result.append(line)
            i = j

        return result
