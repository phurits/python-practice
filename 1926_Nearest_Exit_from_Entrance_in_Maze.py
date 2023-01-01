class Solution:
    def nearestExit(self, maze, entrance) -> int:
        allpath = set()
        edge = []
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if i == 0 or j == 0 or i == len(maze)-1 or j == len(maze[i])-1:
                    edge.append([i,j])

        def shortestPath(index,path,havego = []):
            if index in edge and index != entrance:
                    return allpath.add(path)
            if maze[index[0]][index[1]] == '+':
                return 
            if index in havego:
                return
            havego.append(index)
            #up
            if maze[index[0]][index[1]-1] == '.' and index[1] >= 0:
                shortestPath([index[0],index[1]-1],path+1,havego)
            #down
            if maze[index[0]][index[1]+1] == '.' and index[1] < len(maze[0]):
                shortestPath([index[0],index[1]+1],path+1,havego)
            #left
            if maze[index[0]-1][index[1]] == '.' and index[0] >= 0:
                shortestPath([index[0]-1,index[1]],path+1,havego)
            #right
            if maze[index[0]+1][index[1]] == '.' and index[0] < len(maze):
                shortestPath([index[0]+1,index[1]],path+1,havego)
            return
        shortestPath(entrance,0)
        return min(allpath)


maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

print(Solution().nearestExit(maze,entrance))