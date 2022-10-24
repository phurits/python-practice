class Solution(object):
    def maxLength(self, arr):
        unique = []
        for i in arr:
            j = set(i)
            if len(j) == len(j):
                unique.append(j)
        
        concat = [set()]
        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append(c | u)
        
        return max(len(cc) for cc in concat)
        
                
        """
        :type arr: List[str]
        :rtype: int
        """

inp = input().split()

ans = Solution().maxLength(inp)
print(ans)
