class Solution:
    def longestCommonPrefix(self, strs) -> str:
        l = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                l = l + i[0]
            else:
                break
        return l

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))