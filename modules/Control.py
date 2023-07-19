# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
import subprocess
import pyautogui

# Accessing the speaker
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # Volume Range
# volMin, volMax = volume.GetVolumeRange()[:2]


def Enter():
    print("Entered Controls:...")


def VolumeUP():
    current_volume = volume.GetMasterVolumeLevel()
    if volMin <= current_volume < volMax:
        if volMin <= current_volume <= -24.0:
            current_volume += 0.5
        elif -24 < current_volume <= -15.0:
            current_volume += 0.2
        elif -15 < current_volume <= -10:
            current_volume += 0.15
        else:
            if current_volume + 0.1 < volMax:
                current_volume += 0.1
            else:
                current_volume = volMax
    # print(volMin, volMax)
    volume.SetMasterVolumeLevel(current_volume, None)


def VolumeDOWN():
    current_volume = volume.GetMasterVolumeLevel()
    if volMin <= current_volume <= volMax:
        if -10 <= current_volume <= volMax:
            current_volume -= 0.05
        elif -10 > current_volume >= -15.0:
            current_volume -= 0.08
        elif -15 > current_volume >= -24:
            current_volume -= 0.1
        else:
            if current_volume - 0.4 > volMin:
                current_volume -= 0.4
            else:
                current_volume = volMin
    # print(volMin, volMax)
    volume.SetMasterVolumeLevel(current_volume, None)


def scrollUP():
    pyautogui.scroll(50)
    print("SCROLLING UP")


def scrollDOWN():
    pyautogui.scroll(-50)
    print("SCROLLING DOWN")


def open_program(program):
    print(f"opening program {program}")
    subprocess.call([program])
