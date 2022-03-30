class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        digit = 0

        for i in range(len(s)):
            digit = digit + d[s[i]]

        for k in range(len(s) - 1):
            if d[s[k]] < d[s[k + 1]]:
                digit = digit - 2 * d[s[k]]

        return digit


roman = Solution()
print(roman.romanToInt(s='XIV'))
