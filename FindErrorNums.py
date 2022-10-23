class Solution:
    def findErrorNums(self, nums):
        n,a,b = len(nums), sum(nums), sum(set(nums))
        s = n*(n+1)//2      #Formula for Addition from 1 to n
        return [a-b,s-b]
        

nums = [int(x) for x in input().split()]
ans = Solution().findErrorNums(nums)
print(ans)