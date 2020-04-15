from tkinter import *
import pyshorteners

root = Tk()
root.title("Url shorteners")
root.geometry("275x130")

def urlfunc():
    url = urltext.get()
    urllink = StringVar()
    link = pyshorteners.Shortener().tinyurl.short(url)
    entry2 = Entry(root, textvariable = urllink).grid(row=3,column=1,ipadx=10)
    urllink.set(link)

label1 = Label(root, text ="URL SHORTENERS").grid(row=0,column=1)
label2 = Label(root, text ="Enter url").grid(row=1,column=0,padx=20)

urltext = StringVar()
entry1 = Entry(root, textvariable = urltext).grid(row=1,column=1, padx=5)
button1 = Button(root,text = "Click", command = urlfunc).grid(row=2,column=1,pady=5)

root.mainloop()