import cv2
import mediapipe as mp
import pyautogui as pg
import HandTrackingModule as htm

import time
from pynput.keyboard import Controller,Key
detector=htm.HandDetector()
keyboard = Controller()
cap=cv2.VideoCapture(0)

while True:
        success,img=cap.read()
        img = cv2.flip(img, 1)
        img=cv2.resize(img,(1000,600))
        hands,_=detector.findHands(img)
        delayCounter=0
        if hands:
                lmList=[]
                lmListLe = []
                if len(hands) > 1:
                        if hands[0]['type'] == 'Right':
                                lmList = hands[0]['lmList']
                                lmListLe = hands[1]['lmList']
                        else:
                                lmListLe = hands[0]['lmList']
                                lmList = hands[1]['lmList']
                else:
                        if hands[0]['type'] == 'Right':
                                lmList = hands[0]['lmList']
                        if hands[0]['type'] == 'Left':
                                lmListLe = hands[0]['lmList']
                if lmListLe:
                        l, _, _ = detector.findDistance(lmListLe[8][:2], lmListLe[12][:2], img)
                        if l < 50:
                                keyboard.press(Key.left)
                        else:
                                keyboard.release(Key.left)
                if lmList:
                        l, _, _ = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
                        l1,_,_=detector.findDistance(lmList[4][:2],lmList[8][:2],img)
                        if l < 50:
                                keyboard.press(Key.right)
                        else:
                                keyboard.release(Key.right)
                        if l1<50:
                                keyboard.press(Key.enter)
                        else:
                                keyboard.release(Key.enter)

        cv2.imshow("Hill Climbing",img)
        cv2.waitKey(1)

