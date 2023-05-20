# Program tasks
import pyautogui
import time
#import subprocess
import os

# Mina
def open_Anghami():
    app_path = r"C:\Users\rafik\AppData\Local\anghami\Anghami.exe"
    #subprocess.call("Anghami")
    os.startfile(app_path)

# Search for a playlist and shuffle play
def search_playlist(playlistName):
    pyautogui.click(x=245, y=300)           # Go to the "Your Library"
    time.sleep(1)

    pyautogui.click(x=450, y=570)           # Go to the "Playlists"
    time.sleep(1)

    pyautogui.click(x=1660, y=163)          # Click on Search Bar
    time.sleep(1)

    pyautogui.typewrite(playlistName)       # Enter Playlist Name
    time.sleep(1)

    pyautogui.click(x=700, y=300)           # Go to the Desired Playlist
    time.sleep(2)

    pyautogui.click(x=570, y=450)           # Select Menu
    time.sleep(1)

    pyautogui.click(x=570, y=500)           # Shuffle play


