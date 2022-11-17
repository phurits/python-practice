class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
                #Start Point            #End Point
        Xover = max(rec1[0],rec2[0])  -  min(rec1[2],rec2[2])
        Yover = max(rec1[1],rec2[1])  -  min(rec1[3],rec2[3])
        
        if Xover < 0 and Yover < 0:
            return True
        return False

rec1 = [-4,-9,-2,3]
rec2 = [1,-5,9,-1]

print(Solution().isRectangleOverlap(rec1,rec2))