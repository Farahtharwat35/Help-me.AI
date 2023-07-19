import json
 
dbType = tuple[dict[str, str], dict[str, dict[str, str]]]

def readData() -> dbType:
    with open('./database/database.json', 'r') as openfile:
        data = json.load(openfile)
        return data["GESTURES"], data["STATES"]

def writeData(data):
    with open("./database/database.json", "w") as writeFile:
        json.dump(data, writeFile, indent=4)

gestures, states = readData()

print(gestures)
print(states)