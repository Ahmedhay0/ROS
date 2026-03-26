while True:
    try:
        inp = int(input("Enter an integer:\n"))
        break
    except ValueError:
        print("Invalid input enter a single integer")
big= small=inp
while inp!=-1:
    if inp>big:big=inp
    if inp<small:small=inp
    try:
        inp = int(input("Enter an integer:\n"))
    except ValueError:
        print("Invalid input enter a single integer")
print(big,small)