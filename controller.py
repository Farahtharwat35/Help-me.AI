WHATSAPP_FILE = "./database/Whatsapp.txt"
NAVIGATE_FILE = "./database/Navigate.txt"
CONTROLLER_FILE = "./database/Control.txt"
ANGHAMI_FILE = "./database/Anghami.txt"
GESTURES_FILE = "./database/gestures.txt"
whatsapp_file = open(WHATSAPP_FILE)
whatsapp_data = whatsapp_file.readlines()
whatsapp_dic = {}
for line in whatsapp_data:
    whatsapp_dic[line.split()[0]] = line.split()[1]

navigate_data = open(NAVIGATE_FILE).readlines()
navigate_dic = {}
for line in navigate_data:
    navigate_dic[line.split()[0]] = line.split()[1]

controller_file = open(CONTROLLER_FILE)
controller_data = controller_file.readlines()
control_dic = {}
for line in controller_data:
    control_dic[line.split()[0]] = line.split()[1]

anghami_data = open(ANGHAMI_FILE).readlines()
anghami_dic = {}
for line in anghami_data:
    anghami_dic[line.split()[0]] = line.split()[1]

gesture_data = open(GESTURES_FILE).readlines()
gesture_dic = {}
for line in gesture_data:
    gesture_dic[line.split()[0]] = line.split()[1]

modules = {
    "Control": "SIGN/Control/Enter/TRUE/",
    "Navigate": "SIGN/Navigate/Enter/TRUE/",
    "ScreenShot": "SIGN/ScreenShot/take_screenshot/FALSE/",
    "Anghami": "SIGN/Anghami/open_Anghami/TRUE/",
    "Whatsapp": "SIGN/Whatsapp/open_whatsapp/TRUE/"
}

functions = {
    "Volume Up": "SIGN/Control/VolumeUP",
    "Volume Down": "SIGN/Control/VolumeDOWN",
    "Scroll Up": "SIGN/Control/scrollUP",
    "Scroll Down": "SIGN/Control/scrollDOWN",
    "Open Program": "SIGN/Control/open_program/",
    "Search for Playlist": "SIGN/Anghami/search_playlist/",
    "Navigate": "SIGN/Navigate/navigate/",
    "Search Contact": "SIGN/Whatsapp/search_for_contact/",
    "Send Message": "SIGN/Whatsapp/send_whatsapp_message/",
    "Open Mic": "SIGN/Whatsapp/Open_mic",
}


def txt_emptylines(filename):
    with open(filename) as f_input:
        data = f_input.read().rstrip('\n')

    with open(filename, 'w') as f_output:
        f_output.write(data)


def whatsapp_update(gesture, function, params):
    new_function = function + params

    key = {i for i in whatsapp_dic if whatsapp_dic[i] == new_function}
    if key:
        del whatsapp_dic[key.pop()]

    whatsapp_dic[gesture] = new_function

    txt = ""
    for key, value in whatsapp_dic.items():
        txt += f"{key} {value}\n"

    open(WHATSAPP_FILE, "w+").write(txt)
    txt_emptylines(WHATSAPP_FILE)


def navigate_update(gesture, location):
    new_function = functions["Navigate"] + location

    key = {i for i in navigate_dic if navigate_dic[i] == new_function}
    if key:
        del navigate_dic[key.pop()]

    navigate_dic[gesture] = new_function
    txt = ""
    for key, value in navigate_dic.items():
        txt += f"{key} {value}\n"

    open(NAVIGATE_FILE, "w+").write(txt)
    txt_emptylines(NAVIGATE_FILE)


def control_update(gesture, function, program):
    if (function == "SIGN/Control/open_program/"):
        new_function = function + program
    else:
        new_function = function

    key = {i for i in control_dic if control_dic[i] == new_function}
    if key:
        del control_dic[key.pop()]

    control_dic[gesture] = new_function

    txt = ""
    for key, value in control_dic.items():
        txt += f"{key} {value}\n"

    open(CONTROLLER_FILE, "w+").write(txt)
    txt_emptylines(CONTROLLER_FILE)


def anghami_update(gesture, playlist):
    new_function = functions["Search for Playlist"] + playlist

    key = {i for i in anghami_dic if anghami_dic[i] == new_function}
    if key:
        del gesture_dic[key.pop()]

    anghami_dic[gesture] = new_function

    txt = ""
    for key, value in anghami_dic.items():
        txt += f"{key} {value}\n"

    open(ANGHAMI_FILE, "w+").write(txt)
    txt_emptylines(ANGHAMI_FILE)

#prevent overwritten in text files
def update_gesture(entry_gesture, gesture, module, function, params):
    if module != "ScreenShot":
        if not entry_gesture or not gesture:
            return False

        if entry_gesture == gesture:
            return False

    key = {i for i in gesture_dic if gesture_dic[i] == modules[module]}
    if key:
        del gesture_dic[key.pop()]

    gesture_dic[entry_gesture] = modules[module]

    txt = ""
    for key, value in gesture_dic.items():
        txt += f"{key} {value}\n"

    open(GESTURES_FILE, "w+").write(txt)
    txt_emptylines(GESTURES_FILE)

    if module == "Whatsapp":
        function = functions[function]
        whatsapp_update(gesture, function, params)
    elif module == "Control":
        function = functions[function]
        control_update(gesture, function, params)
    elif module == "Navigate":
        navigate_update(gesture, params)
    elif module == "Anghami":
        anghami_update(gesture, params)


    return True
