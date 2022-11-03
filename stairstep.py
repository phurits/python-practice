def stairsloop(n):
    pos1,pos2 = 1,1
    for i in range(n-1):
        temp = pos1
        pos1 = pos1 + pos2
        pos2 = temp
    return pos1


inp = int(input())
ans = stairsloop(inp)
print(ans)

