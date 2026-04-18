try:
    with open("config.json","r"):
        print("system ready")
except FileNotFoundError:
    with open("config.json","x"):
        print("File has been created")