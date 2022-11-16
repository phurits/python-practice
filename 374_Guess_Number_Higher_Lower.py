class Solution:
    def guess(self,num,pick):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        min,max = 1,n
        while min <= max:
            mid = (max + min) // 2
            g = guess(mid)                  # <-- LeetCode Function
            if   g == 1  : min = mid + 1
            elif g == -1 : max = mid - 1
            else : return mid

n = 10
pick = 6

    