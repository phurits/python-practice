class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            ans = int('-' + str(abs(x))[::-1])
        else:
            ans = int(s[::-1])
        return 0 if not (-2**31 <= ans <= (2**31)-1) else ans


x = 1534236469
print(Solution().reverse(x))