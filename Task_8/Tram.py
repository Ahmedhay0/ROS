current=0
highest=0
for i in range(int(input())):
    a,b=input().split()
    a,b=int(a),int(b)
    current+=b-a
    if highest<current:
        highest=current
print(highest)