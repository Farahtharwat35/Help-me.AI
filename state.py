import time
from datetime import datetime

from Control import scrollDOWN, scrollUP
from ScreenShot import take_screenshot

LAST_STATE = None

STATES = {
    "control": {"palm": "scrollDown", "peace": "scrollUp"},
    "volume": {"thumb": "bye", "index": "goodbye"},
    "Null": {"call": "screenshot"}
}

GESTURES = {"spiderman": "control", 
            "peace": "volume", 
            "call": "Null"}


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
            print(f"Calling Null with {gesture} and last_state {LAST_STATE}")
            map_state_to_function(gesture)
            LAST_STATE = None


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Executing at: ", current_time)

    time.sleep(1)
    map_gesture_to_function("spiderman")
    map_gesture_to_function("spiderman")
    time.sleep(1)
    map_gesture_to_function("palm")
    time.sleep(1.5)
    map_gesture_to_function("peace")
    time.sleep(1)
    map_gesture_to_function("FIST SIGN")
    time.sleep(1)
    map_gesture_to_function("peace")
    time.sleep(1)
    map_gesture_to_function("spiderman")
    time.sleep(1)
    map_gesture_to_function("thumb")
    time.sleep(1)
    map_gesture_to_function("index")
    time.sleep(1)
    map_gesture_to_function("call")
    time.sleep(1)
    map_gesture_to_function("FIST SIGN")
    time.sleep(1)
    map_gesture_to_function("call")
    time.sleep(1)
