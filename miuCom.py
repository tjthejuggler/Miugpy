import colorsys
import math
from math import hypot
from tkinter import * #for widgets
import tkinter as ttk #for widgets
from tkinter.scrolledtext import ScrolledText
import time #for sending midi
import rtmidi #for sending midi
import numpy as np #for webcam
import cv2 #for webcam
from collections import deque # for tracking balls
import argparse # for tracking balls
import imutils # for tracking balls
import sys # for tracking balls
from tkinter import messagebox
import pyautogui
import time
import pyHook
import pythoncom
import win32com.client
from tkinter.filedialog import askopenfilename
from scipy import ndimage
import matplotlib.pyplot as plt
shell = win32com.client.Dispatch("WScript.Shell")
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output")
root = Tk() 
root.title("Miug")
def run_camera():    
    PY3 = sys.version_info[0] == 3
    if PY3:
        xrange = range
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
            help="path to the (optional) video file")
    ap.add_argument("-b", "--buffer", type=int, default=64,
            help="max buffer size")
    args = vars(ap.parse_args())
    pts = deque(maxlen=args["buffer"])
    camera = cv2.VideoCapture(0)
    all_cx = []
    all_cy = []
    frames = 0
    while True and frames < 200: 
        (grabbed, frame) = camera.read()
        frames = frames + 1
        print("frame:" + str(frames))
        if args.get("video") and not grabbed:
            break                            
        frame = imutils.resize(frame, width=600)
        
        #grey = np.zeros((frame.shape[0], frame.shape[1])) # init 2D numpy array
        framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        ret,thresh = cv2.threshold(framegray,127,255,0)
        #thresh = cv2.adaptiveThreshold(framegray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            cnt = contours[0]
            M = cv2.moments(cnt)
            #print M
            if M['m00'] > 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                all_cx.append(cx)
                all_cy.append(cy)
                print("cx : "+str(cx)+",cy :"+str(cy))


        for i in xrange(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        
        #if cv2.getWindowProperty('Frame', 0) == -1:
            #print("b1")
            #break
        if key == ord("q"):
            print("b2")
            break
    camera.release()
    cv2.destroyAllWindows()
    line1 = plt.plot(all_cx, label="x")
    line2 = plt.plot(all_cy, label="y")
    plt.legend([line1, line2],['X', 'Y'])
    plt.show()

run_camera()
