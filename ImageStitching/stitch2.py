import cv2
import numpy as np

##选择摄像头
videoLeftUp = cv2.VideoCapture(0)
videoRightUp = cv2.VideoCapture(1)

width = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while (videoLeftUp.isOpened()):
    retLeftUp, frameLeftUp = videoLeftUp.read()
    retRightUp, frameRightUp = videoRightUp.read()

    frameLeftUp = cv2.resize(frameLeftUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
    frameRightUp = cv2.resize(frameRightUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)

    frameUp = np.hstack((frameLeftUp, frameRightUp))

    cv2.imshow('frame', frameUp)
    key = cv2.waitKey(10)
    if int(key) == 113:
        break

videoLeftUp.release()
videoRightUp.release()