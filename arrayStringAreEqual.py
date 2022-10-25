class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ""
        str2 = ""
        for i in word1:
            str1 += i
        for i in word2:
            str2 += i
        if str1 == str2:
            return True
        else:
            return False

word1 = input().split()
word2 = input().split()

ans = Solution().arrayStringsAreEqual(word1,word2)
print(ans)