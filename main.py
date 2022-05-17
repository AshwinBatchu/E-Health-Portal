import os
import pandas as pd
import random
import collections
from tkinter import *
import tkinter
import time

Coronary_Artery_Disease = ['chestpain','weakness','armpain','breadth shortness']
Stroke = ['weakness','confusion','troublewalking','lowconfidence']
Low_Respiratory_Infections   = ['runny nose','dry cough','sore throat','fever']
Chronic_obstructive_pulmonary_disease = ['wheezing','swelling','low energy','respiration problem']
lung_cancers = ['hoarseness','tiredness','weakness','weightloss']
Diabetes = ['very thirsty','weightloss','tiredness','dryskin']
Alzheimers_Disease = ['memoryloss','confusion','restlessness','weakness']
Tuberculosis = ['coughing','fever','chestpain','weightloss']
Cirrhosis = ['bleeding','weightloss','itchyskin','nausea']

mainlist = [Coronary_Artery_Disease,Stroke,Low_Respiratory_Infections ,Chronic_obstructive_pulmonary_disease,lung_cancers ,Diabetes ,Alzheimers_Disease,Tuberculosis,Cirrhosis]
names = ['Coronary_Artery_Disease','Stroke','Low_Respiratory_Infections','Chronic_obstructive_pulmonary_disease','lung_cancers','Diabetes','Alzheimers_Diseas','Tuberculosis','Cirrhosis']









x = Tk()
x.title("Main Page - Virtual Hospital")
x.geometry("500x200")

tokelist = []


def maketoken():
    token1 = random.randint(1,1000)
    token2 = random.randint(1,1000)
    token = str(token1)+str(token2)
    for a in tokelist:
        if a == token:
            maketoken()
        else:
            tokelist.append(token)     
    return(token)     


def aboutinfos():
    main = Toplevel(x)
    main.geometry("500x500")
    main.title("About Information Window")
    label1 = tkinter.Label(main,text="Designed by - Ashwin Batchu")
    label2 = tkinter.Label(main,text="The Virtual Doctor")
    label3 = tkinter.Label(main,text="Free Doctor Consuting Software")
    label4 = tkinter.Label(main,text="Made on 15/05/22")
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    
def askQ():

    def takevalue():
        listnew = []
        c1 = f1.get()
        c2 = f2.get()
        c3 = f3.get()
        c4 = f4.get()
        listnew.append(c1)
        listnew.append(c2)
        listnew.append(c3)
        listnew.append(c4)
        old = listnew
        print("Button Working")
        print(listnew)
        i23 = 0
        for a in mainlist:
            
            if collections.Counter(a) != collections.Counter(old):
                i23 = i23 + 1
                if i23 == 9:
                     l234 = Label(main, text = "Disease Not Found Please Consult a Doctor , Redirecting to Registration Page")
                     l234.pack()
                     time.sleep(2)
                     registrationslot()

            else:
                ind = mainlist.index(a)
                print(ind)
                print("Disease Identified")
                fogg = names[ind]
                l234 = Label(main, text = "You have "+ fogg)
                l234.pack()

                



    main = Toplevel(x)
    main.geometry("500x300")
    main.title("The Disease Predictor")
    l = Label(main, text = "Enter Your Symptoms Below")
    f1 = tkinter.Entry(main,width=20,)
    f2 = tkinter.Entry(main,width=20)
    f3 = tkinter.Entry(main,width=20)
    f4 = tkinter.Entry(main,width=20)
    l.pack()
    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()

    a2 = tkinter.Button(main,text="Take In",command=takevalue)
    a2.pack()

    mainloop()



def registrationslot():
    
    def takevalu():
        x = slot1.get()
        y = slot2.get()

        f3 = maketoken()

        a0 = pd.read_csv('reg.csv')
        p = a0.tail(1)
        f = p['time']
        x23 = str(f)
        y4 = x23.split(" ")
        y22 = y4[4].split("\nName")
        a2 = y22[0]
        a3 = int(a2)


        if a3 == 2200:
            print("Hospital Closed Come tomorrow")
        else:    
            df = pd.DataFrame({'name': [x],
                            'time': [a3+100],
                            'reason': [y],
                            'token':[f3]
                            })                   
            df.to_csv('reg.csv',mode='a',index=False,header=False)
            label1 = tkinter.Label(registerwin,text="Reason is "+ y)
            label2 = tkinter.Label(registerwin,text="Name of Patient "+ x)
            label3 = tkinter.Label(registerwin,text="Token Number "+ f3)
            label4 = tkinter.Label(registerwin,text="Appointment Time is "+ str(a3+100))
            label1.pack()
            label2.pack()
            label3.pack()
            label4.pack()




    registerwin = Toplevel(x)
    registerwin.geometry("600x500")
    registerwin.title("Registeration Window")
    slot1 = tkinter.Entry(registerwin)
    slot1.insert(0,"Enter Patient Name")
    slot2 = tkinter.Entry(registerwin,)
    slot2.insert(0,"Enter Reason")
    button23 = tkinter.Button(registerwin,text="Submit",command = takevalu)
    slot1.pack()
    slot2.pack()
    button23.pack()






def mainwindow_run():
    print("Opened Main Window")
    main = Toplevel(x)

    main.geometry("700x490")
    main.title("Main Window")
    button1 = tkinter.Button(main,width=30,height=10,text="Consult Doctor",command=askQ)
    button2 = tkinter.Button(main,width=30,height=10,text="Book Appointment",command = registrationslot)
    button3 = tkinter.Button(main,width=30,height=10,text="Get Information",command=aboutinfos)
    button1.pack()
    button2.pack()
    button3.pack()






def registerwindow():   
    def registername():
        print("Function Called")
        new_user = e3.get()
        new_password = e4.get()
        a = pd.read_csv("testxl.csv")
        if new_user in a.values:
            print("Username Already Exists Please Try another one")
        else :
            df = pd.DataFrame({'username': [new_user],
                    'password': [new_password]
                    })                   
            df.to_csv('testxl.csv',mode='a',index=False,header=False)

    newwin = Toplevel(x)
    newwin.title("Register Your ID")
    newwin.geometry("500x200")
    e3 = Entry(newwin,width = 20)
    e4 = Entry(newwin,width = 20)
    e3.insert(0,"Enter Username")
    e4.insert(0,"Enter Password")
    l6 = tkinter.Button(newwin,text="Register",command=registername)
    
    e3.pack()
    e4.pack()
    l6.pack()
    



def loginmain():
    print("Function Called")
    username_main = e.get()
    password_main = e2.get()
    a = pd.read_csv("testxl.csv")
    if username_main in a.values:
        print("Username Accepted")
        if password_main in a.values:
            print("Password Accepted")
            mainwindow_run()
            
    else:
        print("Error in Logging in")




l3 = tkinter.Button(x,text="Login",width=10,command=loginmain)
l5 = tkinter.Button(x,text="Register New ID",command=registerwindow)

e = Entry(x,width = 20)
e.insert(0,"Enter Username")
e2 = Entry(x , width= 20)
e2.insert(0,"Password")
e.pack()
e2.pack()
l3.pack()
l5.pack()


mainloop()
