
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch == '+' or ch == '-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                # Only one decimal point, before the exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch == 'e' or ch == 'E':
                # Exponent requires a preceding digit
                # and can appear only once
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False

            else:
                return False

        return seen_digit
