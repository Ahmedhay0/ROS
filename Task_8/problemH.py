out=[]
for i in range(int(input())):
    inp=[]
    x =int(input())
    for j in input().split():
        inp.append(int(j))
    inp.sort()
    out.append(inp[x-1]-inp[0])
print(*out,sep="\n")