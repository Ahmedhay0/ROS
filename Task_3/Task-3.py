def pick_winner(names=[]):
    if names ==[] or not isinstance(names,list):
        print("Please input a list that isn't empty")
        return
    from random import randint
    return names[randint(0,len(names)-1)]
#print(pick_winner(["john","amr","paul","mark","nolan"]))


def move_player(x=0,y=0,direc=""):
    if direc=="":
        return x , y
    elif direc.lower()=="up":
        y+=5
    elif direc.lower()=="down":
        y-=5
    elif direc.lower()=="left":
        x-=5
    elif direc.lower()=="right":
        x+=5
    else:
        print("Please input a valid direction")
    return x , y
#print(move_player(6,10,"up"))

def common_elements(set1,set2):
    com=set()
    for i in set1:
        if i in set2:
            com.add(i)
    return com
#print(common_elements({1,"cat","banana","water","johan"},{5,"johan","water","idk"}))


def get_unique_lottery():
    from random import randint
    winners=set()
    while len(winners) < 6:
        winners.add(randint(1,50))
    return winners
#print(get_unique_lottery())

def calculate_bill(prices={},items=[]):
    if prices =={}:
        print("Please input prices and items bought")
        return
    total=0
    for i in items:
        if i in prices:
            total+=prices[i]
    return total
#print(calculate_bill({'banana':0.3,"apple":0.4,"bread":0.2,"chocolate":0.6},['banana',"chocolate","chocolate"]))


def analyze_grades(grades=[]):
    if grades == [] or not isinstance(grades[0],int):
        print("Input a list of grades please")
        return
    high = low = grades[0]
    average=0
    for i in grades:
        if i>high:
            high=i
        elif i<low:
            low=i
        average+=i
    average/=len(grades)
    return high , low , average
print(analyze_grades([100,50,60,70,20,35,47,12,39,26,46,76]))


