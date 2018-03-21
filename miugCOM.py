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
    while True: 
        (grabbed, frame) = camera.read()

        if args.get("video") and not grabbed:
            break                            
        frame = imutils.resize(frame, width=600)
        
        grey = np.zeros((frame.shape[0], frame.shape[1])) # init 2D numpy array
        # get row number
        for rownum in range(len(frame)):
            for colnum in range(len(frame[rownum])):
                grey[rownum][colnum] = np.average(frame[rownum][colnum])

        com = ndimage.measurements.center_of_mass(grey)
        #print("beginning")
        print(com)
        for i in xrange(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        
        #if cv2.getWindowProperty('Frame', 0) == -1:
            #print("b1")
            #break
        if key == ord("q"):
            print("b2")
            break
    camera.release()
    cv2.destroyAllWindows()
run_camera()

