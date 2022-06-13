#importing libraries
from flask import Flask, render_template, Response
import cv2
import os
import time
scores = []
start = 0
end = 0
distractionStart = 0
distracted = False
distractionStarting = False
focusSession = False
cascadePath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
video = cv2.VideoCapture(0)
bottomX = 0
bottomY = 0
faceWidth = 0
faceLength = 0
exit = False  
ret, frame = video.read()
while True:
    ret, frame = video.read()
    cv2.putText(frame, str(scores), (540,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
    if(distracted):
        bottomX = 0
        bottomY = 0
        faceWidth = 0
        faceLength = 0
        exit = False  
        start = 0
        end = 0
        distractionStart = 0
        distractionStarting = False
        focusSession = False
    ret, frame = video.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayscale, scaleFactor=1.1, minSize=(120,120), flags=cv2.CASCADE_SCALE_IMAGE)
    for(minX, minY, width, height) in faces:
        cv2.rectangle(frame, (minX,minY), (minX+width, minY+height), (0,255,0),2)
        if(focusSession==False):
            #print("Revival")
            start = time.time()
            #print(start)
            bottomX = minX
            bottomY = minY
            faceWidth = width
            faceLength = height 
            focusSession = True 
            distracted = False
        if((distractionStarting==False) and (time.time()-start>10) and (minX<bottomX-50 or minX>bottomX+50 or minY<bottomY-50 or minY>bottomY+50)):
            #print("Please")
            distractionStart = time.time()
            distractionStarting = True
        if((distractionStarting==True) and (time.time()-distractionStart>5)):
            #print("distracted")
            end = time.time()
            distracted = True
            times = int(end-start)
            minutes = int(times/60)
            sec = times-60*minutes
            minutes = str(minutes)
            seconds = str(sec-10)
            Minutes = minutes.zfill(2)
            Seconds = seconds.zfill(2)
            focusSession=False
            scores.append(str(Minutes)+":"+str(Seconds))
            
        if ((distractionStarting==True) and (time.time()-start>10) and (minX<bottomX-50 or minX>bottomX+50)):
            cv2.putText(frame, "Distracted: session will end in " + str(5-int(time.time()-distractionStart)), (420,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        else:
            distractionStarting=False
        times = int(time.time()-start)
        minutes = int(times/60)
        sec = times-60*minutes
        minutes = str(minutes)
        seconds = str(sec-10)
        Minutes = minutes.zfill(2)
        Seconds = (seconds).zfill(2)
        if(sec>10):
            cv2.putText(frame, "Time focused: " + str(Minutes)+":"+str(Seconds), (30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        cv2.putText(frame, "Past scores:", (970,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        cv2.putText(frame, "Type q to quit", (20,420),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        if(time.time()-start<10):
            cv2.putText(frame, "Focus session will start in:  " + str(10-int(time.time()-start)), (420,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        for i in range(len(scores)):
            cv2.putText(frame, scores[i], (970,90+90*i),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
        if((distractionStarting==True) and (time.time()-distractionStart>5)):
            cv2.putText(frame, "Sorry you were distracted", (460,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_4,False)
    cv2.imshow('Video',frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit = True
        end = time.time()
    
    #print(str(bottomX)+" "+str(bottomY)+" "+str(faceWidth)+" "+str(faceLength))
    if(exit==True):
        break
    continue