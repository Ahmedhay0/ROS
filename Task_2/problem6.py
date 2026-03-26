sent=input("Enter your sentence:")
last = 0
i = 0
words=[]
for i in range(len(sent)):
    if sent[i]==" ":
        words.append(sent[last:i])
        last = i+1
words.append(sent[last:len(sent)+1])
words.reverse()
print(*words)