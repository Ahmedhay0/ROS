out=[]
inp=[]
for i in range(int(input())):
    for i in input().split():
        inp.append(int(i))
        inp.sort()
    if inp[0]+inp[1]==inp[2]:
        out.append("YES")
    else:out.append("NO")
    inp=[]
print(*out,sep='\n')