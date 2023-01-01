class Solution1(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

class Solution2(object):
    def twoSum(self, nums, target):
        dic = {}
        for idx,val in enumerate(nums):
            r = target - val
            if r in dic:
                return [dic[r],idx]
            else:
                dic[val] = idx
            
nums = [2,7,11,15]
target = 9
print(Solution2().twoSum(nums,target))

