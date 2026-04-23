import os,sys
os.system("")

temp_n1="player 1"
temp_n2="player 2"
temp_s1="X"
temp_s2="O"
p1_c,p2_c="31","34"
p1_n,p2_n=f"\033[{p1_c}m{temp_n1}\033[0m",f"\033[{p2_c}m{temp_n2}\033[0m"
p1_s,p2_s=f"\033[{p1_c}m{temp_s1}\033[0m",f"\033[{p2_c}m{temp_s2}\033[0m"
p1_scr,p2_scr=0,0
board={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
turn = 1
game_end=False
winner=""
win=False
n=3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        choice = input("1.change players' names\n2.change symbols\n3.change colors\n4.change board size\n5.start game\n(changing names resets scores to 0)\n")
        try:
            choice = int(choice)
        except ValueError:
            clear_screen()
            print("invalid choice choose from the menu") 
            continue
        if choice==1:
            clear_screen()
            change_name()
        elif choice==2:
            clear_screen()
            change_syms()
        elif choice==3:
            clear_screen()
            change_clr()
        elif choice==4:
            clear_screen()
            change_brd()
        elif choice==5:
            clear_screen()
            game()
        else:
            clear_screen()
            print("invalid choice choose from the menu")

def change_name():
    global p1_s,p1_c,p1_n,p2_c,p2_s,p2_n,temp_n1,temp_n2
    while True:
        temp_n1= input("Choose a name for player 1:\n(No input is considered default(player 1))\n")
        clear_screen()
        temp_n2=input("Choose a name for player 2:\n(No input is considered default(player 2))\n")
        clear_screen()
        if temp_n1=="":
            temp_n1="player 1"
        if temp_n2=="":
            temp_n2="player 2"
        if temp_n1 == temp_n2:
            print("players can't be the same name")
            continue
        p1_n,p2_n=f"\033[{p1_c}m{temp_n1}\033[0m",f"\033[{p2_c}m{temp_n2}\033[0m"
        if input(f"player 1 name is {p1_n} and player 2 name is {p2_n} is that correct?(y to exit naming)").lower()=="y":
            clear_screen()
            global p1_scr,p2_scr
            p1_scr,p2_scr=0,0
            break

def change_syms():
    global p1_s,p1_c,p1_n,p2_c,p2_s,p2_n,temp_s1,temp_s2
    while True:
        choice = input(f"1.Exchange p1 and p2 symbols:\n2.Choose new symbols\n(Default is X for {p1_n} and O for {p2_n}, note that symbols are case sensitive and can't be numbers)\n")
        try:
            choice = int(choice)
        except ValueError:
            clear_screen()
            print("invalid choice choose from the menu")
            continue
        if choice==1:
            temp_s1,temp_s2=temp_s2,temp_s1
            clear_screen()
        elif choice == 2:
            temp_s1=input(f"choose symbol for {p1_n}\n(spaces and empty strings are considered default)\n")
            clear_screen()
            try: 
                int(temp_s1)
                print("symbols can't be numbers")
                continue
            except ValueError:
                pass
            if temp_s1.strip()=="":
                temp_s1="X"
            temp_s2=input(f"choose symbol for {p2_n}\n(spaces and empty strings are considered default)\n")
            try: 
                int(temp_s2)
                print("symbols can't be numbers")
                continue
            except ValueError:
                pass
            if temp_s2.strip()=="":
                temp_s2="O"
        if temp_s1 == temp_s2:
            print("Symbols must be different")
            continue
        p1_s,p2_s=f"\033[{p1_c}m{temp_s1}\033[0m",f"\033[{p2_c}m{temp_s2}\033[0m"
        if input(f"{p1_n} is {p1_s} {p2_n} is {p2_s} is that correct?(y to exit symbols changing)").lower()=="y":
            clear_screen()
            break

def change_clr():
    global p1_s,p1_c,p1_n,p2_c,p2_s,p2_n
    while True:
        choice = input(f"1.Exchange player colors\n2.choose different colors\n(default is \033[31mRed\033[0m for {temp_n1} and \033[34mBlue\033[0m for {temp_n2})\n")
        try:
            choice = int(choice)
        except ValueError:
            clear_screen()
            print("invalid choice choose from the menu")
            continue 
        if choice == 1:
            p1_c,p2_c=p2_c,p1_c
        elif choice == 2:
            colors={"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,"cyan":36,"white":37}
            while True:
                color=input(f"choose a color for {p1_n}:\n(availabe colors are red, green, blue, yellow, magenta, cyan, white)\n").lower()
                if color in colors:
                    p1_c=colors[color]
                    break
                else:
                    clear_screen()
                    print("unavailable color")
                    continue
            while True:
                color=input(f"choose a color for {p2_n}:\n(availabe colors are red, green, blue, yellow, magenta, cyan, white)\n").lower()
                if color in colors:
                    p2_c=colors[color]
                    break
                else:
                    clear_screen()
                    print("unavailable color")
                    continue
        p1_n,p2_n=f"\033[{p1_c}m{temp_n1}\033[0m",f"\033[{p2_c}m{temp_n2}\033[0m"
        p1_s,p2_s=f"\033[{p1_c}m{temp_s1}\033[0m",f"\033[{p2_c}m{temp_s2}\033[0m"
        if input(f"colors for players are: {p1_n}, {p2_n} is that correct?(y to exit color changing)").lower()=='y':
            clear_screen()
            break
def change_brd():
    global n,board
    while True:
        n=input("Insert board N*N size\n(Size can't be less than 3 and the default is 3)\n")
        try:
            n = int(n)
        except ValueError:
            clear_screen()
            print("invalid input choose a single integer higher than 2")
            continue
        if n<3:
            clear_screen()
            print("N can't be less than 3")
            continue
        break
    board={}
    for i in range(1,n**2+1):
        board[i]=str(i)
    
def check_win():
    global winner,game_end,p1_n,p1_scr,p2_scr,p2_n,win,n,board
    if turn>=2*n-1:
        for i in range(1,n+1):
            last_sym=board[i]
            for k in range(1,n):
                if board[i+n*k]==last_sym:
                    if k !=n-1:continue
                    if last_sym==p1_s:
                        winner=p1_n
                        p1_scr+=1
                    else:
                        winner=p2_n
                        p2_scr+=1
                    win =True
                    game_end=True
                    return
                else:
                    break
        i=1
        while i <= n**2-n+1:
            last_sym=board[i]
            for k in range(1,n):
                if board[i+k]==last_sym:
                    if k !=n-1:continue
                    if last_sym==p1_s:
                        winner=p1_n
                        p1_scr+=1
                    else:
                        winner=p2_n
                        p2_scr+=1
                    win =True
                    game_end=True
                    return
                else:
                    break
            i+=n
        i=1
        last_sym=board[1]
        while i <=n**2:
                if last_sym==board[i]:
                    if i!=n**2:
                        i+=(n+1)
                        continue
                    if last_sym==p1_s:
                        winner=p1_n
                        p1_scr+=1
                    else:
                        winner=p2_n
                        p2_scr+=1
                    win =True
                    game_end=True
                    return
                else: break
        i=2*n-1
        last_sym=board[n]
        while i<n**2:
            if last_sym==board[i]:
                    if i!=n**2-n+1:
                        i+=(n-1)
                        continue
                    if last_sym==p1_s:
                        winner=p1_n
                        p1_scr+=1
                    else:
                        winner=p2_n
                        p2_scr+=1
                    win =True
                    game_end=True
                    return
            else: break
            
                
            
            

def disp_board():
    w = len(str(n**2))

    for i in range(1, n**2 + 1):
        print(board[i].center(w), end="")

        if i % n != 0:
            print(" | ", end="")
        else:
            print()
            if i != n**2:
                print(("-" * w + "-+-") * (n - 1) + "-" * w)


def game():
    global turn,p1_s,p1_c,p1_n,p2_c,p2_s,p2_n,p1_scr,p2_scr,game_end,board,win
    while not game_end:
        print("unoccupied positions are displayed on board")
        disp_board()
        if turn%2:
            print(f"{p1_n}'s turn")
        else: print(f"{p2_n}'s turn")
        move = input("where do you want to play?")
        try:
            move = int(move)
        except ValueError:
            clear_screen()
            print("invalid position")
            continue
        if move not in board or board[move] == p1_s or board[move]==p2_s:
            print("position is unavailable")
            continue
        if turn%2:
            board[move]=p1_s
        else: board[move]=p2_s
        check_win()
        clear_screen()
        turn+=1
        if turn==n**2+1:
            game_end=True
    if win:
        print(f"{winner} is the winner")
    else:
        print("It's a draw")
    print(f"current score:\n{p1_n}:{p1_scr}\n{p2_n}:{p2_scr}")
    turn = 1
    win=False
    game_end=False
    for i in range(1,len(board)+1):
        board[i]=str(i)
    if input("Do you want to play again?(y for a rematch)").lower()=="y":
        clear_screen()
        game()
    else:
        clear_screen()
        if input("return to main menu?(y to return refusing closes the game)").lower()=="y":
            clear_screen()
            main_menu()
        else: sys.exit()
main_menu()