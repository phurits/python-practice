class Solution:
    def removeElement(self, nums, val: int) -> int:
        # Second Solution | From Last Index to First Index
        m = len(nums)
        for i in range(m-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

        

nums = [0,1,2,2,3,0,4,2]

val = 2

print(Solution().removeElement(nums,val))