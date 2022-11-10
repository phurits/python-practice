class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [""]
        for i in range(len(s)):
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        ans = ""     
        return ans.join(stack)    

s = "azxxzy"
print(Solution().removeDuplicates(s))