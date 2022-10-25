class Solution:
    def countAndSay(self, n: int) -> str:
        saytext = ""
        cur = "1"
        alllist = []
        
        for i in range(1,n+1):      #check n number
            alllist=[]
            if i == 1:
                saytext = "1"
                continue
            else:
                count = 0
                cur = saytext[0]
                for j in range(len(saytext)):       #check text in order
                    
                    if saytext[j] == cur:
                        count += 1
                    else:
                        templist = [count,cur]
                        alllist.append(templist)
                        cur = saytext[j]
                        count=1
                    if j == len(saytext)-1:
                        templist = [count,cur]
                        alllist.append(templist)
            ttext = ""
            for map in alllist:
                ttext += str(map[0])
                ttext += str(map[1])
            saytext = ttext
        return saytext
                
            


inp = int(input())


print(Solution().countAndSay(inp))