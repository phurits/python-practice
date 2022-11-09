class Solution:
    def romanToInt(self, s) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        prev = 0
        total = 0
        for letter in s:
            if prev < roman[letter]:
                total += roman[letter] - (2*prev)
            else:
                total += roman[letter]
            prev = roman[letter]
        return total



s = "MCMXCIV"
ans = Solution().romanToInt(s)
print(ans)