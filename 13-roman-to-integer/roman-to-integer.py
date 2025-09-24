class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Roman symbols to values
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        # Traverse from right to left
        for char in reversed(s):
            curr = values[char]

            # If current value < previous, we subtract (subtractive case like IV, IX, etc.)
            if curr < prev:
                total -= curr
            else:
                total += curr

            prev = curr

        return total
