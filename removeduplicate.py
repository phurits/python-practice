class Solution(object):
    def removeDuplicates(self, nums):
        nodup = set(nums)
        newlist = []
        for i in nodup:
            newlist.append(i)
        return newlist
        

nums = [int(x) for x in input().split()]

ans = Solution().removeDuplicates(nums)
print(ans)