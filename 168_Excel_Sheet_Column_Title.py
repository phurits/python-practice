class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(65+columnNumber%26) + ans
            columnNumber //= 26
        return ans

columnNumber = 701
print(Solution().convertToTitle(columnNumber))