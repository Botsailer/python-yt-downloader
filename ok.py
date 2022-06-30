import os
from tkinter import *
os.system(''' python -m pip install pytube
python -m pip install requests
python -m pip install Pillow''')
print("import of module completed")
from pytube import YouTube
from PIL import ImageTk, Image 

def clip():
    global url,ur, link
    cliptext = root.clipboard_get()
    url.delete(0, "end")
    url.insert(0, str(cliptext))
    ur=str(cliptext)
def music():
    vid=YouTube(ur)
    mu=vid.streams.filter(only_audio=True).last()
    out_file=mu.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    Label(text="Downloaded",font=('Arial',20)).pack()

def high():
    vid=YouTube(ur)
    mu=vid.streams.filter(only_audio=False)
    mul=list(enumerate(mu))
    mu.get_highest_resolution().download()
    c=Tk()
    c.geometry("750x800+450+200")
    Label(c,text="Done downlaod",font=("arial",20)).pack()
    Label(c,text="WILL CLOSE AFTER 5sec",font=("arial",25)).pack()
    c.after(5000,c.destroy)

def low():
    vid=YouTube(ur)
    mu=vid.streams.filter(only_audio=False)
    mul=list(enumerate(mu))
    mu.get_lowest_resolution().download()
    c=Tk()
    c.geometry("750x800+450+200")
    Label(c,text="Done downlaod",font=("arial",20)).pack()
    Label(c,text="WILL CLOSE AFTER 5sec",font=("arial",25)).pack()
    c.after(5000,c.destroy)

def video():
    vidos=Tk()
    vidos.geometry("550x400+450+200")
    vidos.title("VIDEO Section")
    Label(vidos,text="DOWNLOAD HIGHEST RESOLUTION OR LOWEST",font=("Aireal",15)).pack()
    h=Button(vidos,text="HIGH",command=high,fg="yellow",bg="black").place(x='250',y='50')
    l=Button(vidos,text="Low",command=low,fg="red",bg="#a7f542").place(x='100',y='50')
def pro():
    root.destroy()
    win=Tk()
    win.geometry("350x400+450+200")
    Label(win,text="Select an option",font=('Arial',15)).pack()
    m=Button(win,activeforeground="green",text="Music",bg="aqua",command=music).place(x='250',y='50')
    v=Button(win,activeforeground="green",text="VIDEO",bg="pink",command=video).place(x='100',y='50')
def dw():
    global h1, paste
    global root
    vid=YouTube(ur)
    root.geometry("700x400")
    h1.config(text=vid.title,font=("Arial",15))
    url.destroy()
    paste.destroy()
    go.destroy()
    Label(text="continue?",fg='Red',font=('Arial',22)).pack()
    yes=Button(text="YES",command=pro).pack()
    no=Button(text="NO!",command= lambda:
    root.destroy()).pack()
root=Tk()
root.bg="red"
root.geometry("350x400+450+200")
root.title("YOUTUBE VIDEO DOWNLOADER")
ur=StringVar()
h1=Label(text="Enter the text below:-",bg="aqua",fg="black")
h1.pack()
url=Entry(root,width="40",textvariable=ur)
url.pack()
url.focus()
paste=Button(root,text="paste clipboard",fg="red",command=clip)
paste.pack()
go=Button(root,text="Go",bg="pink",command=dw)
go.pack()
