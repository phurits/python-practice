class Solution(object):
    def plusOne(self, digits):
        text = ""
        for i in digits:
            text += str(i)
        nums = int(text)
        nums += 1
        text = str(nums)
        ans = []
        for i in range(len(text)):
            ans.append(int(text[i]))
        return ans

digits = [int(x) for x in input().split()]

ans = Solution().plusOne(digits)
print(ans)