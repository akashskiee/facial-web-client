import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import sqlite3
import tkinter.ttk as ttk
import tkinter.font as font
import pandas as pd
from tkinter import messagebox

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1280x720')
window.configure(background='#153b3b')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)



message = tk.Label(window, text="Face Recognition Based Attendance" ,bg="#a53b3b"  ,fg="white"  ,width=50  ,height=3,font=("Courier New",30,'bold')) 
message.place(x=200, y=20)

lbl = tk.Label(window, text="Enter Your Student ID",width=28  ,height=2  ,fg="black"  ,bg="light blue" ,font=('times', 15, ' bold ') ) 
lbl.place(x=200, y=200)

txt = tk.Entry(window,width=28  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=600, y=215)

lbl2 = tk.Label(window, text="Enter Your Name",width=28,fg="black",bg="light blue",height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=200, y=300)

txt2 = tk.Entry(window,width=28  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=600, y=315)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="black"  ,bg="light blue"  ,height=2 ,font=('times', 15, ' bold ')) 
lbl3.place(x=400, y=400)

message = tk.Label(window, text="" ,bg="light blue"  ,fg="black"  ,width=40  ,height=2, activebackground = "#FFDAB9" ,font=('times', 15, ' bold ')) 
message.place(x=645, y=400)

lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="black"  ,bg="light blue"  ,height=2 ,font=('times', 15, ' bold')) 
lbl3.place(x=400, y=670)

lbl4 = tk.Label(window, text="Select Subject : ",width=20  ,fg="black"  ,bg="light blue"  ,height=2 ,font=('times', 15, ' bold')) 
lbl4.place(x=250, y=470) 

lbl5 = tk.Label(window, text="Select Time : ",width=20  ,fg="black"  ,bg="light blue"  ,height=2 ,font=('times', 15, ' bold')) 
lbl5.place(x=820, y=470)

message2 = tk.Label(window, text="" ,fg="black"   ,bg="light blue",activeforeground = "#FFDAB9",width=40  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=645, y=670)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():
        if(txt.get() == "") :
            messagebox.showerror("Error", "Please Enter Student ID")
            return
        if(txt2.get() == "") :
            messagebox.showerror("Error", "Please Enter Student Name")
            return
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        face_id=(txt.get())
        vid_cam = cv2.VideoCapture(0)

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        count = 0

        assure_path_exists("dataset/")

        while(True):
            _, image_frame = vid_cam.read()
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
                count += 1

       
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('frame', image_frame)

            if cv2.waitKey(300) & 0xFF == ord('q'):
                break


            elif count>=50:
                print("Successfully Captured")
                break
        Id=(txt.get())
        name=(txt2.get())
        conn = sqlite3.connect('Face-DataBase.db')
        c = conn.cursor()
        query = ("INSERT into Student(Id, Name) values(?, ?)")
        data = c.execute(query, (Id, name))
        conn.commit()
        c.close()
        conn.close()
        vid_cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id +" Name : "+ name
        message.configure(text= res)
   
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        Ids=[]
        for imagePath in imagePaths:
            pilImage=Image.open(imagePath).convert('L')
            imageNp=np.array(pilImage,'uint8')
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            faces=detector.detectMultiScale(imageNp)
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids

    faces,Ids = getImagesAndLabels('dataSet')
    s = recognizer.train(faces, np.array(Ids))
    recognizer.write('trainer/trainer.yml')
    res = "Image Trained "#+",".join(str(f) for f in Id)
    message.configure(text= res)
    
def TrackImages():
    start=time.time()
    
#print(start)
    period=10
    cv2.destroyAllWindows()
    if(cmb.get() == "" or cmb2.get() == "") :
        messagebox.showerror("Error", "Please select time and subject before taking attendance")
        return
    face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
    cap = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    flag = 0
    id=0
    conn = sqlite3.connect('Face-DataBase.db')
    c = conn.cursor()
    query = ("SELECT COUNT(*) FROM Student")
    data = c.execute(query)
    result = data.fetchall()
    nums = len(result)
    c.close()
    conn.close()   

#print(nums)
#for i in nums:
   # print(i)
    filename='filename'
    dict = {
                'item1': 1
    }
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for (x,y,w,h) in faces:
       # roi_gray = gray[y:y + h, x:x + w]
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
       # id,conf=recognizer.predict(roi_gray)
            id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf < 100) :
                if((str(id)) not in dict):
                    dict[str(id)]=str(id)
             
                ts = time.time()
                conn = sqlite3.connect('Face-DataBase.db')
                c = conn.cursor()  
                timeStamp = cmb2.get()    
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                roll = id
                sub = cmb.get()
                query_select = ("SELECT * FROM Attendance5 WHERE Roll= ? AND Date = ? AND Time = ? AND Subject = ?")
                data_select = c.execute(query_select, (roll, date, timeStamp, sub))
                has_entries = 1
                for row in data_select :
                    print("Here")
                    has_entries = 0
                    break
                if(has_entries) : 
                    query2 = ("SELECT Name FROM Student WHERE Id='" + str(roll) + "'")
                    data2 = c.execute(query2)
                    row = c.fetchone()[0]
                    print(row)
                    query = ("INSERT INTO Attendance5(Roll,Name, Date, Time, Subject) VALUES (?,?,?,?,?)")
                    data = c.execute(query, (roll,row,date,timeStamp,sub))
                conn.commit()
                c.close()
                conn.close()   
                if((str(id)) not in dict):
                    dict[str(id)]=str(id)
                break
            
        #cv2.putText(img, str(Id), (x,y+h), fontface, fontscale, fontcolor)
            cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255))
        cv2.imshow('frame',img)
    #cv2.imshow('gray',gray)
        if flag == 100:
        
            print("Attendance Update Failed")
            break
        if time.time()>start+period:
            break
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    res="attendance added"
    message2.configure(text= res)
    message.configure(text= res)
  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="black"  ,bg="blue"  ,width=28  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="black"  ,bg="blue"  ,width=28  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=300)    
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="black"  ,bg="blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=550)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="black"  ,bg="blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=550)
trackImg = tk.Button(window, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=800, y=550)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="black"  ,bg="blue"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=550)
cmb = ttk.Combobox(window, width="37",height="30", values=("Maths","Science","English","Hindi"))
cmb.place(x=520,y=490)
cmb2 = ttk.Combobox(window, width="37",height="30", values=("8:00 - 9:00","9:00 - 10:00","10:00 - 11:00","11:00 - 12:00"))
cmb2.place(x=1100,y=490)
window.mainloop()
