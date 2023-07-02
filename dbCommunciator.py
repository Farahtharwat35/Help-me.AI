
import json
 
def readFile():
    lines = open("./database/main.txt", 'r').read().splitlines()
    states = {}
    gestures = {}
    for line in lines:
        command, calling = line.split("=")
        state, sequence = calling.split(":")
        enterGesture, callingGesture = sequence.split("->")
        if state == "Null":
            gestures[enterGesture] = callingGesture
        else:
            gestures[enterGesture] = state
        
        newState = {callingGesture: command}
        # states[state] = newState
        if states[state]:
            pass
        states.update()

    print(states)
    print(gestures)

def readData():
    with open('./database/database.json', 'r') as openfile:
        data = json.load(openfile)
        return data["GESTURES"], data["STATES"]
    
gestures, states = readData()

print(gestures)
print(states)