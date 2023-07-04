from tkinter import *
from pytube import YouTube

ui = Tk()
ui.geometry('500x300')
ui.resizable(0,0)
ui.title("Plutus Youtube Download Tool")

Label(ui,text = 'Plutus Youtube Downloader V.1', font = 'arial 20 bold').pack()


url = StringVar()
Label(ui,text = 'Paste Video Link Here', font = 'Helvetica 15 bold').place(x=160 , y=60)
url_insert = Entry(ui, width = 70, textvariable = url).place(x = 32, y = 90) 


def viddownloader():
    urls = YouTube(str(url.get()))
    video = urls.streams.first()
    video.download()
    Label(ui, text = 'Your Video Has Downloaded', font = 'Helvetica 12'.place(x = 180, y = 210))

Button (ui, text = 'Download Video', font = 'Times 15 bold',bg = 'Darkorchid1', padx = 2, command = viddownloader).place(x = 180, y = 150)

ui.mainloop()