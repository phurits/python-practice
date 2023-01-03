class Solution:
    def pivotIndex(self, nums ) -> int:
        left,right = 0,sum(nums)
        for idx,num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1



nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))