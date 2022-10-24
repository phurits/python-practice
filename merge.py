class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        for i in range(m):
            temp.append(nums1[i])
        for i in range(n):
            temp.append(nums2[i])
        temp.sort()
        nums1 = temp
        return nums1

nums1 = []
nums2 = []
m = 0
n = 0

nums1 = [int(x) for x in input().split()]
m = int(input())
nums2 = [int(x) for x in input().split()]
n = int(input())
Solution().merge(nums1,m,nums2,n)