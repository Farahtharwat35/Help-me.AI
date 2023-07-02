import time

from modules.Control import scrollDOWN, scrollUP
from modules.ScreenShot import take_screenshot
from dbCommunciator import readData

LAST_STATE = None

GESTURES, STATES = readData()


LAST_STATE_TIME = time.time()


def map_state_to_function(gesture):
    func = STATES[LAST_STATE].get(gesture)
    print("Executing function: ", func, " in state ", LAST_STATE)
    if func == "scrollUp":
        scrollUP()
    elif func == "scrollDown":
        scrollDOWN()
    elif func == "screenshot":
        take_screenshot()


def map_gesture_to_function(gesture: str):
    gesture = gesture.lower()
    global LAST_STATE_TIME, LAST_STATE
    if (time.time() - LAST_STATE_TIME) <1:
        print("CANNOT PERFORM OPERATION")
        return
    if gesture == "FIST SIGN":
        if LAST_STATE:
            print("Leaving current state " + LAST_STATE)
        LAST_STATE = None
        return
    if LAST_STATE != None:
        map_state_to_function(gesture)

    else:
        LAST_STATE = GESTURES.get(gesture)
        if not LAST_STATE:
            print("Entered wrong state", gesture)
            return
        print("Entered state " + LAST_STATE)
        LAST_STATE_TIME = time.time()
        # print("Entered state spiderman")
        LAST_STATE_TIME = time.time()
        # print("Entered state peace")
        if LAST_STATE == "Null":
            map_state_to_function(gesture)
            LAST_STATE = None




   
