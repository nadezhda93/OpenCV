import Tkinter as tk
import numpy as np
import cv2

def showCamera():
    filewin = tk.Toplevel(root)
    frame = Frame(root, width=640, height=480)
    frame.pack()
    cap = cv2.VideoCapture(0)
    ret, frame2 = cap.read()
    cv2.imshow('original', frame2)
    #video.attach_window(frame.window_id())
   
root = tk.Tk()
root.title("Simple Gui")
root.geometry("850x600")

#create the menu bar on the window
menubar = tk.Menu(root)
#create first menu in bar - Show
showmenu = tk.Menu(menubar, tearoff=0)
#first submenu in dropdown list and command associated
showmenu.add_command(label="Capture Video", command=showCamera)

showmenu.add_separator()
showmenu.add_command(label="Exit", command=root.quit)
#set File menu in menubar
menubar.add_cascade(label="File", menu=showmenu)




root.config(menu=menubar)
root.mainloop()