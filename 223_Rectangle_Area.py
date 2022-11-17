class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        width1,height1 = abs(ax2 - ax1),abs(ay2 - ay1)
        width2,height2 = abs(bx2 - bx1),abs(by2 - by1)

        area1,area2 = width1 * height1,width2*height2

        Xstartpoint = max(ax1,bx1)
        Xendpoint   = min(ax2,bx2)
        Ystartpoint = max(ay1,by1)
        Yendpoint   = min(ay2,by2)
        
        Xover = Xendpoint - Xstartpoint
        Yover = Yendpoint - Ystartpoint
        
        if Xover > 0 and Yover > 0:
            return area1 + area2 - (Xover * Yover)
        else:
            return area1 + area2

        

print(Solution().computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))