out=0
for i in range(int(input(""))):
    p,q=input("").split()
    p=int(p)
    q=int(q)
    if q-p>1:
        out+=1
print(out)