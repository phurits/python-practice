class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_s = s[::-1]
        print(rev_s)
        if s == rev_s:
            return True
        return False

x = 121
print(Solution().isPalindrome(x))