from datetime import datetime
import time
from state import map_gesture_to_function

def callStateWithdelay(parameter: str):
    time.sleep(1)
    map_gesture_to_function(parameter)
    time.sleep(1)

def allStates():
    callStateWithdelay("spiderman")
    callStateWithdelay("spiderman")
    callStateWithdelay("palm")
    callStateWithdelay("peace")
    callStateWithdelay("FIST SIGN")
    callStateWithdelay("peace")
    callStateWithdelay("spiderman")
    callStateWithdelay("thumb")
    callStateWithdelay("index")
    callStateWithdelay("call")
    callStateWithdelay("FIST SIGN")
    callStateWithdelay("call")

def nullableStates():
    callStateWithdelay("call")
    callStateWithdelay("like")


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Executing at: ", current_time)

    nullableStates()