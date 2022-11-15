class Solution:
    def removeStones(self, stones) -> int:
        
        # visited = []
        # coor = stones[-1]

        # def DFS(coor,visited):
        #     if coor not in visited:
        #         visited.append(coor)
        #     for next in stones:
        #         if next in visited:
        #             continue
        #         if coor[0] == next[0] or coor[1] == next[1]:
        #             DFS(next,visited)

        # DFS(coor,visited)
        # return len(visited)-1

        visited = []

        def DFS(coor,visited):
            if coor in visited:
                return
            for next in stones:
                print("Coor = " + str(coor) +"next = " + str(next))
                if next in visited or next == coor:
                    continue
                if coor[0] == next[0] or coor[1] == next[1]:
                    if coor not in visited:
                        visited.append(coor)
                    print("FOUND Coor = " + str(coor) +"next = " + str(next))
                    DFS(next,visited)
        for coor in stones:
            DFS(coor,visited)
            print("Current Node " + str(coor) + " Have Visited " + str(visited))
        return len(visited)-1
        



stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(Solution().removeStones(stones))

# [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]     5
# [[0,0],[0,2],[1,1],[2,0],[2,2]]           3
# [[0,0]]                                   0
# [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]     4