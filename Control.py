from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import subprocess
import pyautogui
#####Accessing the speaker#####
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#####Volume Range#####
volMin, volMax = volume.GetVolumeRange()[:2]


def Enter():
    print("Entered Controls:...")
def VolumeUP():
    currentVolume = volume.GetMasterVolumeLevel()
    if volMin <= currentVolume < volMax:
        if volMin <= currentVolume <= -24.0:
            currentVolume += 0.5
        elif -24 < currentVolume <= -15.0:
            currentVolume += 0.2
        elif -15 < currentVolume <= -10:
            currentVolume += 0.15
        else:
            if currentVolume + 0.1 < volMax:
                currentVolume += 0.1
            else:
                currentVolume = volMax
    # print(volMin, volMax)
    volume.SetMasterVolumeLevel(currentVolume, None)
def VolumeDOWN():
    currentVolume = volume.GetMasterVolumeLevel()
    if volMin <= currentVolume <= volMax:
        if -10 <= currentVolume <= volMax:
            currentVolume -= 0.05
        elif -10 > currentVolume >= -15.0:
            currentVolume -= 0.08
        elif -15 > currentVolume >= -24:
            currentVolume -= 0.1
        else:
            if currentVolume - 0.4 > volMin:
                currentVolume -= 0.4
            else:
                currentVolume = volMin
    # print(volMin, volMax)
    volume.SetMasterVolumeLevel(currentVolume, None)

# Mina
def scrollUP():
    pyautogui.scroll(25)
    print("SCROLLING UPPP")
def scrollDOWN():
    pyautogui.scroll(-25)
    print("SCROLLING DOWN")
# Brwana
def open_program(program):
    print(f"opening program {program}")
    subprocess.call([program])