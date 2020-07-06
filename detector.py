import cv2
import numpy as np
import pandas as pd

import sqlite3

class DB:
    def openDB(self):
        conn = sqlite3.connect('database/database.db')
        print("opened database successfully")
        cursor = conn.execute("SELECT sessionid, date, query, positive, negative from MiningReport;")

        data = []
        
        for row in cursor:
            datarow = [row[0],row[1],row[2],row[3],row[4]]
            data.append(datarow)
            df = pd.DataFrame(data,columns=['Session ID','Date','Query','Positive%','Negative%'])
        print(df)

        conn.close()

def function():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "./Classifiers/face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)
    flag=0
    i=0
    while (i<60):
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print(Id, conf)
            if(Id==1):
               Id="Jenit"
               if(conf>=45.0):
                   flag=1
            elif(Id==2):
               Id="Jenit"
            elif(Id==3):
               Id="Abhishek"
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
        cv2.imshow('Face detection',im) 
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
        i=i+1

    if(flag==1):
        obj=DB()
        obj.openDB()
    
    cam.release()
    cv2.destroyAllWindows()
