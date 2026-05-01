out=[]
for i in range(int(input())):
    rate = int(input())
    if rate>=1900:
        out.append("Division 1")
    elif rate>=1600:
        out.append("Division 2")
    elif rate>=1400:
        out.append("Division 3")
    else: out.append("Division 4")
print(*out,sep="\n")