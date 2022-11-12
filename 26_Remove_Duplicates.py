class Solution:
    def removeDuplicates(self, nums) -> int:
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count

nums = [1,1,2,3,3,3,4,4,4]
print(Solution().removeDuplicates(nums))