import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ultralytics import YOLO
import cv2

WinD = tk.Tk()
WinD.title("YOLO Object Detection")
WinD.geometry("600x300")
WinD.configure(bg='black')
WinD.iconbitmap("D:\JKAN\Rmutr.ico")


text1 = tk.Label(text="โปรแกรมตรวจจับป้ายทะเบียนรถจักรยานยนต์", bg="black", 
                 foreground="#ff1493",
                 font=("AppleThin", 20, "bold")).pack()

text2 = tk.Label(text="โปรดกรอกภาพของคุณ", 
                 foreground="#ff1493", 
                 bg="black",
                 font=("AppleThin", 15, "bold")).pack()

def In_put_img():
    ImgDT = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.mp4")])

    detect_objects(ImgDT)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):  # กด 'q' เพื่อออก
            break


def In_put_img2():
    cap = cv2.VideoCapture(0)  
    module = YOLO("best.pt")  
    
    webcam_window = tk.Toplevel()
    webcam_window.title("Web Camera")
    webcam_window.geometry("640x480")
    
    while True:
        ret, frame = cap.read()  
        outputyolo = module(source=frame, show=True,conf=0.79)

        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break

    cap.release()  
    webcam_window.destroy()  

def detect_objects(frame):
    module = YOLO("best.pt")
    outputyolo = module(source=frame, show=True,conf=0.79)

browse_button1 = ttk.Button(WinD, text="ใส่ภาพหรือวีดีโอของคุณ", command=In_put_img)
browse_button1.pack()

browse_button2 = ttk.Button(WinD, text="Web Camera", command=In_put_img2)
browse_button2.pack()

style = ttk.Style()
style.configure("TButton",
                padding=14,
                foreground="#ff1493",
                background="black",
                font=("AppleThin", 14, "bold"))

WinD.mainloop()
