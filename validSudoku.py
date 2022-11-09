class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)] 

        for x in range(9):
            for y in range(9):
                index = board[x][y]
                if index == '.':
                    continue
                if index in rows[x] or index in columns[y] or index in squares[x//3][y//3]:
                    return False
                rows[x].add(index)
                columns[y].add(index)
                squares[x//3][y//3].add(index)

        return True

inp = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

ans = Solution().isValidSudoku(inp)
print(ans)