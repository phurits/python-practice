class Solution(object):
    def minWindow(self, s, t):
        word = []
        substring = []
        shortestsubstring = ""
        for letter in t:
            word.append(letter)

        # if length of S is shorter than lenght of T
        if len(s) < len(t):
            return shortestsubstring

        # Start Checking All Substring
        for start_index in range(len(s)):
            temp = []
            for j in range(start_index,len(s)):
                count = 0
                temp.append(s[j])
                wordcheck = word.copy()
                for letter in temp:
                    if letter in wordcheck:
                        count += 1
                        wordcheck[wordcheck.index(letter)] = 0
                
                if count == len(word):
                    ########## Convert List to String #########
                    newss = ""
                    for z in temp:
                        newss += z
                    substring.append(newss)

                    ########## Checking New Substring is Shorter #########
                    shortestsubstring = min(substring,key=len)
                    
                    break
                    
        return  shortestsubstring

s = input()
t = input()
ans = Solution().minWindow(s,t)
print(ans)

