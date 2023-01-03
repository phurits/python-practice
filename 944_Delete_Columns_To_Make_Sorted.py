class Solution:
    def minDeletionSize(self, strs) -> int:
        col = 0
        for i in range(len(strs[0])):
            temp = []
            for j in strs:
                temp.append(j[i])
            if temp != sorted(temp):
                col += 1
        return col

class Solution2:
    def minDeletionSize(self, strs) -> int:
        col = 0
        for i in zip(*strs):
            if list(i) != sorted(list(i)):
                col += 1
        return col

strs = ["rrjk","furt","guzm"]
print(Solution2().minDeletionSize(strs))
