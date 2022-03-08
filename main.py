from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Happy Birthday !!!')
root.iconbitmap('Image/icon.ico')

imagess = ImageTk.PhotoImage(Image.open('Image/presents_open.png'))
text0 = ("Chúc con chó của t sang tuổi mới \nMạnh khỏe, học tốt và bớt yêu đương nha :)))")
text1 = ("Warning: \nIf you open the gift, you will have to face the consequenses \nProceed ?")
text2 = ("Warning: \nYou have opened the true gift\nNow, face the consequenses !")

def True_gift():
    messagebox.showinfo("Warning",text2)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def click():
    res = messagebox.askyesno("Warning",text1)
    if res == 1:
        top = Toplevel()
        top.title('Gift')
        top.iconbitmap('Image/icon.ico')
        i = Button(top,image=imagess,command=True_gift)
        i.grid(row=0,column=0)
    else:
        messagebox.showinfo(":)","You coward :))")
        
mylabel0 = Label(root,text='Happy birthday you moron :)',font=('Calibri',20))
mylabel0.grid(row=0,column=0,columnspan=2)

mylabel1 = Label(root,text=text0,font=('Calibri',15))
mylabel1.grid(row=1,column=0,columnspan=3)

mylabel2 = Label(root,text='click here to open your gift :)) -->',font=('Calibri',10))
mylabel2.grid(row=2,column=0,rowspan=2)

mylabel3 = Label(root,text='(if you want)')
mylabel3.grid(row=3,column=0,rowspan=2)

presentss = ImageTk.PhotoImage(Image.open('Image/presents.png'))
button = Button(root, image=presentss,command=click)
button.grid(column=1,row=2,columnspan=3,rowspan=3,padx=5,pady=5)

root.mainloop()