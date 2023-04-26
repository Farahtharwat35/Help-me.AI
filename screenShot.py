import time
from PIL import ImageGrab
from datetime import datetime
def take_screenshot():
    screenshot = ImageGrab.grab()
    readable_time = datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d0_%H_%M_%S')
    screenshot.save(f"{readable_time}.jpg")
def printTest():
    print("ALOOO YA 3AAALAM")