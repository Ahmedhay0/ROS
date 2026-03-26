while True:
    try:
        inp = int(input("Enter a positive integer:\n"))
        if inp>0:
            break
        else:
            print("Invalid input enter a single postive integer")
    except ValueError:
        print("Invalid input enter a single postive integer")
if inp>1:
    i = 1
    sum = 0
    rep = inp//2
    while i<rep+1:
        sum += i*2
        i+=1
    print(sum)
else:print(0)