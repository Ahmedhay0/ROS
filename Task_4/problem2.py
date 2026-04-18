def load_inventory():
    import json
    try:
        with open("Inventory.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_inventory(data):
    import json
    with open("Inventory.json","w") as file:
        json.dump(data,file,indent=4)
