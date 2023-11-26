from tkinter import*
from PIL import Image,ImageTk,ImageDraw, ImageFont


man=Tk()
man.geometry("1366x768")
man.configure(bg="lavenderblush")
screenwidth = man.winfo_screenwidth()
screenheight = man.winfo_screenheight()
print(screenwidth)
print(screenheight)
man.wm_iconbitmap("1.ico")
man.geometry(f"{screenwidth}x{screenheight}")

manc1=Canvas(man,width=int(screenwidth/2),height=int(screenheight/2),bg="#d7c49e")
manc1.place(x=0,y=0)
manframe1=Frame(manc1,bg="#d7c49e")
manframe1.pack(expand=1,fill=BOTH)
manc1.create_window((0, 0), anchor='nw',width=390,window=manframe1)

Label(manc1,text="ATTENDANCE MANAGEMENT",bg="red4",fg="lightcyan",font="calibri 15",padx=71).place(x=125,y=20)

Label(manc1,text="Admission number:",font="catholic 12 bold",fg="gray1").place(x=230,y=60)
Entry(manc1,font="calibri 13 bold",bg="lavender",fg="black",textvariable=StringVar).place(x=230,y=100)

Label(manc1,text="Class and Section:",font="catholic 12 bold",fg="gray1").place(x=230,y=140)
Entry(manc1,font="calibri 13 bold",bg="lavender",fg="black",textvariable=StringVar).place(x=230,y=180)

Button(manc1,text="Search",font="calibri 12",cursor='hand2').place(x=295,y=215)

#def present():
#def absent():

present=Checkbutton(text="Mark Present",textvariable=IntVar,font="calibri 12",cursor='hand2').place(x=210,y=260)
absent=Checkbutton(text="Mark Absent",textvariable=IntVar,font="calibri 12",cursor='hand2').place(x=340,y=260)

#def upadte():
#def delete():
#def add():
#def save():
#def close():
Button(manc1,text=" Update ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=90,y=300)
Button(manc1,text=" Delete ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=180,y=300)
Button(manc1,text=" Add New ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=260,y=300)
Button(manc1,text="   Save Changes  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=360,y=300)
Button(manc1,text="  Close  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=500,y=300)

manc2=Canvas(man,width=int(screenwidth/2),height=int(screenheight/2),bg="#343148")
manc2.place(x=int(screenwidth/2),y=0)
manframe2=Frame(manc2,bg="#343148")
manframe2.pack(expand=1,fill=BOTH)
manc2.create_window((int(screenwidth/2), 0), anchor='nw',width=390,window=manframe2)
def study_mat_links():
    Entry(manc2,font="calibri 15 bold",width=35,bg="lavender",fg="black").place(x=200,y=230)
    Button(manc2,text=" Update ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=190,y=300)
    Button(manc2,text=" Delete ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=280,y=300)
    Button(manc2,text="  Save Changes ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=360,y=300)
    Button(manc2,text="   Close  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=500,y=300)
    
Label(manc2,text="STUDY MATERIAL LINKs",
      bg="lavenderblush",fg="red4",font="calibri 15",padx=71).place(x=200,y=20)
Label(manc2,text="Enter class :",fg="red4",font="calibri 15",padx=71).place(x=250,y=80)
Entry(manc2,font="calibri 15 bold",width=35,bg="lavender",fg="black").place(x=200,y=140)
Button(manc2,command=study_mat_links,text="  Search  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=350,y=180)

manc3=Canvas(man,width=int(screenwidth/2),height=int(screenheight/2),bg="#343148")
manc3.place(x=0,y=384)
manframe3=Frame(manc3,bg="#343148")
manframe3.pack(expand=1,fill=BOTH)
manc3.create_window((0,384),anchor='se',width=390,window=manframe3)
def search():
    Button(manc3,text=" Update ",font="calibri 12 bold",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=100,y=250)
    Button(manc3,text=" Delete ",font="calibri 12 bold",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=190,y=250)
    Button(manc3,text=" Add New ",font="calibri 12 bold",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=270,y=250)
    Button(manc3,text="   Save Changes  ",font="calibri 12 bold",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=370,y=250)
    Button(manc3,text="  Close  ",font="calibri 12 bold",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=510,y=250)
    Label(manc3,text='|  Total Amount   |       Paid       |       Fine       |    Net Payable Amount  |',font="catholic 12 bold").place(x=100,y=170)
    Entry(manc3,font="calibri 13 bold",width=14,bg="lavender",fg="black",textvariable=IntVar).place(x=100,y=195)
    Entry(manc3,font="calibri 13 bold",width=10,bg="lavender",fg="black",textvariable=IntVar).place(x=230,y=195)
    Entry(manc3,font="calibri 13 bold",width=10,bg="lavender",fg="black",textvariable=IntVar).place(x=325,y=195)
    Entry(manc3,font="calibri 13 bold",width=20,bg="lavender",fg="black",textvariable=IntVar).place(x=420,y=195)

Label(manc3,text="FEES MANAGEMENT",bg="lavenderblush",fg="red4",font="calibri 15",padx=71).place(x=175,y=20)
Label(manc3,text="Admission number:",font="catholic 12 bold",fg="gray1").place(x=230,y=60)
Entry(manc3,font="calibri 13 bold",bg="lavender",fg="black",textvariable=StringVar).place(x=230,y=100)
Button(manc3,command=search,text="Search",font="calibri 10",cursor='hand2').place(x=295,y=135)

manc4=Canvas(man,width=int(screenwidth/2),height=int(screenheight/2),bg="#d7c49e")
manc4.place(x=int(screenwidth/2),y=384)
manframe4=Frame(manc4,bg="#d7c49e")
manframe4.pack(expand=1,fill=BOTH)
manc4.create_window((int(screenwidth/2), 384),ancho='se',width=390,window=manframe4)
Label(manc4,text="NOTICE !!",bg="red4",fg="lightcyan",font="calibri 15",padx=71).place(x=225,y=20)
def notice():
    Entry(manc4,font="calibri 15 bold",width=35,bg="lavender",fg="black").place(x=200,y=200)
    Button(manc4,text=" Update ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=210,y=250)
    Button(manc4,text="  Save Changes ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=305,y=250)
    Button(manc4,text="   Close  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=440,y=250)

Label(manc4,text="Enter class :",fg="red4",font="calibri 15",padx=71).place(x=250,y=80)
Entry(manc4,font="calibri 15 bold",width=35,bg="lavender",fg="black").place(x=200,y=120)
Button(manc4,command=notice,text="  Search  ",font="calibri 12",bg="lightskyblue4",fg="lavenderblush",cursor='hand2').place(x=350,y=160)

man.mainloop()
