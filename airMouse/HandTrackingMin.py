import cv2
import mediapipe as mp
import time

import mouseControl as mouseC


def checkClick(indexY, clickY):
    if indexY > clickY:
        mouseC.clickMouse()


if __name__ == '__main__':

    while True:

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        cap = cv2.VideoCapture(0)

        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils

        cTime = 0
        pTime = 0

        success, img = cap.read()

        # inverts image
        img = cv2.flip(img, 1)

        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRBG)


        xVal8 = 0
        yVal8 = 0

        xVal4 = 0
        yVal4 = 0

        # print(results.multi_hand_landmarks)
        if (results.multi_hand_landmarks):

            for handLms in results.multi_hand_landmarks:
                # get tip of index finger ( 8 )

                lm8 = handLms.landmark[8]
                h, w, c = img.shape

                xVal8, yVal8 = int(lm8.x * w), int(lm8.y * h)

                # get tip of thumb ( 4 )
                lm8 = handLms.landmark[4]
                h, w, c = img.shape

                # gets x and y values for tip of thumb
                xVal4, yVal4 = int(lm8.x * w), int(lm8.y * h)

                # print(handLms, "ed")


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        # mouseC.moveTo(xVal8, yVal8)

        # checks if mouse should click
        # checkClick(yVal8, yVal4)

        # calculates fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # draws text
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (0, 0, 255), 2)
        cv2.putText(img, "Finger", (xVal8, yVal8), cv2.FONT_ITALIC, 3, (0,0,255), 2)
        cv2.circle(img, (xVal8, yVal8), 25, (255, 0, 0), 10)
        cv2.circle(img, (xVal4, yVal4), 25, (0, 255, 0), 10)

        #shows screen
        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)

        # time.sleep(.01)

