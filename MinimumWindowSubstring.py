class Solution(object):
    def minWindow(self, s, t):
        word = []
        substring = []
        shortestsubstring = ""
        for letter in t:
            word.append(letter)
        
        for start_index in range(len(s)):
            temp = []
            for j in range(start_index,len(s)):
                temp.append(s[j])
                count = 0
                for letter in word:
                    if letter in temp:
                        count += 1
                if count == len(word):
                    ########## Convert List to String #########
                    newss = ""
                    for z in temp:
                        newss += z
                    substring.append(newss)

                    ########## Checking New Substring is Shorter #########
                    shortestsubstring = min(substring,key=len)
                    
                    break
                    
        return shortestsubstring


s = input()
t = input()
ans = Solution().minWindow(s,t)
print(ans)

