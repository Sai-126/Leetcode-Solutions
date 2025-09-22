class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: remove leading whitespace
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1
        return sign * res
