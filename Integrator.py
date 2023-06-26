# This file is for Integrating all functions into the system
# This function chooses the first gesture which is the start of every sequence of gestures.
# Then the other functions are focused on executing the sequence
# import time
def gestureChooser_main(gesture, flag1: bool, modules) -> bool:
    if flag1:
        with open('./database/Gestures.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split('/')
                txt_gesture = columns[0]
                txt_module = columns[1]
                txt_function = columns[2]
                txt_sequence = columns[3]
                # print(gesture, " ", action, " ", function)
                if gesture == txt_gesture:
                    modules.append(txt_module)
                    module = __import__(txt_module)
                    func = getattr(module, txt_function)
                    func()
                    # time.sleep(0.7)
                    if txt_sequence == "TRUE":
                        return False
            return flag1
    else:
        return gestureChooser_side(gesture, flag1, modules)


def gestureChooser_side(gesture, flag1: bool, modules) -> bool:
    #print("Da5alttttttttt")
    print(modules)
    with open("./database/" + modules[-1] + '.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            columns = line.split('/')
            txt_gesture = columns[0]
            txt_module = columns[1]
            txt_function = columns[2]
            if columns[-1] is not txt_function:
                txt_attribute = columns[3:]
                print(txt_attribute)
            if gesture == txt_gesture:
                module = __import__(txt_module)
                func = getattr(module, txt_function.strip())
                if columns[-1] is not txt_function:
                    func(*txt_attribute)
                else:
                    func()
                # Give Time for next Function Call
                # time.sleep(0.7)
            if gesture == "FIST SIGN":
                return True
        return False