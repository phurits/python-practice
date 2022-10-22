class Solution(object):
    def threeSum(self, nums):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    temp = []
                    if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[k])
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
        return ans
        

nums = [int(x) for x in input().split()]

ans = Solution().threeSum(nums)
print(ans)
