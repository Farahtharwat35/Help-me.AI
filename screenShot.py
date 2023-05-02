import time
from PIL import ImageGrab
from datetime import datetime
def take_screenshot():
    screenshot = ImageGrab.grab()
    readable_time = datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d0_%H_%M_%S')
    screenshot.save(f"{readable_time}.jpg")
    time.sleep(1)

# def printTest1():
#     print("ALOOO YA 3LAAAM")
# def printTest3(name):
#     print("ALOOO YA " + name)
# def printTest2(name1,name2):
#     print("MLOOK EL AI " + name1 + " " + name2)