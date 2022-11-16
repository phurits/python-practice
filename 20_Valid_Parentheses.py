class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbol = {
            '(':')',
            '[':']',
            '{':'}',
        }
        for letter in s:
            if letter in symbol.keys():
                stack.append(symbol[letter])
            elif not stack or stack[-1] != letter:
                return False
            else:
                stack.pop()

        return len(stack) == 0
s = "())"
print(s)
print(Solution().isValid(s))
        