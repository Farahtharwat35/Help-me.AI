import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import matplotlib.pyplot as plt


#####Detecting, initializing, and configuring the hands#####
mpHands = mp.solutions.hands
#This line imports the hands module from the MediaPipe library and assigns it to the variable mpHands.
#This module contains the functionality for detecting and tracking hands in images and videos
hands = mpHands.Hands()
#This line creates an instance of the Hands class from the hands module, which is used to detect and track hands in an image or video.
#This line initializes the hand tracking model with default parameters.
mpDraw = mp.solutions.drawing_utils
#This line imports the drawing_utils module from the MediaPipe library and assigns it to the variable mpDraw.
#This module contains utility functions for drawing the hand landmarks and connections on an image or video frame.


def countFingers(image, results, draw=True, display=True):

    # Get the height and width of the input image.
    height, width, _ = image.shape

    # Create a copy of the input image to write the count of fingers on.
    output_image = image.copy()

    # Initialize a dictionary to store the count of fingers of both hands.
    count = {'RIGHT': 0, 'LEFT': 0}

    # Store the indexes of the tips landmarks of each finger of a hand in a list.(The IDs are represented by Landmark objects,
    # which have a name attribute that indicates the name of the landmark)
    fingers_tips_ids = [mpHands.HandLandmark.INDEX_FINGER_TIP, mpHands.HandLandmark.MIDDLE_FINGER_TIP,
                        mpHands.HandLandmark.RING_FINGER_TIP, mpHands.HandLandmark.PINKY_TIP]

    # Initialize a dictionary to store the status (i.e., True for open and False for close) of each finger of both hands.
    fingers_statuses = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False,
                        'RIGHT_PINKY': False, 'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False,
                        'LEFT_RING': False, 'LEFT_PINKY': False}

    # Iterate over the found hands in the image. hand_info contains ClassificationList object for each hand,
    for hand_index, hand_info in enumerate(results.multi_handedness):

        # Retrieve the label of the found hand= access the handedness information for each hand using the ClassificationList.classification attribute,
        # which is a list of ClassificationResult objects.)
        hand_label = hand_info.classification[0].label

        # Retrieve the landmarks of the found hand.
        hand_landmarks = results.multi_hand_landmarks[hand_index]

        # Iterate over the indexes of the tips landmarks of each finger of the hand.
        for tip_index in fingers_tips_ids:

            # Retrieve the label (i.e., index, middle, etc.) of the finger on which we are iterating upon.
            finger_name = tip_index.name.split("_")[0]

            # Check if the finger is up by comparing the y-coordinates of the tip and pip landmarks.
            if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y):
                # Update the status of the finger in the dictionary to true.
                fingers_statuses[hand_label.upper() + "_" + finger_name] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1

        # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
        thumb_tip_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x
        thumb_mcp_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP - 2].x

        # Check if the thumb is up by comparing the hand label and the x-coordinates of the retrieved landmarks.
        if (hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or (
                hand_label == 'Left' and (thumb_tip_x > thumb_mcp_x)):
            # Update the status of the thumb in the dictionary to true.
            fingers_statuses[hand_label.upper() + "_THUMB"] = True

            # Increment the count of the fingers up of the hand by 1.
            count[hand_label.upper()] += 1

    # Check if the total count of the fingers of both hands are specified to be written on the output image.
    if draw:
        # Write the total count of the fingers of both hands on the output image.
        cv2.putText(output_image, " Total Fingers: ", (10, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (20, 255, 155), 2)
        cv2.putText(output_image, str(sum(count.values())), (width // 2 - 150, 240), cv2.FONT_HERSHEY_SIMPLEX,
                    8.9, (20, 255, 155), 10, 10)

    # # Check if the output image is specified to be displayed.
    # if display:
    #     print ("outttt")
    #     # Display the output image.
    #     plt.figure(figsize=[10, 10])
    #     plt.imshow(output_image[:, :, ::-1]);
    #     plt.title("Output Image");
    #     plt.axis('off');

    # Otherwise
    #else:

        # Return the output image, the status of each finger and the count of the fingers up of both hands.
    return output_image, fingers_statuses, count


def recognizeGestures(image, fingers_statuses, count):

    # Create a copy of the input image.
    output_image = image.copy()

    # Store the labels of both hands in a list.
    hands_labels = ['RIGHT', 'LEFT']

    # Initialize a dictionary to store the gestures of both hands in the image.
    hands_gestures = {'RIGHT': "UNKNOWN", 'LEFT': "UNKNOWN"}

    # Iterate over the left and right hand.
    for hand_index, hand_label in enumerate(hands_labels):

        # Check if the person is making the 'Peace Sign' gesture with the hand.
        ####################################################################################################################

        # Check if the number of fingers up is 2 and the fingers that are up, are the index and the middle finger.
        if count[hand_label] == 2 and fingers_statuses[hand_label + '_MIDDLE'] and fingers_statuses[hand_label + '_INDEX']:

            # Update the gesture value of the hand that we are iterating upon to V SIGN.
            hands_gestures[hand_label] = "PEACE SIGN"
            print("PEACE SIGN")

        ####################################################################################################################

        # Check if the person is making the 'SPIDERMAN' gesture with the hand.
        ##########################################################################################################################################################

        # Check if the number of fingers up is 3 and the fingers that are up, are the thumb, index and the pinky finger.
        elif count[hand_label] == 3 and fingers_statuses[hand_label + '_THUMB'] and fingers_statuses[
            hand_label + '_INDEX'] and fingers_statuses[hand_label + '_PINKY']:

            # Update the gesture value of the hand that we are iterating upon to SPIDERMAN SIGN.
            hands_gestures[hand_label] = "SPIDERMAN SIGN"
            print("Spider SIGN")

        ##########################################################################################################################################################

        # Check if the person is making the 'HIGH-FIVE' gesture with the hand.
        ####################################################################################################################

        # Check if the number of fingers up is 5, which means that all the fingers are up.
        elif count[hand_label] == 5:

            # Update the gesture value of the hand that we are iterating upon to HIGH-FIVE SIGN.
            hands_gestures[hand_label] = "HIGH-FIVE SIGN"
            print("HIGH-FIVE SIGN")

        ####################################################################################################################

        #elif count[hand_label]==1 and fingers_statuses[hand_label + '_THUMB']

        # Return the output image and the gestures of the both hands.
        return output_image, hands_gestures


cap = cv2.VideoCapture(0) # default 0
#cap.set(3,1280) to make a specific winodw with resolution 960*1280
#cap.set(4,960)


#####Accessing the speaker#####
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#####Volume Range#####
volMin, volMax = volume.GetVolumeRange()[:2]
print (volMin,volMax)
volumeFlag = False;

while True:

    #Capturing images
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #The results variable contains the output of the hand landmark detection,
    # which includes information such as the 3D coordinates of each hand landmark, the hand's pose,
    # and the handedness (left or right hand).
    results = hands.process(imgRGB)

    #List for hands
    lmList = []

    if results.multi_hand_landmarks:
        img, fingers_statuses, count = countFingers(img, results, display=False)
        _,myGesture = recognizeGestures(img, fingers_statuses, count)
        HIGH_FIVE_SIGN="HIGH-FIVE SIGN"
        if  HIGH_FIVE_SIGN in myGesture.values():
            volumeFlag = True;
        for handlandmark in results.multi_hand_landmarks:
            # This line loops through each individual landmark point in the currentVolume set of hand landmarks.
            # The landmark property of the handlandmark object contains a list of 21 (x, y, z) coordinates for each hand landmark detected in the image or video frame.
            for id, lm in enumerate(handlandmark.landmark):
                h, w, c = img.shape  #height, width, and channels of image
                cx, cy = int(lm.x * w), int(lm.y * h)
                #(This line calculates the (x, y) coordinates of the currentVolume landmark point by multiplying its normalized (x, y) coordinates (in the range [0, 1]) with the width and height of the image, respectively, and converting the result to an integer value.
                # This gives the pixel coordinates of the landmark point in the image.
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)  #draw all the landmarks

    two=2
    three=3

    if lmList != []:

        ##Set MasterVolume
        if (volumeFlag):
            print ("FLAGG")
            # ##Points for thumb and index
            # x1, y1 = lmList[4][1], lmList[4][2]
            # x2, y2 = lmList[8][1], lmList[8][2]
            #
            # ##Draw circle on tips
            # cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)

            # ##Draw a line in between
            # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            #
            # ##Getting length between fingers
            # length = hypot(x2 - x1, y2 - y1)

            # for i in count.values() :
            #     print(i)

            if two in count.values() or three in count.values():
                ##converting hand range to volume range
                #vol = np.interp(length, [60, 260], [volMin, volMax])
                # #print(vol, length)  # for debugging
                currentVolume=volume.GetMasterVolumeLevel()
                print("currentVolume ",currentVolume)

                if (two in count.values()):
                    if (currentVolume  >= volMin and currentVolume < volMax):
                        print("da5alt")
                        if (currentVolume >=volMin and currentVolume <= -24.0  ):
                            currentVolume+= 0.5
                        elif (currentVolume > -24  and currentVolume <= -15.0 ):
                            currentVolume += 0.2
                        elif (currentVolume > -15 and currentVolume <= -10):
                            currentVolume += 0.15
                        else:
                            if(currentVolume+0.1<volMax):
                                currentVolume += 0.1
                            else :
                                currentVolume=volMax

                else :
                    print("elseee")
                    if (currentVolume  >= volMin and currentVolume <= volMax):
                        print("twooooooo")
                        if (currentVolume >=-10 and currentVolume <= volMax  ):
                            print(("dou7aa"))
                            currentVolume-= 0.05
                        elif (currentVolume < -10  and currentVolume >= -15.0 ):
                            currentVolume -= 0.08
                        elif (currentVolume < -15 and currentVolume >= -24):
                            currentVolume -= 0.1
                        else:
                            if(currentVolume-0.4>volMin):
                                currentVolume -= 0.4
                            else :
                                currentVolume=volMin


                print("currentVolume 2: ", currentVolume)
                volume.SetMasterVolumeLevel(currentVolume, None)



        indexX = 0
        indexY = 0
        indexMid = 0
        handBottomX = 0
        handBottomY = 0
        pinkyX = 0
        pinkyY = 0
        fistWarning = "Fist!"
        ThumbY = 0
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
            elif lms[0] == 8:
                indexY = lms[2]
            elif lms[0] == 4:
                ThumbY = lms[2]
        if ThumbY == indexY:
            flag = True
        if (middleY < handBottomY) and (ringY < handBottomY) and (pinkyY < handBottomY) and (middleY > middleBottomY) and (ringY > ringBottomY) and (pinkyY>pinkyBottomY):
            #cv2.rectangle(handsFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            #cv2.putText(handsFrame, fistWarning, (pinkyX + 2, indexY - 2), (font), .7,(0, 0, 255), 1, cv2.LINE_4)
            print("Fist!!")
            volumeFlag = False

    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
     break

