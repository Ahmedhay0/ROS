out = []
for i in range(int(input())):
    length = int(input())
    name1,name2=input().split()
    for j in range(length):
        if name1[j] in name2:
            name2=name2.replace(name1[j],"",1)
        else:
            out.append("NO")
            break
    if name2=="":
        out.append("YES")
print(*out,sep="\n")