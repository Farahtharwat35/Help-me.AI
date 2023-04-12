import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

cap = cv2.VideoCapture(0) # default 0

#####Detecting, initializing, and configuring the hands#####
mpHands = mp.solutions.hands # This line imports the hands module from the MediaPipe library and assigns it to the variable mpHands.
                            # This module contains the functionality for detecting and tracking hands in images and videos
hands = mpHands.Hands() #This line creates an instance of the Hands class from the hands module, which is used to detect and track hands in an image or video.
                        # This line initializes the hand tracking model with default parameters.
mpDraw = mp.solutions.drawing_utils #This line imports the drawing_utils module from the MediaPipe library and assigns it to the variable mpDraw.
                    # This module contains utility functions for drawing the hand landmarks and connections on an image or video frame.

#####Accessing the speaker#####
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#####Volume Range#####
volMin, volMax = volume.GetVolumeRange()[:2]
flag= True
while True:

    #Capturing images
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #List for hands
    lmList = []

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            # This line loops through each individual landmark point in the current set of hand landmarks.
            # The landmark property of the handlandmark object contains a list of 21 (x, y, z) coordinates for each hand landmark detected in the image or video frame.
            for id, lm in enumerate(handlandmark.landmark):
                h, w, c = img.shape  #height, width, and channels of image
                cx, cy = int(lm.x * w), int(lm.y * h) # (This line calculates the (x, y) coordinates of the current landmark point by multiplying its normalized (x, y) coordinates (in the range [0, 1]) with the width and height of the image, respectively, and converting the result to an integer value.
                # This gives the pixel coordinates of the landmark point in the image.)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)  #draw all the landmarks

    if lmList != []:

        ##Set MasterVolume
        if (flag ):
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
            vol = np.interp(length, [60, 260], [volMin, volMax])

            print(vol, length)  # for debugging

            volume.SetMasterVolumeLevel(vol, None)

        indexX = 0
        indexY = 0
        indexMid = 0
        handBottomX = 0
        handBottomY = 0
        pinkyX = 0
        pinkyY = 0
        fistWarning = "Fist!"
        ThumbY=0
        for lms in lmList:
            if lms[0] == 9:
                middleBottomY = lms[2]
            elif lms[0] == 13:
                ringBottomY = lms[2]
            elif lms[0] == 17:
                pinkyBottomY = lms[2]
            elif lms[0] == 11:
                middleY = lms[2]
            # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
            elif lms[0] == 15:
                ringY = lms[2]
            # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
            elif lms[0] == 19:
                pinkyX, pinkyY = lms[1], lms[2]
                # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
            elif lms[0] == 0:
                handBottomX, handBottomY = lms[1], lms[2]
            elif lms[0]== 8 :
                indexY=lms[2]
            elif lms [0]==4 :
                ThumbY=lms[2]
        if(ThumbY==indexY):
            flag=True

        if (middleY < handBottomY) and (ringY < handBottomY) and (pinkyY < handBottomY) and (middleY > middleBottomY) and (ringY > ringBottomY) and (pinkyY>pinkyBottomY):
            #cv2.rectangle(handsFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            #cv2.putText(handsFrame, fistWarning, (pinkyX + 2, indexY - 2), (font), .7,(0, 0, 255), 1, cv2.LINE_4)
           # print("Fist!!")
            flag=False


    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
     break

