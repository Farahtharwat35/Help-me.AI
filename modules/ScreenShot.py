import time
from PIL import ImageGrab
from datetime import datetime
def take_screenshot():
    screenshot = ImageGrab.grab()
    readable_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H_%M_%S')
    screenshot.save(f"./Screenshots/{readable_time}.jpg")
