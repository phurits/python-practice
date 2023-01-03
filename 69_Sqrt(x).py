class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        while True:
            if num*num > x:
                return num - 1
            num += 1

class Solution2:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        if x == 0 or x == 1:
            return x
        left,right = 0,x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid >= x and (mid+1) * (mid + 1) < x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
x = 4
print(Solution().mySqrt(x))