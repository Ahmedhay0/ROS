def write_log(x):
    with open("log.txt","a") as file:
        file.write(x+"\n")
def read_logs():
    with open("log.txt","r") as file:
        for line in file:
            print(line.strip())
read_logs()