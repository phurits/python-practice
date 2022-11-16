# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int,version) -> int:
        def isBadVersion(v):
            if v >= version:
                return True
            return False
        first,last = 1,n
        if isBadVersion(first):
            return first
        while last - first > 1:
            mid = (first + last) // 2
            status = isBadVersion(mid)
            print(f'F = {first} , L = {last} , mid = {mid} , status = {status}')
            if status is True: last = mid 
            else :  first = mid 
        return last

n,v = 2,2

print(Solution().firstBadVersion(n,v))
