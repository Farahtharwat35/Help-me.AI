import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

cap = cv2.VideoCapture(0)

#####Detecting, initializing, and configuring the hands#####
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#####Accessing the speaker#####
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#####Volume Range#####
volMin, volMax = volume.GetVolumeRange()[:2]

while True:

    #Capturing images
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #List for hands
    lmList = []

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, c = img.shape  #height, width, and channels of image
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)  #draw all the landmarks

    if lmList != []:
        ##Points for thumb and index
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        ##Draw circle on tips
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)

        ##Draw a line in between
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        ##Getting length between fingers
        length = hypot(x2 - x1, y2 - y1)

        ##converting hand range to volume range
        vol = np.interp(length, [15, 220], [volMin, volMax])

        print(vol, length) #for debugging

        ##Set MasterVolume
        volume.SetMasterVolumeLevel(vol, None)

        cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break