import time

from modules.Control import scrollDOWN, scrollUP
from modules.ScreenShot import take_screenshot
from dbCommunciator import readData

LAST_STATE = None

GESTURES, STATES = readData()


LAST_STATE_TIME = time.time()


def map_state_to_function(gesture):
    func = STATES[LAST_STATE].get(gesture)
    print("Executing function: ", func)
    if func == "scrollUp":
        scrollUP()
    elif func == "scrollDown":
        scrollDOWN()
    elif func == "screenshot":
        take_screenshot()


def map_gesture_to_function(gesture):
    global LAST_STATE_TIME, LAST_STATE
    if (time.time() - LAST_STATE_TIME) < 0.5:
        print("CANNOT PERFORM OPERATION")
        return
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
        if LAST_STATE == "Null":
            map_state_to_function(gesture)
            LAST_STATE = None




   
