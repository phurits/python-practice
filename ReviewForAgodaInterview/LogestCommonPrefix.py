class Solution1:
    def longestCommonPrefix(self, strs) -> str:
        short = min(strs,key=len)
        ans = ""
        for x in range(len(short)):
            t = 0
            for j in strs:
                if j.startswith(short[:x+1]):
                    t += 1
                else:
                    break
            if t == len(strs):
                ans = short[:x+1]
        return ans

class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        strs = sorted(strs,key=len)
        ans = ""
        for x,word in enumerate(strs[0]):
            for n in range(1,len(strs)):
                if word != strs[n][x]:
                    return ans
            ans += word
        return ans

                

strs = ["dog","racecar","car"]
print(Solution1().longestCommonPrefix(strs))

