class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    for l in range(i+3,len(nums)):
                        temp = []
                        if nums[i] + nums[j] + nums[k] + nums[l] == target and i != j != k != l:
                            temp.append(nums[i])
                            temp.append(nums[j])
                            temp.append(nums[k])
                            temp.append(nums[l])
                            temp.sort()
                            if temp not in ans:
                                ans.append(temp)

        return ans

nums = [int(x) for x in input().split()]
target = input()

ans = Solution().FourSum(nums,target)
print(ans)
