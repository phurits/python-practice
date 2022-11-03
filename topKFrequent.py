class Solution:
    def topKFrequent(self, words, k: int):
        mydict = {}
        ans = []
        words = sorted(words)
        for i in words:
            mydict[i] = words.count(i)
        sortvaluedict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(sortvaluedict[i][0])
        return ans

inp = input().split()
k = int(input())
ans = Solution().topKFrequent(inp,k)
print(ans)