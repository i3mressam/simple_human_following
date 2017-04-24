

from collections import deque
import numpy as np
import argparse
import freenect
import imutils
import cv2
import serial
from time import sleep

ser = serial.Serial("/dev/ttyACM1",9600)

#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-b", "--buffer", type=int, default=10,
        help="max buffer size")
args = vars(ap.parse_args())


blueLower = (110, 50, 50)
blueUpper = (130, 255, 255)
pts = deque(maxlen=args["buffer"])


# to the kinect

camera = get_video()

# keep looping
while True:

        # grab the current frame
        frame = get_video()

        

        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=1280)
        # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "blue", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size
                if radius > 500:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("a")
                elif (radius > 150 and radius < 175) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("b")
                elif (radius > 120 and radius < 150) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("c")
                elif (radius > 85 and radius < 120) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("d")        
                elif (radius > 50 and radius < 85) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("e")
                elif (radius > 20 and radius < 50) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("f")
                elif (radius > 10 and radius < 20) and (x > 600 and x < 680) :
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("g")
                #forward spd1
                elif (radius > 150 and radius < 175) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("h")
                elif (radius > 150 and radius < 175) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("i")
                elif (radius > 150 and radius < 175) and (x > 1080 and x <= 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("j")
                elif (radius > 150 and radius < 175) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("k")
                elif (radius > 150 and radius < 175) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("l")
                elif (radius > 150 and radius < 175) and (x < 200 and x >= 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("m")
                #forward spd2                        
                elif (radius > 120 and radius < 150) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("n")
                elif (radius > 120 and radius < 150) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("o")
                elif (radius > 120 and radius < 150) and (x > 1080 and x < 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("p")
                elif (radius > 120 and radius < 150) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("q")
                elif (radius > 120 and radius < 150) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("r")
                elif (radius > 120 and radius < 150) and (x < 200 and x > 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("s")
                #forward spd3
                elif (radius > 85 and radius < 120) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("t")
                elif (radius > 85 and radius < 120) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("u")
                elif (radius > 85 and radius < 120) and (x > 1080 and x < 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("v")
                elif (radius > 85 and radius < 120) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("w")
                elif (radius > 85 and radius < 120) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("x")
                elif (radius > 85 and radius < 120) and (x < 200 and x > 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("y")
               #forward spd4
                elif (radius > 50 and radius < 85) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("z")
                elif (radius > 50 and radius < 85) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("aa")
                elif (radius > 50 and radius < 85) and (x > 1080 and x < 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ab")
                elif (radius > 50 and radius < 85) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ac")
                elif (radius > 50 and radius < 85) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ad")
                elif (radius > 50 and radius < 85) and (x < 200 and x > 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ae")
               #forward spd5
                elif (radius > 20 and radius < 50) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("af")
                elif (radius > 20 and radius < 50) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ag")
                elif (radius > 20 and radius < 50) and (x > 1080 and x < 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ah")
                elif (radius > 20 and radius < 50) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ai")
                elif (radius > 20 and radius < 50) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("aj")
                elif (radius > 20 and radius < 50) and (x < 200 and x > 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ak")
               #forward spd6
                elif (radius > 10 and radius < 20) and (x > 680 and x < 880): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("al")
                elif (radius > 10 and radius < 20) and (x > 880 and x < 1080): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("am")
                elif (radius > 10 and radius < 20) and (x > 1080 and x < 1280): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("an")
                elif (radius > 10 and radius < 20) and (x < 600 and x > 400): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ao")
                elif (radius > 10 and radius < 20) and (x < 400 and x > 200): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("ap")
                elif (radius > 10 and radius < 20) and (x < 200 and x > 0): 
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        ser.write("aq")         
                #stop        
                else:
                        
                        ser.write("g")
                        
                               
        # update the points queue
        pts.appendleft(center)

        # loop over the set of tracked points
        for i in xrange(1, len(pts)):
                # if either of the tracked points are None, ignore
                # them
                if pts[i - 1] is None or pts[i] is None:
                        ser.write("d")
                        
                # otherwise, compute the thickness of the line and
                # draw the connecting lines
                thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
                cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

        # show the frame to our screen
        cv2.imshow("Frame", frame)
        
        key = cv2.waitKey(1) & 0xFF
        

        


