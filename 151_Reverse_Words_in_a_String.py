class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()           #Remove First & Last Space
        s = " ".join(s.split())
        lst = s.split()
        lst.reverse()
        return " ".join(lst)
        

s = '  hello  world  '
print(Solution().reverseWords(s))