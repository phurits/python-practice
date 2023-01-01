class Solution:
    def minFallingPathSum(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        for i in range(h-1):
             for j in range(w):
                cur = matrix[i][j]
                
                next = matrix[i+1][j-1]
        return pathsize

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(Solution().minFallingPathSum(matrix))