class Solution:
    def findBall(self, grid):

        b = []
        #print Grid 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    print("\\",end="")
                else:
                    print("/",end="")
            print()

        Lhit = 0
        Rhit = 0
        Dhit = 0

        curpos = []

        for i in range(len(grid[0])):
            Lhit = 0
            Rhit = 0
            Dhit = 0

            curpos = [i,0]
            while(Lhit != 1 or Rhit != 1  or Dhit != 1):
                
            
                #check Current Position
                if grid[curpos[0]][curpos[1]] == 1:         #Check Right
                    
                    if curpos[1]+1 >= len(grid[0]):
                        Rhit == 1       #RIGHT WALL
                        break

                    nextpos = [curpos[0],curpos[1]+1]

                    # Right is Wall
                    if nextpos[1] >= len(grid[0][0]):
                        Rhit == 1
                        break

                    

                elif grid[curpos[0]][curpos[1]] == -1:      #Check Left

                    if curpos[1]-1 <= 0:    
                        Lhit == 1   
                        break

                    nextpos = [curpos[0],curpos[1]+1]


                    






        return


inp = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
ans = Solution().findBall(inp)
