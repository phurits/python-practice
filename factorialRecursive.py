def factorial(inp):
    if inp == 0:
        return 1
    return factorial(inp-1) * inp

inp = int(input())
ans = factorial(inp)
print(ans)
