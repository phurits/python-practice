class Solution:
    def moveZeroes(self, nums) -> None:
        m = len(nums)
        for i in range(m-1,-1,-1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
        return

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)