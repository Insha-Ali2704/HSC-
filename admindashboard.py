from tkinter import *
from PIL import Image,ImageTk,ImageDraw, ImageFont

adm=Tk()
adm.title("Admin Dashboard")
adm.geometry("1366x768")

adm.configure(bg="lavenderblush")
screenwidth = adm.winfo_screenwidth()
screenheight = adm.winfo_screenheight()
print(screenwidth)
print(screenheight)
adm.wm_iconbitmap("1.ico")
adm.geometry(f"{screenwidth}x{screenheight}")
admc1=Canvas(adm,width=390,height=screenheight,bg="hotpink4")
admc1.place(x=0,y=0)
admframe1=Frame(admc1,bg="hotpink4")
admframe1.pack(expand=1,fill=BOTH)
admc1.create_window((0, 0), anchor='nw',width=390,window=admframe1)

Label(admc1,text="Name : ",bg="mistyrose",fg="black",font="century 15 ",padx=40).place(x=0,y=260)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=260)

Label(admc1,text="Phone No. :",bg="mistyrose",fg="black",font="century 15 ",padx=22).place(x=0,y=300)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=300)

Label(admc1,text="D.O.B : ",bg="mistyrose",fg="black",font="century 15 ",padx=40).place(x=0,y=340)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=340)

Label(admc1,text="Father's Name: ",bg="mistyrose",fg="black",font="century 15 ",padx=2).place(x=0,y=380)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=380)

Label(admc1,text="Mother's Name:",bg="mistyrose",fg="black",font="century 15 ",padx=2).place(x=0,y=420)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=420)

Label(admc1,text="Joining Date: ",bg="mistyrose",fg="black",font="century 15 ",padx=12).place(x=0,y=460)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=460)

Label(admc1,text="Salary : ",bg="mistyrose",fg="black",font="century 15 ",padx=40).place(x=0,y=500)
Label(admc1,text="",bg="mistyrose",fg="black",font="century 15 ",padx=120).place(x=155,y=500)

admc2=Canvas(adm,width=280,height=screenheight,bg="violetred4")
admc2.place(x=screenwidth-280,y=0)
admframe2=Frame(admc2,bg="violetred4")
admframe2.pack(expand=1,fill=BOTH)
admc2.create_window((screenwidth-280, 0), anchor='ne',width=180,window=admframe2)


hi=Image.open("greeting.png")
resized=hi.resize((150,180),Image.LANCZOS)
photohi=ImageTk.PhotoImage(resized)
Label(adm,image=photohi,bg="mediumpurple").place(x=393,y=0)

Label(adm,text="WELCOME BACK ADMIN!",bg="turquoise4",fg="white",font="algerian 15").place(x=560,y=30)
Label(adm,bg="dimgray",height=25,width=45).place(x=750,y=220)
Label(adm,text="~MANAGE",bg="lavenderblush",fg="hotpink4"
      ,font="modern 35 bold").place(x=450,y=260)
Label(adm,text="your",bg="lavenderblush",fg="hotpink4"
      ,font="calibri 25 bold").place(x=640,y=260)
Label(adm,text="TASKS here!",bg="lavenderblush",fg="hotpink4"
      ,font="modern 35 bold").place(x=460,y=320)

Label(adm,text="TASK MANAGEMENT",bg="red4",fg="lightcyan",font="calibri 15",padx=72).place(x=750,y=220)

Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=251)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=280)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=309)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=338)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=367)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=396)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=425)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=454)
Entry(adm,font="calibri 13 bold",width=35,bg="lavender",fg="black").place(x=750,y=483)

#def add():
#def update():
#def delete():
#def save():

Button(adm,text=" ADD " ,font="calibri 12 bold",bg="darkslategray",border=0,fg="white",padx=2).place(x=760,y=529)
Button(adm,text=" UPDATE ",font="calibri 12 bold",bg="darkslategray",border=0,fg="white",padx=2).place(x=825,y=529)
Button(adm,text=" DELETE ",font="calibri 12 bold",bg="darkslategray",border=0,fg="white",padx=2).place(x=905,y=529)
Button(adm,text=" SAVE ",font="calibri 12 bold",bg="darkslategray",border=0,fg="white",padx=2).place(x=985,y=529)

#def home():
#def student_dashboard():
#def teacher_dashboard():
#def logout():
Button(adm,text=" Home ",font="catholic 15 bold",bg="violetred4",activebackground="violetred3",border=0,fg="white",relief='sunken',padx=100).place(x=int(screenwidth-277),y=100)
Button(adm,text=" Student Dashboard ",font="catolic 15 bold",bg="violetred4",activebackground="violetred3",border=0,fg="white",relief='sunken',padx=50).place(x=int(screenwidth-277),y=160)
Button(adm,text=" Teacher Dashboard ",font="catholic 15 bold",bg="violetred4",activebackground="violetred3",border=0,relief='sunken',padx=50,fg="white").place(x=int(screenwidth-277),y=220)
Button(adm,text=" Log out ",font="catholic 15 bold",bg="violetred4",activebackground="violetred3",border=0,fg="white",relief='sunken',padx=100).place(x=int(screenwidth-277),y=280)


adm.mainloop()
