out=[]
for i in range(int(input())):
    word = input()
    if len(word)<11:
        out.append(word)
    else:
        out.append(word[0]+str(len(word)-2)+word[-1])
print(*out,sep='\n')