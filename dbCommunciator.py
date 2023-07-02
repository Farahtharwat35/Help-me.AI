
import json
 
def readData():
    with open('./database/database.json', 'r') as openfile:
        data = json.load(openfile)
        return data["GESTURES"], data["STATES"]
    
gestures, states = readData()

print(gestures)
print(states)