class Solution(object):
    def twoSum(self, nums, target):
        ind = [0,0]
        for x,y in enumerate(nums):
            for xx,yy in enumerate(nums):
                if y + yy == target and x != xx:
                    ind[0] = x
                    ind[1] = xx
                    ind.sort()
        return ind

        

nums = [int(x) for x in input().split()]
target = int(input())

ans = Solution().twoSum(nums,target)
print(ans)