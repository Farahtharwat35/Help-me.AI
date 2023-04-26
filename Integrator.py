# This file is for Integrating all functions into the system

def gestureChooser(gesture):
    with open('gestures.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            columns = line.split('/')
            txt_gesture = columns[0]
            txt_module = columns[1]
            txt_function = columns[2]
            # print(gesture, " ", action, " ", function)
            if gesture == txt_gesture:
                module = __import__(txt_module)
                func = getattr(module, txt_function)
                func()
