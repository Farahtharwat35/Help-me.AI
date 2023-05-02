# This file is for Integrating all functions into the system
# This function chooses the first gesture which is the start of every sequence of gestures.
# Then the other functions are focused on executing the sequence
import time
#TODO:Try to make one function @Farah
def gestureChooser_main(gesture, flag1, modules):
    if flag1[0]:
        with open('gestures.txt', 'r') as file:
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
                        flag1[0] = False
    else:
        gestureChooser_side(gesture, flag1, modules)


def gestureChooser_side(gesture, flag1, modules):
    print("Da5alttttttttt")
    print(modules)
    with open(modules[-1] + '.txt', 'r') as file:
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
                flag1[0] = True