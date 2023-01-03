class Solution:
    def runningSum(self, nums):
        ans = []
        temp = 0
        for i in nums:
            ans.append(i+temp)
            temp += i
        return ans

nums = [1,2,3,4]
print(Solution().runningSum(nums))