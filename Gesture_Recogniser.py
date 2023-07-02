import cv2
import mediapipe as mp
from state import map_gesture_to_function

#####Detecting, initializing, and configuring the hands#####
mpHands = mp.solutions.hands
# This line imports the hands module from the MediaPipe library and assigns it to the variable mpHands.
# This module contains the functionality for detecting and tracking hands in images and videos
hands = mpHands.Hands()
# This line creates an instance of the Hands class from the hands module, which is used to detect and track hands in an image or video.
# This line initializes the hand tracking model with default parameters.
mpDraw = mp.solutions.drawing_utils


# This line imports the drawing_utils module from the MediaPipe library and assigns it to the variable mpDraw.
# This module contains utility functions for drawing the hand landmarks and connections on an image or video frame.


def countFingers(image, results, draw=True):
    # Get the height and width of the input image.
    height, width, _ = image.shape

    # Create a copy of the input image to write the count of fingers on.
    output_image = image.copy()

    # Initialize a dictionary to store the count of fingers of both hands.
    count = {"RIGHT": 0, "LEFT": 0}

    # Store the indexes of the tips landmarks of each finger of a hand in a list.(The IDs are represented by Landmark objects,
    # which have a name attribute that indicates the name of the landmark)
    fingers_tips_ids = [
        mpHands.HandLandmark.INDEX_FINGER_TIP,
        mpHands.HandLandmark.MIDDLE_FINGER_TIP,
        mpHands.HandLandmark.RING_FINGER_TIP,
        mpHands.HandLandmark.PINKY_TIP,
    ]

    # Initialize a dictionary to store the status (i.e., True for open and False for close) of each finger of both hands.
    fingers_statuses = {
        "RIGHT_THUMB": False,
        "RIGHT_INDEX": False,
        "RIGHT_MIDDLE": False,
        "RIGHT_RING": False,
        "RIGHT_PINKY": False,
        "LEFT_THUMB": False,
        "LEFT_INDEX": False,
        "LEFT_MIDDLE": False,
        "LEFT_RING": False,
        "LEFT_PINKY": False,
        "RIGHT_THUMB_UP": False,
        "LEFT_THUMB_UP": False,
        "RIGHT_THUMB_DOWN": False,
        "LEFT_THUMB_DOWN": False,
    }

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
            if (
                hand_landmarks.landmark[tip_index].y
                < hand_landmarks.landmark[tip_index - 2].y
            ):
                # Update the status of the finger in the dictionary to true.
                fingers_statuses[hand_label.upper() + "_" + finger_name] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1

        # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
        thumb_tip_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x
        thumb_mcp_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP - 2].x
        thumb_tip_y = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].y
        thumb_mcp_y = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP - 2].y

        # Check if the thumb is up by comparing the hand label and the x-coordinates of the retrieved landmarks.
        if (hand_label == "Right" and (thumb_tip_x < thumb_mcp_x)) or (
            hand_label == "Left" and (thumb_tip_x > thumb_mcp_x)
        ):
            # Update the status of the thumb in the dictionary to true.
            fingers_statuses[hand_label.upper() + "_THUMB"] = True
            # Increment the count of the fingers up of the hand by 1.
            count[hand_label.upper()] += 1

        if (hand_label == "Right" and (thumb_tip_y < thumb_mcp_y)) or (
            hand_label == "Left" and (thumb_tip_y < thumb_mcp_y)
        ):
            # Update the status of the thumb in the dictionary to true.
            fingers_statuses[hand_label.upper() + "_THUMB_UP"] = True

        if (hand_label == "Right" and (thumb_tip_y > thumb_mcp_y)) or (
            hand_label == "Left" and (thumb_tip_y > thumb_mcp_y)
        ):
            # Update the status of the thumb in the dictionary to true.
            fingers_statuses[hand_label.upper() + "_THUMB_DOWN"] = True

    # Check if the total count of the fingers of both hands are specified to be written on the output image.
    if draw:
        # Write the total count of the fingers of both hands on the output image.
        text = "Detected " + str(sum(count.values())) + " Fingers"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        text_x = 10
        cv2.putText(
            output_image,
            text,
            (text_x, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (60, 179, 113),
            2,
        )
        # Return the output image, the status of each finger and the count of the fingers up of both hands.
    return output_image, fingers_statuses, count


def recognizeGestures(fingers_statuses, count):
    hands_labels = ["RIGHT", "LEFT"]
    hands_gestures = {"RIGHT": "UNKNOWN", "LEFT": "UNKNOWN"}
    for hand_index, hand_label in enumerate(hands_labels):
        print(hand_label, hand_index)
       # Check if the number of fingers up is 2 and the fingers that are up, are the index and the middle finger.
        if (
            count[hand_label] == 2
            and fingers_statuses[hand_label + "_MIDDLE"]
            and fingers_statuses[hand_label + "_INDEX"]
        ):
            # Update the gesture value of the hand that we are iterating upon to V SIGN.
            hands_gestures[hand_label] = "PEACE SIGN"
            print("PEACE SIGN")

        elif (
            count[hand_label] == 3
            and fingers_statuses[hand_label + "_THUMB"]
            and fingers_statuses[hand_label + "_INDEX"]
            and fingers_statuses[hand_label + "_PINKY"]
        ):
            # Update the gesture value of the hand that we are iterating upon to SPIDERMAN SIGN.
            hands_gestures[hand_label] = "SPIDERMAN SIGN"
            print("Spider SIGN")

        elif count[hand_label] == 5:
            # Update the gesture value of the hand that we are iterating upon to HIGH-FIVE SIGN.
            hands_gestures[hand_label] = "HIGH-FIVE SIGN"
            print("HIGH-FIVE SIGN")

        ####################################################################################################################

        elif count[hand_label] == 0:
            # Update the gesture value of the hand that we are iterating upon to FIST SIGN.
            hands_gestures[hand_label] = "FIST SIGN"
            print("FIST SIGN")

        #####################################################################################################################

        elif (
            count[hand_label] == 2
            and fingers_statuses[hand_label + "_THUMB"]
            and fingers_statuses[hand_label + "_PINKY"]
        ):
            # Update the gesture value of the hand that we are iterating upon to CALL SIGN.
            hands_gestures[hand_label] = "CALL SIGN"
            print("CALL SIGN")

        #####################################################################################################################

        elif (
            count[hand_label] == 3
            and fingers_statuses[hand_label + "_MIDDLE"]
            and fingers_statuses[hand_label + "_PINKY"]
            and fingers_statuses[hand_label + "_RING"]
        ):
            # Update the gesture value of the hand that we are iterating upon to PERFECTO SIGN.
            hands_gestures[hand_label] = "PERFECTO SIGN"
            print("PERFECTO SIGN")

        #####################################################################################################################

        elif count[hand_label] == 1 and fingers_statuses[hand_label + "_INDEX"]:
            # Update the gesture value of the hand that we are iterating upon to ONE SIGN WITH INDEX.
            hands_gestures[hand_label] = "ONE SIGN"
            print("ONE SIGN")

        ######################################################################################################################
        elif count[hand_label] == 1 and fingers_statuses[hand_label + "_THUMB_UP"]:
            # Update the gesture value of the hand that we are iterating upon to ONE SIGN WITH INDEX.
            hands_gestures[hand_label] = "THUMB UP SIGN"
            print("THUMB UP SIGN")

        ######################################################################################################################

        elif count[hand_label] == 1 and fingers_statuses[hand_label + "_THUMB_DOWN"]:
            # Update the gesture value of the hand that we are iterating upon to ONE SIGN WITH INDEX.
            hands_gestures[hand_label] = "THUMB DOWN SIGN"
            print("THUMB DOWN SIGN")

    return hands_gestures


cap = cv2.VideoCapture(0)  # default 0
# to make a specific window with resolution 960*1280
cap.set(3, 1280)
cap.set(4, 960)

while True:
    # Capturing images
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        img, fingers_statuses, count = countFingers(img, results)
        myGesture = recognizeGestures(fingers_statuses, count)
        print("VAluessss", myGesture)
        map_gesture_to_function(myGesture["RIGHT"])
        for handlandmark in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(
                img, handlandmark, mpHands.HAND_CONNECTIONS
            )  # draw all the landmarks

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
