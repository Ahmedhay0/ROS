out = 0
for i in range(int(input())):
    inp=[]
    for i in input().split():
        inp.append(int(i))
    if inp[0]+inp[1]+inp[2]>1:
        out+=1
print(out)
