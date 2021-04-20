from tkinter import * # Importing TKinter
import serial
import threading


def threadstartcar():
    arduino=serial.Serial('COM8',9600,timeout=0)
    distances = []
    while (True):
        if (arduino.inWaiting()>0):
                myData = arduino.readline()
            #distances.append(myData)
            #print(myData)
                z=myData.decode()
                #outmain=str(z)
                outus.configure(text=myData)
            #print(distances)



def threaddestroywid():
    screen.destroy()



def exitwid():
    #t2=threading.Thread(target=threaddestroywid)
    #t2.start()
    t2.join()





def startcar():
    #t1=threading.Thread(target=threadstartcar)
    #t1.start()
    t1.join()


    
   





if __name__=="__main__":

    #Setting up the screen in which the background colour can be all changed as per the requirements
    screen=Tk()#the main screen
    screen.geometry("500x270")
    screen.title("TEAM 1.618")
    heading=Label(bg="green",fg="white",width="500",height="270")
    heading.pack()
    #icon=PhotoImage(file=open("C:\Users\Utkarsh Akhouri\Desktop\Team 1.618\download.jpg"))

    #The sensor reading and their position
    reading_outus=Label(text="Distance from the obstacles behind the car",fg="black",font=("Times New Roman",15))
    reading_outus.place(x=10,y=10)
    #outus=Label(text=" ",fg="white",bg="black",font=("Comic Sans MS",15)

    outus=Label(screen,text="0",fg="black",bg="white",width="11",height="1")    
    outus.place(x=370,y=13)


            
    register=Button(screen,text="Start",width ="11",height="2",command=startcar,bg="white",fg="black")
    register.place(x=65,y=225)

    t1=threading.Thread(target=threadstartcar)
    t1.start()

    
    exitbutton=Button(screen,text="Exit the widget",width="11",height="2",command=threaddestroywid,bg="white",fg="black")
    exitbutton.place(x=350,y=225)

    t2=threading.Thread(target=threaddestroywid)
    t2.start()

    
    #arduino = serial.Serial('COM8', 9600, timeout=1000)

    #outus=Label(screen,text="0",fg="black",bg="white",width="11",height="1")
    #outus.place(x=370,y=13)
   
    #=IntVar()
            #outus=Label(text=" ",fg="white",bg="black",font=("Comic Sans MS",15)
 
   #     outus.place(x=370,y=10)







