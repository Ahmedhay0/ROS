import platform , datetime
def main():
    if __name__=="__main__":
        log_system_info()

def log_system_info():
    with open("sys_log.txt","w") as file:
        file.write(f"{platform.system()} \n { datetime.datetime.now().timestamp()}")
main()