class Solution:
    def numSquares(self, n: int) -> int:
        sumlist = []
        power = 100
        def findsum(n,pwr,checklist = []):
            #OUT OF RECURSIVE
            if pwr < 1:
                return
            if n < 0:
                return
            #CHECK IF SUM = 0
            if n - (pwr ** 2) == 0:
                checklist.append(pwr)
                sumlist.append(checklist)
                return

            #OTHER CASE
            if n - (pwr ** 2) < 0:
                findsum(n,pwr-1,checklist)
            if n - (pwr ** 2) > 0:
                checklist.append(pwr)
                findsum(n-(pwr ** 2),pwr,checklist)
            
            return
        findsum(n,power)
        return sumlist
        
n = 12
print(Solution().numSquares(n))
