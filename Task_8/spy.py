out=[]
inp=[]
for i in range(int(input())):
    x = int(input())
    for j in input().split():
        inp.append(int(j))
    original = inp.copy()
    inp.sort()
    if inp[1]==inp[0]:
        out.append(original.index(inp[x-1])+1)
    else:
        out.append(original.index(inp[0])+1)
    inp=[]
print(*out,sep='\n')