import time
from datetime import datetime

from Control import scrollDOWN, scrollUP

LAST_STATE = None

STATES = {
    "control": {"palm": "scrollDown", "peace": "scrollUp"},
    "volume": {"thumb": "bye", "index": "goodbye"},
}

GESTURES = {"spiderman": "control", 
            "peace": "volume", 
            "call": "screenshot"}



LAST_STATE_TIME = time.time()


def map_state_to_function(gesture):
    func = STATES[LAST_STATE].get(gesture)
    print("Executing function: ", func)
    if func == "scrollUp":
        scrollUP()
    elif func == "scrollDown":
        scrollDOWN()


def map_gesture_to_function(gesture):
    global LAST_STATE_TIME, LAST_STATE
    # if (time.time() - LAST_STATE_TIME) < 1:
    #     print("CANNOT PERFORM OPERATION")
    #     return
    if gesture == "FIST SIGN":
        print("Leaving current state " + LAST_STATE)
        LAST_STATE = None
        return
    if LAST_STATE != None:
        map_state_to_function(gesture)

    else:
        LAST_STATE = GESTURES.get(gesture)
        print("Entered state " + LAST_STATE)
        LAST_STATE_TIME = time.time()
        # print("Entered state spiderman")
        LAST_STATE_TIME = time.time()
        # print("Entered state peace")
        if LAST_STATE == "screenshot":
            print("taking screenshot")
            LAST_STATE = None


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Executing at: ", current_time)

# time.sleep(1)
map_gesture_to_function("spiderman")
map_gesture_to_function("spiderman")
# time.sleep(1)
map_gesture_to_function("palm")
time.sleep(1.5)
map_gesture_to_function("peace")
map_gesture_to_function("FIST SIGN")
map_gesture_to_function("peace")
map_gesture_to_function("spiderman")
map_gesture_to_function("thumb")
map_gesture_to_function("index")
map_gesture_to_function("call")
map_gesture_to_function("FIST SIGN")
map_gesture_to_function("call")
