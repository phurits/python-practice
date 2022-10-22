class Solution(object):
    def twoSum(self, nums, target):
        ind = [0,0]
        for i in nums:
            for j in nums:
                if j != i:
                    if j + i == target:
                        ind[0] = nums.index(i)
                        ind[1] = nums.index(j)
                        ind.sort()
        return ind

        

inp = [int(x) for x in input().split()]