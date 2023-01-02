class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        #if word[0].isupper() and word[1:].islower(): 
        if word.istitle():
            return True
        return False

word = "Usa"
print(Solution().detectCapitalUse(word))
