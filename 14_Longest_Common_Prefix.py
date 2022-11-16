class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs = sorted(strs,key=len)
        ans = ""
        for x,word in enumerate(strs[0]):
            for n in range(1,len(strs)):
                if word != strs[n][x]:
                    return ans
            ans += word
        return ans



strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs)) 
