class Solution(object):
    def isPalindrome(self, x):
        temp = str(x)
        for i in range(len(temp)):
            if(temp[i] != temp[len(temp)-i-1]):
                return False
        return True

inp = int(input())

ans = Solution().isPalindrome(inp)
print(ans)

