import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Vishal - WebBrowser")
root.geometry('1200x750+0+0')
root.configure(bg='#564669')
root.resizable(True,True)


f1 = tk.Frame(root,width=500,height=400,relief='ridge',bg='lightblue',bd=100).place(x=150,y=80)

img = tk.PhotoImage(file="backg.png")
imgp = tk.Label(root,image=img)
imgp.pack()

def fc():
    webbrowser.open_new("www.facebook.com")

def yt():
    webbrowser.open_new("www.youtube.com")

def iT():
    webbrowser.open_new("www.instagram.com")

def tW():
    webbrowser.open_new("www.twitter.com")

def s():
    word = x.get()
    search = "www.google.com/search?q"+word
    webbrowser.open_new(search)


x = tk.StringVar()

#====================================Button GUI====================
bimg = tk.PhotoImage(file='f.png')
b1=tk.Button(f1,font=('arial',20,'bold'),fg='white',bg='blue',image=bimg,relief='raise',command=fc)
b1.place(x=400,y=350,height=160,width=165)

yimg = tk.PhotoImage(file='ytt.png')
b2=tk.Button(f1,font=('arial',20,'bold'),fg='blue',bg='yellow',image=yimg,relief='raise',command=yt)
b2.place(x=100,y=350,height=160,width=160)

iimg = tk.PhotoImage(file='ii.png')
b3=tk.Button(f1,text="Instagram",font=('arial',20,'bold'),fg='white',bg='red',image=iimg,relief='raise',command=iT)
b3.place(x=700,y=350,height=160,width=165)

timg = tk.PhotoImage(file='t.png')
b4=tk.Button(f1,font=('arial',20,'bold'),fg='white',bg='steelblue',relief='raise',image=timg,command=tW)
b4.place(x=1000,y=350,height=160,width=165)

simg = tk.PhotoImage(file='search.png')
b5=tk.Button(f1,text="Search",font=('arial',20,'bold'),fg='white',bg='green',image=simg,relief='raise',command=s)
b5.place(x=700,y=70,height=80,width=80)


#=====================================Entry Text===============================
e1 = tk.Entry(f1,textvariable=x,relief='sunken',bd=4)
e1.place(x=350,y=80,width=300,height=45)





root.mainloop()