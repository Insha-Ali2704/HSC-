from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as tmsg
import webbrowser
import mysql.connector
def on_closing():
    main.destroy()
def pageclose():
    main.withdraw()
    gallery.withdraw()
    founder.withdraw()
    aop.withdraw()
    faculty.withdraw()
    facility.withdraw()
    fee.withdraw()
    ach.withdraw()
    advc.withdraw()
    coFounder.withdraw()
    contact.withdraw()
    stlog.withdraw()
    tchlog.withdraw()
    adminlog.withdraw()
    sgst.withdraw()
    sgtc.withdraw()
class image1:
    def __init__(self, master,file,x,y,a,b,s):
        canvas =Canvas(master,bg="lavender",height=s)
        canvas.pack(fill=X)
        background_image = PhotoImage(file="bg.png")
        canvas.create_image(0, 0, anchor=NW, image=background_image)
        canvas.background = background_image

        self.img= (Image.open(file))
        self.resized_image= self.img.resize((a,b),Image.LANCZOS)
        self.new_image= ImageTk.PhotoImage(self.resized_image,master=canvas) # Changes here
        canvas.create_image(x, y, image=self.new_image) # Changes here.

class Gallery:
        def __init__(self, master,file1,x1,y1,file2,a,b,s,file3,file4,file5,file6,file7,file8,file9):
            canvas =Canvas(master,bg="lavender",height=s)
            canvas.pack(fill=X)
            #for file1
            self.img= (Image.open(file1))
            self.resized_image= self.img.resize((a,b),Image.LANCZOS)
            self.new_image= ImageTk.PhotoImage(self.resized_image,master=canvas) # Changes here
            canvas.create_image(x1, y1, image=self.new_image) # Changes here.
            #for file2
            self.img1= (Image.open(file2))
            self.resized_image1= self.img1.resize((a,b),Image.LANCZOS)
            self.new_image1= ImageTk.PhotoImage(self.resized_image1,master=canvas) # Changes here
            canvas.create_image(x1+450, y1, image=self.new_image1) # Changes here.
            #for file 3
            self.img2= (Image.open(file3))
            self.resized_image2= self.img2.resize((a,b),Image.LANCZOS)
            self.new_image2= ImageTk.PhotoImage(self.resized_image2,master=canvas) # Changes here
            canvas.create_image(x1+900, y1, image=self.new_image2) # Changes here.
            #for file 4
            self.img3= (Image.open(file4))
            self.resized_image3= self.img3.resize((a,b),Image.LANCZOS)
            self.new_image3= ImageTk.PhotoImage(self.resized_image3,master=canvas) # Changes here
            canvas.create_image(x1, y1+350, image=self.new_image3) # Changes here.
            #for file 5
            self.img4= (Image.open(file5))
            self.resized_image4= self.img4.resize((a,b),Image.LANCZOS)
            self.new_image4= ImageTk.PhotoImage(self.resized_image4,master=canvas) # Changes here
            canvas.create_image(x1+450, y1+350, image=self.new_image4) # Changes here.
            #for file 6
            self.img5= (Image.open(file6))
            self.resized_image5= self.img5.resize((a,b),Image.LANCZOS)
            self.new_image5= ImageTk.PhotoImage(self.resized_image5,master=canvas) # Changes here
            canvas.create_image(x1+900, y1+350, image=self.new_image5) # Changes here.
            #for file 7
            self.img6= (Image.open(file7))
            self.resized_image6= self.img6.resize((a,b),Image.LANCZOS)
            self.new_image6= ImageTk.PhotoImage(self.resized_image6,master=canvas) # Changes here
            canvas.create_image(x1, y1+700, image=self.new_image6) # Changes here.
            #for file 8
            self.img7= (Image.open(file8))
            self.resized_image7= self.img7.resize((a,b),Image.LANCZOS)
            self.new_image7= ImageTk.PhotoImage(self.resized_image7,master=canvas) # Changes here
            canvas.create_image(x1+450, y1+700, image=self.new_image7) # Changes here.
            #for file 9
            self.img8= (Image.open(file9))
            self.resized_image8= self.img8.resize((a,b),Image.LANCZOS)
            self.new_image8= ImageTk.PhotoImage(self.resized_image8,master=canvas) # Changes here
            canvas.create_image(x1+900, y1+700, image=self.new_image8) # Changes here.
def showcontact():
    pageclose()
    contact.deiconify()
    contact.protocol("WM_DELETE_WINDOW",on_closing)
    contact.title("Contact us")
    screenwidth = contact.winfo_screenwidth()
    screenheight = contact.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    contact.wm_iconbitmap("1.ico")
    contact.geometry(f"{screenwidth}x{screenheight}")


    canvas=Canvas(contact,width=screenwidth-20,height=screenheight-30,bg="lavender")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    contactframe=Frame(canvas,bg="lavender")
    contactframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=contactframe)
    scrollbar = Scrollbar(contact,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #aexecutequerrying logo
    # img_hsc=Image.open("hsc.png") 
    # resized_img_hsc=img_hsc.resize((220,120),Image.LANCZOS)
    # photo_hsc=ImageTk.PhotoImage(resized_img_hsc)
    # L1=Label(canvas,image=photo_hsc,bg="dark blue")
    # L1.place(x=5,y=0)
    #navigation bar
    logo=image1(contactframe,"hsc.png",130,55,255,100,100)
    navbar(contactframe)
    window=image1(contactframe,"30.jpg",screenwidth/2,150,screenwidth,300,970)

    Label(contactframe,text="Contact Us",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline",justify=CENTER).place(x=50,y=450)

    Label(contactframe,text='''Enter Your detail. Hope we will connect with you soon.''',fg="black",bg="light skyblue3",font="Candara 20 italic").place(x=50,y=520)
    Label(contactframe,text="Name:- ",fg="black",bg="dark green",font="Candara 20 italic").place(x=250,y=600)
    Label(contactframe,text="Email:- ",fg="black",bg="dark green",font="Candara 20 italic").place(x=250,y=650)
    Label(contactframe,text="Phone No:- ",fg="black",bg="dark green",font="Candara 20 italic").place(x=250,y=700)
    Label(contactframe,text="Class:- ",fg="black",bg="dark green",font="Candara 20 italic").place(x=250,y=750)

    Entry(contactframe,width=30,font="20").place(x=450,y=600)
    Entry(contactframe,width=30,font="20").place(x=450,y=650)
    Entry(contactframe,width=30,font="20").place(x=450,y=700)
    Entry(contactframe,width=30,font="20").place(x=450,y=750)
    Button(contactframe,text="SUBMIT",padx=20,pady=20,bg="black",fg="white").place(x=450,y=850)


    copyright = Label(contactframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=970)
    contact.mainloop()
def showcofounder():
    pageclose()
    coFounder.deiconify()
    coFounder.protocol("WM_DELETE_WINDOW",on_closing)
    coFounder.title("Co-Founder")
    coFounder.geometry("1366x768")
    screenwidth = coFounder.winfo_screenwidth()
    screenheight = coFounder.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    coFounder.wm_iconbitmap("1.ico")
    coFounder.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(coFounder,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    coFounderframe=Frame(canvas,bg="white",width=screenwidth-20,height=screenheight+950)
    coFounderframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=coFounderframe)
    scrollbar = Scrollbar(coFounder,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #aexecutequerrying logo
    # img_hsc=Image.open("hsc.png") 
    # resized_img_hsc=img_hsc.resize((220,120),Image.LANCZOS)
    # photo_hsc=ImageTk.PhotoImage(resized_img_hsc)
    # L1=Label(coFounderframe,image=photo_hsc,bg="dark blue")
    # L1.place(x=5,y=0)
    #navigation bar
    logo=image1(coFounderframe,"hsc.png",130,55,255,100,100)
    navbar(coFounderframe)
    window=image1(coFounderframe,"f.jpg",screenwidth/2,60,screenwidth,550,300)

    hamid=image1(coFounderframe,"co-founder.jpg",1050,100,300,250,1360)


    Label(coFounderframe,text="Co-Founder",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=40,y=440)
    Label(coFounderframe,text="Janab Saiyid Hamid Saheb",bg="gray25",fg="lavender",font="Broadway 20").place(x=40,y=500)
    Label(coFounderframe,text='''Janab Syed Hamid Saheb was the most perfect person who
    could help him translate his dreams of bringing the Muslims and the deprived
    sections of society into the daylight of educational enlightenment- This is what
    Janab Hakeem Abdul Hameed Saheb must have realized as he set out on his
    self imposed endeavour of bringing about social and educational equality in society.
    Janab Hamid Saheb was born on 28 March, 1920. He completed his graduation and
    post graduation from Aligarh Muslim University. He served the Provincial Civil Services
    in the then United Provinces from 1943 to 1949. Thereafter he served the nation with
    distinction in various central ministries in different capacities till his retirement in 1980.
    A ship is safest when it is in harbour but that is not where it is meant to be.
    After retirement Syed Hamid Saheb declined many offers of gubernatorial and
    diplomatic positions but accepted the Vice-Chancellorship of Aligarh Muslim University,
    his Alma Mater. He accepted and completed the tumultuous term gaining admiration of
    one and all for his courage, patience, and sagacity. He continued to be associated with
    various educational institutions and bodies in an honorary capacity throughout his life.
    Janab Hamid Saheb devoted his life after retirement to the educational cause of the
    community. His heart and soul continued to be preoccupied with the overwhelming
    desire to lift the deprived mass of the society by making available to them
    opportunities of acquiring modern education. Janab Hamid Saheb was a person who
    could extrapolate to the consequences of current information when those were not
    obvious to others around him. The educational inadequacies of the Muslim
    community were constantly a source of concern to him. He was aware of the
    high school-dropout rates of Muslim male students while on the other hand he was
    also distressed by the fact that large number of Muslim girls were practically being
    deprived of school education by being made to stay at home. He knew that Muslims
    would not progress if their girls did not acquire modern education.He was influenced
    by the vision and farsightedness of Janab Abdul Hameed Saheb and joining hands
    with him went on to help establish the Jamia Hamdard and take the
    Hamdard Education Society forward. Janab Hamid Saheb wanted to see increasing
    number of Muslims taking part in the national civil administration. He visited various
    universities and motivated students to sit for and qualify the Indian Civil Services examinations.
    With this mission in mind he, with the active encouragement of
    Janab Hakeem Abdul Hameed Saheb, established a small centre in Talimabad which started
    preparing candidates for the Indian civil services examination. He started this endevour
    in 1991 and 1992 saw success of the first batch of Hamdardians as Indian civil servants.
    The tiny acorn Janab Hamid Saheb planted has grown into a mighty oak known far and
    wide as the Hamdard Study Circle.The Jamia Hamdard, which he helped in seeing the
    light of the day, in 1999 requested Janab Syed Hamid Saheb to become it’s Chancellor
    which he remained till his passing away. In between he continued to be associated with
    educational institutions and committees in various capacities. He also discharged his
    duties as secretary of the Hamdard Education Society ever since its inception.On 29 of
    December 2014 when the sun was drawing the curtain on the day, Janab Hamid Saheb
    sailed out of the safe harbor on a silent tide leaving his family and relations, contemporaries,
    acquaintances, well wishers and those who had merely heard about him mourning the
    irreparable loss.'''
        ,fg="black",font="Calibri 15").place(x=40,y=550)

    # co_founder=Image.open("co-founder.jpg") 
    # resized_co_founder=co_founder.resize((350,380),Image.LANCZOS)
    # photo_co_founder=ImageTk.PhotoImage(resized_co_founder)
    # L2=Label(coFounderframe,image=photo_co_founder,bg="dark blue")
    # L2.place(x=980,y=460)


    Label(coFounderframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=910,y=660)

    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(coFounderframe,text="Union Public Service Commission",command=upsc,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=730)
    Button(coFounderframe,text="Down to Earth",command=down_to_earth,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=770)
    Button(coFounderframe,text="Press Information Bureau",command=pib,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=810)
    Button(coFounderframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=850)
    Button(coFounderframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=910)
    Button(coFounderframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=970)
    Button(coFounderframe,text="World Bank",command=wb,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=1030)
    Button(coFounderframe,text="Third World Network",command=twn,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=1070)
    Button(coFounderframe,text="Project Syndicate",command=ps,width=30,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=910,y=1110)


    copyright = Label(coFounderframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1650)

    coFounder.mainloop()

def showadvisory():
    pageclose()
    advc.deiconify()
    advc.protocol("WM_DELETE_WINDOW",on_closing)
    advc.title("Advisory Committee")
    advc.geometry("1366x768")
    screenwidth = advc.winfo_screenwidth()
    screenheight = advc.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    advc.wm_iconbitmap("1.ico")
    advc.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(advc,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    advcframe=Frame(canvas,bg="lavender",width=screenwidth-20,height=screenheight+650)
    advcframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=advcframe)
    scrollbar = Scrollbar(advc,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    logo=image1(advcframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(advcframe)
    window=image1(advcframe,"31.jpg",screenwidth/2,150,screenwidth,300,1400)
    Label(advcframe,text="Advisory Committee",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)

    Label(advcframe,text="Mr.Naveed Masood IAS (Retd.)",bg="azure4",fg="dark blue",font="Broadway 20").place(x=50,y=530)
    Label(advcframe,text="-Former Secretary to Government of India",fg="black",font="Calibri 15").place(x=50,y=580)

    Label(advcframe,text="Ms. Syeda Sayyadain Hameed",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=630)
    Label(advcframe,text="-Member – Planning Commission",fg="black",font="Calibri 15").place(x=56,y=680)

    Label(advcframe,text="Dr S. Haider Hasan",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=730)
    Label(advcframe,text="-Former Chief Commissioner, Customs and CGST, ",fg="black",font="Calibri 15").place(x=56,y=780)
    Label(advcframe,text="-Director– Hamdard Study Circle New Delhi.  ",fg="black",font="Calibri 15").place(x=56,y=830)

    Label(advcframe,text="Mr. P.A. Inamdar",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=880)
    Label(advcframe,text="-Executive Vice President",fg="black",font="Calibri 15").place(x=56,y=930)
    Label(advcframe,text="-Maulana Azad Education Foundation ",fg="black",font="Calibri 15").place(x=56,y=980)

    Label(advcframe,text="Dr. G.N. Qazi",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=1030)
    Label(advcframe,text="-Director General, HIMSR, New Delhi",fg="black",font="Calibri 15").place(x=56,y=1080)

    Label(advcframe,text="Mr. Syed Samar Hamid (Secretary)",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=1130)
    Label(advcframe,text="-Hamdard Education Society",fg="black",font="Calibri 15").place(x=56,y=1180)

    Label(advcframe,text="Prof. Abdul Nafey",bg="azure4",fg="dark blue",font="Broadway 20").place(x=56,y=1230)
    Label(advcframe,text="-School of International Studies",fg="black",font="Calibri 15").place(x=56,y=1280)
    Label(advcframe,text="-Jawaharlal Nehru University, New Delhi  ",fg="black",font="Calibri 15").place(x=56,y=1330)

    Label(advcframe,text='''
    The Hamdard Study Circle (HSC) was set up in 1991
    by Janab Hakeem Abdul Hameed Saheb together
    with Janab Saiyid Hamid Saheb for coaching candidates from
    minority communities and backward classes for the
    Indian Civil Services.''',fg="black",bg="lavender",font="Calibri 22",width=40).place(x=600,y=1110)
    Label(advcframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=790,y=460)
    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(advcframe,text="Union Public Service Commission",command=upsc,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=520)
    Button(advcframe,text="Down to Earth",command=down_to_earth,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=580)
    Button(advcframe,text="Press Information Bureau",command=pib,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=640)
    Button(advcframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=700)
    Button(advcframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=780)
    Button(advcframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=860)
    Button(advcframe,text="World Bank",command=wb,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=940)
    Button(advcframe,text="Third World Network",command=twn,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1000)
    Button(advcframe,text="Project Syndicate",command=ps,width=25,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1060)

    copyright = Label(advcframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1400)

    advc.mainloop()
def showachievement():
    pageclose()
    ach.deiconify()
    ach.protocol("WM_DELETE_WINDOW",on_closing)
    ach.title("Achievements")
    ach.geometry("1366x768")
    screenwidth = ach.winfo_screenwidth()
    screenheight = ach.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    ach.wm_iconbitmap("1.ico")
    ach.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(ach,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    achframe=Frame(canvas,bg="lavender",width=screenwidth-20,height=screenheight+400)
    achframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=achframe)
    scrollbar = Scrollbar(ach,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    
    logo=image1(achframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(achframe)
    window=image1(achframe,"28.jpg",screenwidth/2,150,screenwidth,300,1220)

    Label(achframe,text="Achievements",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)


    Label(achframe,text='''Since its inception,
    Hamdard Study Circle has strived to
    achieve best results in All India
    Civil Service Examination.''',bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=530)
    Label(achframe,text='''The persistent efforts and
    success of our candidates in qualifying the
    examination on year to year basis since
    1991 has aexecutequerryed to the prestige of Institution.
    Quality learning, continuous monitoring and
    imbibing values of Civil Services have been
    the hallmark of Hamdard Study Circle.
    The Institution provides guidance and coaching
    in all three stages of the Civil Service Examination.
    So far, 658 of our candidates have qualifiedthe
    UPSC C.S exam, and joined the prestigious Civil Services.''',bg="lavender",fg="gray1",font="Century 19 bold" ).place(x=30,y=680)

    Label(achframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=790,y=460)
    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(achframe,text="Union Public Service Commission",command=upsc,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=520)
    Button(achframe,text="Down to Earth",command=down_to_earth,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=580)
    Button(achframe,text="Press Information Bureau",command=pib,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=640)
    Button(achframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=700)
    Button(achframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=780)
    Button(achframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=860)
    Button(achframe,text="World Bank",command=wb,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=940)
    Button(achframe,text="Third World Network",command=twn,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1000)
    Button(achframe,text="Project Syndicate",command=ps,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1060)

    copyright = Label(achframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1200)

    ach.mainloop()

def showfee():
    pageclose()
    fee.deiconify()
    fee.protocol("WM_DELETE_WINDOW",on_closing)
    fee.title("FEE")
    fee.geometry("1366x768")
    screenwidth = fee.winfo_screenwidth()
    screenheight = fee.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    fee.wm_iconbitmap("1.ico")
    fee.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(fee,width=screenwidth-20,height=screenheight,bg="lavender")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    feeframe=Frame(canvas,bg="light skyblue3",width=screenwidth-20,height=screenheight+550)
    feeframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=feeframe)
    scrollbar = Scrollbar(fee,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    logo=image1(feeframe,"hsc.png",130,55,255,100,100)
    navbar(feeframe)
    window=image1(feeframe,"27.jpg",screenwidth/2,150,screenwidth,300,1350)
    Label(feeframe,text="FEE STRUCTURE",bg="dark slate gray",fg="white",font="Bernard_MT 27 underline").place(x=50,y=460)
    Label(feeframe,text='''HSC provides an ambience of learning and a peaceful environment
    to stay focused on the goal.''',fg="black",bg="light skyblue3",font="Candara 22 italic").place(x=50,y=520)

    Label(feeframe,text='''The institution offers residential accommodation,
    mess facilities and other amenities on nominal charges.The fee structure
    for all the facilities is such that even students from remote areas of the
    country could afford to stay in Delhi with all facilities that are required to
    achieve the dream of cracking Civil Service Examination.
    '''
        ,fg="black",font="Calibri 20 ",bg="light skyblue3").place(x=50,y=620)
    Label(feeframe,text='''Following are the expenses that a candidate has to
    bear once selected for the year-long preparation course in
    Hamdard Study Circle :

    -Registration Fee of Rs.6000 at the time of admission. The amount is
    non-refundable once the payment is made.
    -Monthly charges of Rs.6500 for the facilities and services provided in
    Hamdard Study Circle including mess and accommodation.
    -For those availing AC rooms allotted on merit basis will have to
    deposit the security money of Rs. 5000. This amount is refundable
    at the end of the session or when the candidate vacates.
    -Monthly AC electricity bill for only those candidates who have
    AC rooms.''',fg="gray1",font="Calibri 20 ",bg="light skyblue3").place(x=50,y=840)

    Label(feeframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=980,y=460)

    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(feeframe,text="Union Public Service Commission",command=upsc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=530)
    Button(feeframe,text="Down to Earth",command=down_to_earth,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=570)
    Button(feeframe,text="Press Information Bureau",command=pib,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=610)
    Button(feeframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=650)
    Button(feeframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=710)
    Button(feeframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=770)
    Button(feeframe,text="World Bank",command=wb,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=830)
    Button(feeframe,text="Third World Network",command=twn,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=870)
    Button(feeframe,text="Project Syndicate",command=ps,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=910)


    copyright = Label(feeframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1350)

    fee.mainloop()
def showfacility():
    pageclose()
    facility.deiconify()
    facility.protocol("WM_DELETE_WINDOW", on_closing)
    facility.title("Facilities")
    facility.geometry("1366x768")
    screenwidth = facility.winfo_screenwidth()
    screenheight = facility.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    facility.wm_iconbitmap("1.ico")
    facility.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(facility,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    facilityframe=Frame(canvas,bg="lavender",width=screenwidth-20,height=screenheight+850)
    facilityframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=facilityframe)
    scrollbar = Scrollbar(facility,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    logo=image1(facilityframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(facilityframe)
    window=image1(facilityframe,"26.jpg",screenwidth/2,150,screenwidth,300,1650)

    Label(facilityframe,text="Facilities",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)

    Label(facilityframe,text="RESIDENTIAL FACILITIES: ",bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=530)
    Label(facilityframe,text="Accomodation for 168 candidates.",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=580)
    Label(facilityframe,text="New AC Block- HPS Boys Hostel Building ",bg="gainsboro",fg="gray1",font="Century 18 bold").place(x=50,y=620)
    Label(facilityframe,text="-36 AC Rooms for Boys",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=650)
    Label(facilityframe,text="-12 AC Rooms for Girls",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=680)
    Label(facilityframe,text="-Air-conditioned multipurpose hall, lecture hall, Namaz Hall",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=710)
    Label(facilityframe,text="-Visitors’ room, Pantry",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=740)
    Label(facilityframe,text="-Round the clock WiFi",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=770)
    Label(facilityframe,text="-Professional washerman available for washing clothes",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=800)

    Label(facilityframe,text="Old Block",bg="gainsboro",fg="gray1",font="Century 18 bold").place(x=50,y=840)
    Label(facilityframe,text="-Well-equipped Air-Conditioned Lecture hall",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=870)
    Label(facilityframe,text="-Reading cum discussion room",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=900)
    Label(facilityframe,text="-Recreation room",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=930)
    Label(facilityframe,text="-Mess managed by outsourced caterer",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=960)
    Label(facilityframe,text="*The AC rooms are allotted to the willing candidates in the order of merit.",bg="lavender",fg="gray1",font="calibri 17").place(x=40,y=990)

    Label(facilityframe,text="SPORTS AND RECREATIONAL FACILITIES",bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=1030)
    Label(facilityframe,text="-Gymnasium facilities available at subsidised fee",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1060)
    Label(facilityframe,text="-Cricket Field",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1090)
    Label(facilityframe,text="-Football Field",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1120)
    Label(facilityframe,text="-Basketball Field ",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1150)
    Label(facilityframe,text="-Tennis Court ",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1180)
    Label(facilityframe,text="-Badminton Court ",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1210)
    Label(facilityframe,text="-Squash Court",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1240)

    Label(facilityframe,text="BANKING FACILITIES",bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=1280)
    Label(facilityframe,text="-UCO Bank branch and a post office available in Talimabad campus",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1310)

    Label(facilityframe,text="SAFETY AND SECURITY",bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=1350)
    Label(facilityframe,text="-Campus and hostels’ entry and exit manned round-the-clock by professional security agency",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1380)
    Label(facilityframe,text="-CCTV cameras installed in all sensitive areas of the campus",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1410)
    Label(facilityframe,text="-Male and female nurse available on campus",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1440)

    Label(facilityframe,text="POWER",bg="lavender",fg="gray1",font="Century 20 bold").place(x=50,y=1480)
    Label(facilityframe,text="-Round the clock uninterrupted power supply",bg="lavender",fg="gray1",font="calibri 17").place(x=50,y=1510)

    Label(facilityframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=790,y=460)
    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(facilityframe,text="Union Public Service Commission",command=upsc,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=520)
    Button(facilityframe,text="Down to Earth",command=down_to_earth,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=580)
    Button(facilityframe,text="Press Information Bureau",command=pib,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=640)
    Button(facilityframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=700)
    Button(facilityframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=780)
    Button(facilityframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=860)
    Button(facilityframe,text="World Bank",command=wb,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=940)
    Button(facilityframe,text="Third World Network",command=twn,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1000)
    Button(facilityframe,text="Project Syndicate",command=ps,width=35,fg="dark blue",font="Lucida 14 bold",bg="azure4").place(x=790,y=1060)

    copyright = Label(facilityframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1650)
    facility.mainloop()
def showfaculty():
    pageclose()
    faculty.deiconify()
    faculty.protocol("WM_DELETE_WINDOW", on_closing)
    faculty.title("Faculty")
    faculty.geometry("1366x768")
    screenwidth = faculty.winfo_screenwidth()
    screenheight = faculty.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    faculty.wm_iconbitmap("1.ico")
    faculty.geometry(f"{screenwidth}x{screenheight}")

    c=Canvas(faculty,width=screenwidth-20,height=screenheight,bg="lavender")
    c.pack(expand=True,fill=BOTH,side=LEFT)
    facultyframe=Frame(c,bg="lavender",width=screenwidth-20,height=screenheight+270)
    facultyframe.pack(expand=1,fill=BOTH)
    c.create_window((0, 0), anchor='nw',width=screenwidth,window=facultyframe)
    scrollbar = Scrollbar(faculty,command=c.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    c.update_idletasks()
    scrollbar.config(command=c.yview)
    c.config(yscrollcommand=scrollbar.set)
    c.bind('<Configure>', lambda e: c.configure(scrollregion=c.bbox("all")))

    #aexecutequerrying logo
    logo=image1(facultyframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(facultyframe)
    window=image1(facultyframe,"2.jpg",screenwidth/2,150,screenwidth,350,1000)
    Label(facultyframe,text="Faculty",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)
    Label(facultyframe,text='''HSC management ensures that the candidates are
    provided the best available faculties that will provide them the wherewithal
    to excel in the written examination and the personality test.''',fg="black",bg="light skyblue3",font="Candara 20 italic").place(x=50,y=520)

    Label(facultyframe,text='''We have a panel of expert and experienced academicians,
    well versed with the requirements of the UPSC to broadbase the candidates’ knowledge
    and provide the required academic thrust to the aspirants. This panel also includes top
    ex-bureaucrats and media personalities who spare no pain in guiding the HSC
    candidates and leave no stone unturned in ensuring the candidates’ success.
    In aexecutequerryition to the above there are also 4 in-house Academic Associates who help the
    candidates in sourcing study materials, and preparing for the UPSC examinations.
    They set up periodical test papers, conduct tests, and arrange for evaluation of the
    test papers by external examiners.'''
        ,fg="black",font="Calibri 18 ",bg="light skyblue3").place(x=50,y=650)

    Label(facultyframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=980,y=460)

    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(facultyframe,text="Union Public Service Commission",command=upsc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=530)
    Button(facultyframe,text="Down to Earth",command=down_to_earth,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=570)
    Button(facultyframe,text="Press Information Bureau",command=pib,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=610)
    Button(facultyframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=650)
    Button(facultyframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=710)
    Button(facultyframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=770)
    Button(facultyframe,text="World Bank",command=wb,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=830)
    Button(facultyframe,text="Third World Network",command=twn,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=870)
    Button(facultyframe,text="Project Syndicate",command=ps,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=910)


    copyright = Label(facultyframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1000)

    faculty.mainloop()

def showaop():
    pageclose()
    aop.deiconify()
    aop.protocol("WM_DELETE_WINDOW", on_closing)
    aop.title("Admission Procedure")
    aop.geometry("1366x768")
    screenwidth = aop.winfo_screenwidth()
    screenheight = aop.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    aop.wm_iconbitmap("1.ico")
    aop.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(aop,width=screenwidth-20,height=screenheight,bg="lavender")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    aopframe=Frame(canvas,bg="lavender",width=screenwidth-20,height=screenheight+500)
    aopframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=aopframe)
    scrollbar = Scrollbar(aop,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    logo=image1(aopframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(aopframe)
    window=image1(aopframe,"25.jpg",screenwidth/2,150,screenwidth,300,1250)

    Label(aopframe,text="Admission Procedure",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)
    Label(aopframe,text='''Every year Hamdard Study Circle (HSC) conducts entrance
    examination for HSC Preliminary Programme, held normally in July, a little after the
    UPSC Prelims is conducted. Aspirants who wish to join the programme are admitted
    on the basis of an Entrance test and Interview.The entrance test is conducted all
    over India in HSC’s 25 centres–Ahmedabad, Allahabad, Aurangabad, Bangalore,
    Bhopal, Bareilly, Bidar, Calicut, Chennai, Jaipur, Kanpur, Lucknow, Kavaratti, Kolkata,
    Guwahati, Srinagar, Imphal, Hyderabad, Jammu, Mewat, Moradabad, Mumbai,
    New Delhi, Patna, Ranchi, Raipur, Port Blair and Thiruvananthapuram.'''
        ,fg="black",font="Calibri 15",bg="light skyblue3").place(x=50,y=520)
    Label(aopframe,text="The exam comprises:",bg="dark slate gray",fg="white",font="Castellar 20").place(x=50,y=750)
    Label(aopframe,text="-Objective General Studies Paper (100 questions), ",bg="light skyblue3",fg="black",font="Cascadia_Mono 17").place(x=50,y=800)
    Label(aopframe,text="-CSAT (Qualifying)",fg="black",font="Cascadia_Mono 17",bg="light skyblue3").place(x=50,y=850)
    Label(aopframe,text="-Essay Writing (Medium can be one among English, Hindi or Urdu).",bg="light skyblue3",fg="black",font="Cascadia_Mono 17").place(x=50,y=900)
    Label(aopframe,text='''
    Short listed candidates will be called for personality test
    which will be conducted in HSC premises at Talimabad,
    New Delhi. The interview panel consists of eminent
    bureaucrats, journalists, professors, and industrialists etc.
    Selection of candidates is based on merit. Application
    forms are filled, submitted and the nominal fee paid online
    List of selected candidates will be uploaded on the HSC website.
    They are also informed individually through email.''',bg="lavender",fg="black",font="Candara 17").place(x=50,y=950)


    Label(aopframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=980,y=460)

    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(aopframe,text="Union Public Service Commission",command=upsc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=530)
    Button(aopframe,text="Down to Earth",command=down_to_earth,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=570)
    Button(aopframe,text="Press Information Bureau",command=pib,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=610)
    Button(aopframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=650)
    Button(aopframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=710)
    Button(aopframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=770)
    Button(aopframe,text="World Bank",command=wb,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=830)
    Button(aopframe,text="Third World Network",command=twn,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=870)
    Button(aopframe,text="Project Syndicate",command=ps,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=910)


    copyright = Label(aopframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1250)

    aop.mainloop()
def showfounder():
    pageclose()
    founder.deiconify()
    founder.protocol("WM_DELETE_WINDOW", on_closing)
    founder.title("Founder")
    founder.geometry("1366x768")
    screenwidth = founder.winfo_screenwidth()
    screenheight = founder.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    founder.wm_iconbitmap("1.ico")
    founder.geometry(f"{screenwidth}x{screenheight}")
    canvas=Canvas(founder,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    founderframe=Frame(canvas,bg="white",width=screenwidth-20,height=screenheight+650)
    founderframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=founderframe)
    scrollbar = Scrollbar(founder,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    logo=image1(founderframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(founderframe)
    window=image1(founderframe,"32.png",screenwidth/2,150,screenwidth,300,1400)
    Label(founderframe,text="The Founder",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=50,y=460)
    Label(founderframe,text="Janab Hakeem Abdul Hameed Saheb ",bg="gray25",fg="lavender",font="Broadway 20").place(x=50,y=530)
    Label(founderframe,text='''In 1947 when the country was passing through untold social
    and political upheaval Janab Hakeem Abdul Hameed Saheb was scouting for land he
    could buy and build schools for the thousands of Muslims and other weak sections
    of society that stood on the brink of illiteracy, and socio-economic subservience.
    Poverty was staring them in the eyes. Hakeem Saheb realized that without modern
    education Muslims would remain caught in the vicious circle of abject poverty.
    Modern education was needed so that the coming generations would step out into
    the world with the educational empowerment which would put them at par with
    others.His foresight and vision saw him buying land in 1947 in what was then a
    foresaken forested area but is now an overcrowded locality known as Sangam Vihar.
    On this land Janab Hakeem Saheb laid the foundation of the Hamdard Education
    Society. This haloed campus was aptly named Talimabad. Hamdard Education Society,
    also known as HES has evolved as the apex body that runs several schools, coaching
    centres and the Hamdard Study Circle from here. It is one of the premier NGOs in
    the country concerned primarily with the education of minorities, rebuilding the
    nation through participation in civil administration, and the country-wide survey
    of Muslim managed schools and colleges. Hakeem Saheb also took up education
    and research activities establishing the Hamdard Charitable Trust in 1948 and the
    Hamdard National Foundation in 1964. He also established the Hamidia Charitable
    Hospital now known as the Centenary Hospital, and the Jamia Hamdard. Realizing
    the importance of education for the girl child he established the
    Rabea Girls Public School early in Old Delhi.Hakeem Abdul Hameed Saheb’s motto
    was austerity, simple living and selfless service. Throughout his life he practiced
    simple living and tempered it with great politeness, courtesy, and compassion in
    his dealing with all. A god-fearing person, and a philanthropist, Hakeem Saheb
    left for his heavenly abode in 1999 leaving his indelible footprints for us to follow.'''
        ,fg="black",font="Calibri 18").place(x=50,y=580)

    founderimage=Image.open("founder.png") 
    resized_founder=founderimage.resize((350,380),Image.LANCZOS)
    photo_founder=ImageTk.PhotoImage(resized_founder)
    L2=Label(founderframe,image=photo_founder,bg="dark blue")
    L2.place(x=980,y=460)

    Label(founderframe,text="-External Links",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline").place(x=980,y=860)

    def upsc():
        webbrowser.open("https://upsc.gov.in/")
    def down_to_earth():
        webbrowser.open("https://www.downtoearth.org.in/")
    def pib():
        webbrowser.open("https://pib.gov.in/indexm.aspx")
    def darpg():
        webbrowser.open("https://darpg.gov.in/")
    def lbsnaa():
        webbrowser.open("https://www.lbsnaa.gov.in/")
    def unfccc():
        webbrowser.open("https://unfccc.int/")
    def wb():
        webbrowser.open("https://www.worldbank.org/en/home")
    def twn():
        webbrowser.open("https://www.twn.my/")
    def ps():
        webbrowser.open("https://www.project-syndicate.org/")
    Button(founderframe,text="Union Public Service Commission",command=upsc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=930)
    Button(founderframe,text="Down to Earth",command=down_to_earth,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=970)
    Button(founderframe,text="Press Information Bureau",command=pib,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1010)
    Button(founderframe,text='''Department of Administrative Reforms
    and Public Grievances''',command=darpg,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1050)
    Button(founderframe,text='''Lal Bahadur Shastri National
        Academy of Administration''',command=lbsnaa,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1110)
    Button(founderframe,text='''United Nations Framework
    Convention on Climate Change''',command=unfccc,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1170)
    Button(founderframe,text="World Bank",command=wb,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1230)
    Button(founderframe,text="Third World Network",command=twn,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1270)
    Button(founderframe,text="Project Syndicate",command=ps,width=25,fg="dark blue",font="Lucida 12 bold",bg="azure4").place(x=980,y=1310)


    copyright = Label(founderframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=50)
    copyright.place(x=0,y=1400)
    
    founder.mainloop()
def showgallery():
    # global ac
    # ac=Toplevel(cw)
    pageclose()
    gallery.deiconify()
    gallery.protocol("WM_DELETE_WINDOW", on_closing)
    gallery.title("Advisory Committee")
    gallery.geometry("1366x768")
    screenwidth = gallery.winfo_screenwidth()
    screenheight = gallery.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    gallery.wm_iconbitmap("1.ico")
    gallery.geometry(f"{screenwidth}x{screenheight}")

    canvas=Canvas(gallery,width=screenwidth-20,height=screenheight,bg="white")
    canvas.pack(expand=True,fill=BOTH,side=LEFT)
    acframe=Frame(canvas,bg="lavender",width=screenwidth-20,height=screenheight+400)
    acframe.pack(expand=1,fill=BOTH)
    canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=acframe)
    scrollbar = Scrollbar(gallery,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #aexecutequerrying logo
    logo=image1(acframe,"hsc.png",130,55,255,100,100)
    #navigation bar
    navbar(acframe)
    window=image1(acframe,"24.jpg",screenwidth/2,150,screenwidth,300,370)
    #Gallery started
    Label(acframe,text="Gallery",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline",padx=180).place(x=screenwidth/2-150,y=420)
    # g1=image1(acframe,"9.png",250,150,int(screenwidth/3)-20,250,400)
    # g2=image1(acframe,"10.jpg",600,150,int(screenwidth/3)-20,250,400)
    # g3=image1(acframe,"11.png",250,150,int(screenwidth/3)-20,250,300)
    # g4=image1(acframe,"12.png",250,150,int(screenwidth/3)-20,250,300)

    g=Gallery(acframe,"9.png",225,150,"10.png",int(screenwidth/3)-50,250,1150,"11.png","12.png","13.png","14.png","15.png","16.png","17.png")
    Label(acframe,text="Our Co-founder",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=120,y=760)
    Label(acframe,text="Our Boards Member",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=550,y=760)
    Label(acframe,text="Our Inspirations",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=980,y=760)


    Label(acframe,text="Our Co-founder",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=120,y=1120)
    Label(acframe,text="Our Boards Member",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=550,y=1120)
    Label(acframe,text="Our Inspirations",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=980,y=1120)

    Label(acframe,text="Our Co-founder",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=120,y=1480)
    Label(acframe,text="Our Boards Member",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=550,y=1480)
    Label(acframe,text="Our Inspirations",font="Garamond 16 bold",fg="black",bg="cyan",padx=50).place(x=980,y=1480)

    copyright = Label(acframe,text="© Copyright 2019 Hamdard Study Circle. All Rights Reserved.",bg="black",fg="white",width=200,pady=40)
    copyright.place(x=0,y=1530)
    gallery.mainloop()
def showhome():
    pageclose()
    main.deiconify()
def navbar(framev):
    navigation = Frame(framev,bg="dark blue",bd=10)
    navigation.place(x=260,y=0)
    home = Button(navigation,text="Home",fg="white",bg="dark blue",font="lucida 12 underline",height=5,border=0,command=showhome)
    home.pack(side=LEFT,padx=18)
    def about():
        def toggle_button():
            advcb.place_forget()
            fonb.place_forget()
            cofob.place_forget()
        # f=Frame(main,width=165,height=85).place(x=350,y=80)
        advcb=Button(framev,text="Advisory Committee",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),showadvisory()])
        advcb.place(x=350,y=80)
        fonb=Button(framev,text="The Founder",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),showfounder()])
        fonb.place(x=350,y=106)
        cofob=Button(framev,text="Co-founder",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),showcofounder()])
        cofob.place(x=350,y=132)

    home = Button(navigation,text="About HSC",fg="white",bg="dark blue",command=about,font="lucida 12 underline",border=0)
    home.pack(side=LEFT,padx=18)
    def admission():
        def toggle_button():
            aopb.place_forget()
            facb.place_forget()
        facb=Button(framev,text="Faculty",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),showfaculty()])
        facb.place(x=370,y=80)
        aopb=Button(framev,text="Admission Procedure",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),showaop()])
        aopb.place(x=370,y=110)
    home=Button(navigation,text="Admission",command=admission,fg="white",bg="dark blue",font="lucida 12 underline",border=0)
    home.pack(side=LEFT,padx=18)
    home = Button(navigation,text="Fee Structure",fg="white",bg="dark blue",font="lucida 12 underline",border=0,command=showfee)
    home.pack(side=LEFT,padx=18)
    home = Button(navigation,text="Facilities",fg="white",bg="dark blue",font="lucida 12 underline",border=0,command=showfacility)
    home.pack(side=LEFT,padx=18)
    home = Button(navigation,text="Achievements",fg="white",bg="dark blue",font="lucida 12 underline",border=0,command=showachievement)
    home.pack(side=LEFT,padx=18)
    home = Button(navigation,text="Gallery",fg="white",bg="dark blue",font="lucida 12 underline",border=0,command=showgallery)
    home.pack(side=LEFT,padx=18)
    home = Button(navigation,text="Contact",fg="white",bg="dark blue",font="lucida 12 underline",border=0,command=showcontact)
    home.pack(side=LEFT,padx=18)
    #toggle button
    '''for login'''
    def toggle_login():
        def toggle_button():
            stb.place_forget()
            tb.place_forget()
            adb.place_forget()
        # f1=Frame(main,width=165,height=85,bg="dark blue").place(x=1200,y=80)
        stb=Button(framev,text="As student",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),loginstudent()])
        stb.place(x=1200,y=80)
        tb=Button(framev,text="As teacher",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),loginteacher()])
        tb.place(x=1200,y=106)
        adb=Button(framev,text="As admin",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),loginadmin()])
        adb.place(x=1200,y=132)
    home = Button(navigation,text="Login",fg="white",bg="dark blue",font="lucida 12 underline",command=toggle_login,border=0)
    home.pack(side=LEFT)
    def toggle_singup():
        def toggle_button():
            stb.place_forget()
            tb.place_forget()
            adb.place_forget()
        # f1=Frame(main,width=165,height=85,bg="dark blue").place(x=1200,y=80)
        stb=Button(framev,text="As student",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),signstudent()])
        stb.place(x=1200,y=80)
        tb=Button(framev,text="As teacher",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button(),signteacher()])
        tb.place(x=1200,y=106)
        adb=Button(framev,text="As admin",width=16,font="Lucida 12 bold",fg="black",command=lambda:[toggle_button()])
        adb.place(x=1200,y=132)
    home = Button(navigation,text="Register",command=toggle_singup,fg="white",bg="dark blue",font="lucida 12 underline",border=0)
    home.pack(side=LEFT,padx=16)
def showstudentdash(user,passw):
    def study():
        dash.deiconify()
        webbrowser.open("https://quizlet.com/")
    def attendance():
        dash.deiconify()
        att=Tk()
        att.title("Attendance")
        att.geometry("360x80")
        att.resizable(False,False)
        att.configure(bg="gray80")
        att.wm_iconbitmap("1.ico")
        Label(att,font="romania 10 bold",bg="gray80",text="Your attendance has been forwarded to your mail id.").place(x=5,y=10)
        def okk():
            att.destroy()
        Button(att,command=okk,text="OK",fg="black",font="romania 10 bold",bg="gray75").place(x=260,y=40)

    def edit():
        dash.deiconify()
        request=Tk()
        request.title("Edit profile request")
        request.geometry("320x80")
        request.resizable(False,False)
        request.configure(bg="gray80")
        request.wm_iconbitmap("1.ico")
        Label(request,font="romania 10 bold",bg="gray80",text="Your request has been forwarded to the Admin.").place(x=5,y=10)
        def ok():
            request.destroy()
        Button(request,command=ok,text="OK",fg="black",font="romania 10 bold",bg="gray85").place(x=250,y=45)

    def schedule():
        dash.deiconify()
        sched=Tk()
        sched.title("Class Schedule")
        sched.geometry("200x75")
        sched.resizable(False,False)
        sched.configure(bg="gray80")
        sched.wm_iconbitmap("1.ico")
        Label(sched,font="romania 10 bold",bg="gray80",text="No information available.").place(x=5,y=10)
        def close():
            sched.destroy()
            Button(sched,command=close,text="Close",fg="black",font="romania 10 bold",bg="gray85").place(x=120,y=40)
    def fees():
        dash.deiconify()
        fees=Tk()
        fees.title("Fees")
        fees.geometry("340x80")
        fees.resizable(False,False)
        fees.configure(bg="gray80")
        fees.wm_iconbitmap("1.ico")
        Label(fees,font="romania 10 bold",bg="gray80",text="No information available.KIndly approach admin.").place(x=5,y=10)
        def closee():
            fees.destroy()
        Button(fees,command=closee,text="Close",fg="black",font="romania 10 bold",bg="gray75").place(x=260,y=40)
    conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
    db=conn.cursor()
    db.execute("select * from student_data;")
    student_data=db.fetchall()
    conn.commit()
    conn.close()
    for i in student_data:
            if i[0]==user and i[1]==passw:
                Name=i[2]
                Course=i[3]
                phone=i[4]
                dob=i[5]
                Father=i[6]
                Mother=i[7]
                Joining=i[8]
                Valid=i[9]



    pageclose()
    dash.deiconify()
    dash.protocol("WM_DELETE_WINDOW",on_closing)
    dash.title("Student Dashboard")
    dash.geometry("1366x768")
    screenwidth = dash.winfo_screenwidth()
    screenheight = dash.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    dash.wm_iconbitmap("1.ico")
    dash.geometry(f"{screenwidth}x{screenheight}")

    dashc=Canvas(dash,width=550,height=screenheight,bg="dimgray")
    dashc.place(x=0,y=0)
    dashframe=Frame(dashc,bg="dimgray")
    dashframe.pack(expand=1,fill=BOTH)
    dashc.create_window((0, 0), anchor='nw',width=550,window=dashframe)

    Label(dashc,text="Name : ",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=260)
    Label(dashc,text="Course:",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=300)
    Label(dashc,text="Phone No. :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=340)
    Label(dashc,text="D.O.B :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=380)
    Label(dashc,text="Father's Name :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=420)
    Label(dashc,text="Mother's Name :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=460)
    Label(dashc,text="Joining Date :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=500)
    Label(dashc,text="Valid till :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=540)

    Label(dashc,text=f"{Name}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=260)
    Label(dashc,text=f"{Course}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=300)
    Label(dashc,text=f"{phone}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=340)
    Label(dashc,text=f"{dob}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=380)
    Label(dashc,text=f"{Father}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=420)
    Label(dashc,text=f"{Mother}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=460)
    Label(dashc,text=f"{Joining}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=500)
    Label(dashc,text=f"{Valid}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=540)

    c1="020f12"
    c2="lightcyan2"
    c3="thistle4"
    c4="black"
    button1=Button(
        dashc,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=9,height=1,
        border=5,cursor="hand1",command=edit,text="Edit",font="arial 16 bold")
    button1.place(x=180,y=590)
    dashcc=Canvas(dash,width=screenwidth-550,height=screenheight,bg="gray80")
    dashcc.place(x=550,y=0)
    dashfframe=Frame(dashcc,bg="gray80")
    dashfframe.pack(expand=1,fill=BOTH)
    dashcc.create_window((550, 0), anchor='nw',width=screenwidth-550,window=dashfframe)
    def back():
        dash.destroy()
        main.deiconify()
    Button(dashcc,text="<<Back To Main Page",font="Italic 15 bold",command=back).place(x=500,y=30)
    stu1=Image.open("stu1.jpg") 
    resized_stu1=stu1.resize((200,180),Image.LANCZOS)
    photo_stu1=ImageTk.PhotoImage(resized_stu1)
    Label(dashcc,text="Study Material",font="arial 15 bold").place(x=190,y=300)
    button2=Button(
        dashcc,command=study,image=photo_stu1,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button2.place(x=160,y=100)

    stu2=Image.open("stu2.jpg") 
    resized_stu2=stu2.resize((200,180),Image.LANCZOS)
    photo_stu2=ImageTk.PhotoImage(resized_stu2)
    Label(dashcc,text="Attendance",font="arial 15 bold").place(x=450,y=300)
    button3=Button(
        dashcc,command=attendance,image=photo_stu2,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button3.place(x=450,y=100)

    stu3=Image.open("stu3.jpg") 
    resized_stu3=stu3.resize((200,180),Image.LANCZOS)
    photo_stu3=ImageTk.PhotoImage(resized_stu3)
    Label(dashcc,text="Class Schedule",font="arial 15 bold").place(x=160,y=580)
    button4=Button(
        dashcc,command=schedule,image=photo_stu3,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button4.place(x=160,y=380)

    stu4=Image.open("stu4.png") 
    resized_stu4=stu4.resize((200,180),Image.LANCZOS)
    photo_stu4=ImageTk.PhotoImage(resized_stu4)
    Label(dashcc,text="Fees",font="arial 15 bold").place(x=450,y=580)
    button5=Button(
        dashcc,command=fees,image=photo_stu4,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button5.place(x=450,y=380)

    dash.mainloop()

def loginstudent():
    def login():
        count=0
        user=entry1.get()
        user=user.upper()
        passw=entry2.get()
        conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
        db=conn.cursor()
        db.execute("select * from student_data;")
        student_data=db.fetchall()
        conn.commit()
        conn.close()
        for i in student_data:
                if i[0]==user and i[1]==passw:
                    count+=1
                    showstudentdash(user,passw)
        if count!=1:
            response=tmsg.askokcancel("HSC","You have entered the wrong answer Please Try Again...")
            if response:
                loginstudent()
            else:
                main.deiconify()


    pageclose()
    stlog.deiconify()
    stlog.protocol("WM_DELETE_WINDOW",on_closing)
    stlog.title("Student Login")
    stlog.geometry("920x550")
    screenwidth = 920
    screenheight =550
    stlog.resizable(False,False)
    stlog.configure(bg="white")
    print(screenwidth)
    print(screenheight)
    stlogc=Canvas(stlog,width=470,height=screenheight,bg="white")
    stlogc.place(x=0,y=0)
    stlogframe=Frame(stlogc,width=470,height=screenheight,bg="white")
    stlogframe.pack()
    stlogc.create_window((0, 0), anchor='nw',width=470,window=stlogframe)

    login_stlog=Image.open("login_admn.png") 
    resized_login_stlog=login_stlog.resize((300,400),Image.LANCZOS)
    photo_login_stlog=ImageTk.PhotoImage(resized_login_stlog)
    Label(stlogframe,image=photo_login_stlog,border=0).place(x=55,y=80)

    stlogcc=Canvas(stlog,width=screenwidth-471,height=screenheight,bg="white")
    stlogcc.place(x=470,y=0)
    stlogframee=Frame(stlogcc,width=screenwidth-471,height=screenheight,bg="white")
    stlogframee.place(x=470,y=0)
    stlogcc.create_window((470, 0), anchor='nw',width=471,window=stlogframee)
    Label(stlog,text="LOGIN",font="algerian 30 underline",fg="firebrick4",bg="white").place(x=630,y=40)

    Label(stlog,text="Username",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=100)
    entry1=Entry(stlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry1.place(x=490,y=130)

    Label(stlog,text="Password",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=160)
    entry2=Entry(stlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry2.place(x=490,y=190)

    Button(stlog,text="Forgot password?",
        font="century 10 bold",fg="black",
        bg="white",activebackground="skyblue4",
        activeforeground="blue4",
        highlightthickness=2,
        highlightbackground="black",
        highlightcolor="white",width=15,height=1,
        border=2,cursor="hand1").place(x=685,y=240)

    stlog_log=Image.open("login.png") 
    resized_stlog_log=stlog_log.resize((270,160),Image.LANCZOS)
    photo_stlog_log=ImageTk.PhotoImage(resized_stlog_log)
    Button(stlog,image=photo_stlog_log,bg="black",
    highlightthickness=2,border=1,cursor="hand1",width=210,height=25,command=login).place(x=570,y=290)

    stlog_sign=Image.open("signup.jpg") 
    resized_stlog_sign=stlog_sign.resize((270,160),Image.LANCZOS)
    photo_stlog_sign=ImageTk.PhotoImage(resized_stlog_sign)
    Button(stlog,image=photo_stlog_sign,bg="black",
    highlightthickness=2,border=1,cursor="hand1",width=210,height=25).place(x=570,y=360)

    stlog.mainloop()
def showteacherdash(user,passw):
    def tea_att():
        tea.deiconify()
        tea_att=Tk()
        tea_att.title("Attendance")
        tea_att.geometry("360x80")
        tea_att.resizable(False,False)
        tea_att.configure(bg="gray80")
        tea_att.wm_iconbitmap("1.ico")
        Label(tea_att,font="romania 10 bold",bg="gray80",text="Your attendance has been forwarded to your mail id.").place(x=5,y=10)
        def tea_ok():
            tea_att.destroy()
        Button(tea_att,command=tea_ok,text="OK",fg="black",font="romania 10 bold",bg="gray75").place(x=260,y=40)

    def tea_edit():
        tea.deiconify()
        tea_edit=Tk()
        tea_edit.title("Edit profile request")
        tea_edit.geometry("320x80")
        tea_edit.resizable(False,False)
        tea_edit.configure(bg="gray80")
        tea_edit.wm_iconbitmap("1.ico")
        Label(tea_edit,font="romania 10 bold",bg="gray80",text="Your request has been forwarded to the Admin.").place(x=5,y=10)
        def tea_ok():
            tea_edit.destroy()
        Button(tea_edit,command=tea_ok,text="OK",fg="black",font="romania 10 bold",bg="gray85").place(x=250,y=45)

    def tea_schedule():
        tea.deiconify()
        tea_sched=Tk()
        tea_sched.title("Class Schedule")
        tea_sched.geometry("200x75")
        tea_sched.resizable(False,False)
        tea_sched.configure(bg="gray80")
        tea_sched.wm_iconbitmap("1.ico")
        Label(tea_sched,font="romania 10 bold",bg="gray80",text="No information available.").place(x=5,y=10)
        def tea_close():
            tea_sched.destroy()
        Button(tea_sched,command=tea_close,text="Close",fg="black",font="romania 10 bold",bg="gray85").place(x=120,y=40)
    def salary():
        tea.deiconify()
        tea_sal=Tk()
        tea_sal.title("Salary")
        tea_sal.geometry("320x80")
        tea_sal.resizable(False,False)
        tea_sal.configure(bg="gray80")
        tea_sal.wm_iconbitmap("1.ico")
        Label(tea_sal,font="romania 10 bold",bg="gray80",text="Not updated").place(x=5,y=10)
        def tea_sal_ok():
            tea_sal.destroy()
        Button(tea_sal,command=tea_sal_ok,text="OK",fg="black",font="romania 10 bold",bg="gray85").place(x=250,y=45)
    conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
    db=conn.cursor()
    db.execute("select * from teacher_data;")
    teacher_data=db.fetchall()
    conn.commit()
    conn.close()
    for i in teacher_data:
            if i[0]==user and i[1]==passw:
                Name=i[2]
                Course=i[3]
                phone=i[4]
                dob=i[5]
                Father=i[6]
                Mother=i[7]
                Joining=i[8]
                Valid=i[9]


    pageclose()
    tea.deiconify()
    tea.protocol("WM_DELETE_WINDOW",on_closing)
    tea.title("Teacher Dashboard")
    tea.geometry("1366x768")
    screenwidth = tea.winfo_screenwidth()
    screenheight = tea.winfo_screenheight()
    print(screenwidth)
    print(screenheight)
    tea.wm_iconbitmap("1.ico")
    tea.geometry(f"{screenwidth}x{screenheight}")

    teacc=Canvas(tea,width=550,height=screenheight,bg="dimgray")
    teacc.place(x=0,y=0)
    teaframe=Frame(teacc,bg="dimgray")
    teaframe.pack(expand=1,fill=BOTH)
    teacc.create_window((0, 0), anchor='nw',width=550,window=teaframe)

    def syllabus():
        tea.deiconify()
        syl=Tk()
        syl.title("Syllabus Planner")
        syl.geometry("300x200")
        syl.configure(bg="gray80")
        syl.wm_iconbitmap("1.ico")
        sylc=Canvas(syl,width=300,height=200,bg="lavender")
        sylc.pack(expand=True,fill=BOTH,side=LEFT)
        sylframe=Frame(sylc,bg="lavender",width=300,height=200)
        sylframe.pack(expand=1,fill=BOTH)
        Entry(sylframe,font="consolas 15",bg="lavender").place(x=0,y=0)
        
    Label(teacc,text="Name : ",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=260)
    Label(teacc,text="Subject:",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=300)
    Label(teacc,text="Phone No. :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=340)
    Label(teacc,text="D.O.B :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=380)
    Label(teacc,text="Father's Name :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=420)
    Label(teacc,text="Mother's Name :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=460)
    Label(teacc,text="Joining Date :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=500)
    Label(teacc,text="Extension till :",bg="dimgray",fg="black",font="romania 15 ").place(x=10,y=540)

    
    Label(teacc,text=f"{Name}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=260)
    Label(teacc,text=f"{Course}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=300)
    Label(teacc,text=f"{phone}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=340)
    Label(teacc,text=f"{dob}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=380)
    Label(teacc,text=f"{Father}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=420)
    Label(teacc,text=f"{Mother}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=460)
    Label(teacc,text=f"{Joining}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=500)
    Label(teacc,text=f"{Valid}",bg="dimgray",fg="black",font="romania 15 ").place(x=180,y=540)

    c1="020f12"
    c2="lightcyan2"
    c3="thistle4"
    c4="black"
    button1=Button(
        teacc,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=9,height=1,
        border=5,cursor="hand1",command=tea_edit,text="Edit",font="arial 16 bold")
    button1.place(x=180,y=590)
    teac=Canvas(tea,width=screenwidth-550,height=screenheight,bg="gray80")
    teac.place(x=550,y=0)
    teafframe=Frame(teac,bg="gray80")
    teafframe.pack(expand=1,fill=BOTH)
    teac.create_window((550, 0), anchor='nw',width=screenwidth-550,window=teafframe)
    def back():
        tea.destroy()
        main.deiconify()
    Button(teac,text="<<Back To Main Page",font="Italic 15 bold",command=back).place(x=500,y=30)

    tea1=Image.open("tea1.jpg") 
    resized_tea1=tea1.resize((200,180),Image.LANCZOS)
    photo_tea1=ImageTk.PhotoImage(resized_tea1)
    Label(teac,text="Syllabus Planner",font="arial 15 bold").place(x=190,y=300)
    button2=Button(
        teac,command=syllabus,image=photo_tea1,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button2.place(x=160,y=100)

    tea2=Image.open("tea2.jpg") 
    resized_tea2=tea2.resize((200,180),Image.LANCZOS)
    photo_tea2=ImageTk.PhotoImage(resized_tea2)
    Label(teac,text="Attendance",font="arial 15 bold").place(x=450,y=300)
    button3=Button(
        teac,command=tea_att,image=photo_tea2,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button3.place(x=450,y=100)
    tea3=Image.open("tea3.jpg") 
    resized_tea3=tea3.resize((200,180),Image.LANCZOS)
    photo_tea3=ImageTk.PhotoImage(resized_tea3)
    Label(teac,text="Class Schedule",font="arial 15 bold").place(x=160,y=580)
    button4=Button(
        teac,command=tea_schedule,image=photo_tea3,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button4.place(x=160,y=380)

    tea4=Image.open("tea4.png") 
    resized_tea4=tea4.resize((200,180),Image.LANCZOS)
    photo_tea4=ImageTk.PhotoImage(resized_tea4)
    Label(teac,text="Salary",font="arial 15 bold").place(x=450,y=580)
    button5=Button(
        teac,command=salary,image=photo_tea4,bg=c2,
        fg=c4,activebackground=c3,
        activeforeground=c4,highlightthickness=2,
        highlightbackground=c2,highlightcolor="white",
        width=200,height=180,
        border=4,cursor="hand1")
    button5.place(x=450,y=380)
    tea.mainloop()
def loginteacher():
    def login():
        count=0
        user=entry1.get()
        user=user.upper()
        passw=entry2.get()
        conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
        db=conn.cursor()
        db.execute("select * from teacher_data;")
        teacher_data=db.fetchall()
        conn.commit()
        conn.close()
        for i in teacher_data:
                print(i[0],i[1])
                if i[0]==user and i[1]==passw:
                    count+=1
                    showteacherdash(user,passw)
        if count!=1:
            response=tmsg.askokcancel("HSC","You have entered the wrong answer Please Try Again...")
            if response:
                loginteacher()
            else:
                main.deiconify()


    pageclose()
    tchlog.deiconify()
    tchlog.protocol("WM_DELETE_WINDOW",on_closing)
    tchlog.title("Teacher Login")
    tchlog.geometry("920x550")
    screenwidth = 920
    screenheight =550
    tchlog.resizable(False,False)
    tchlog.configure(bg="white")
    print(screenwidth)
    print(screenheight)
    tchlogc=Canvas(tchlog,width=470,height=screenheight,bg="white")
    tchlogc.place(x=0,y=0)
    tchlogframe=Frame(tchlogc,width=470,height=screenheight,bg="white")
    tchlogframe.pack()
    tchlogc.create_window((0, 0), anchor='nw',width=470,window=tchlogframe)

    login_tchlog=Image.open("login_admn.png") 
    resized_login_tchlog=login_tchlog.resize((300,400),Image.LANCZOS)
    photo_login_tchlog=ImageTk.PhotoImage(resized_login_tchlog)
    Label(tchlogframe,image=photo_login_tchlog,border=0).place(x=55,y=80)

    tchlogcc=Canvas(tchlog,width=screenwidth-471,height=screenheight,bg="white")
    tchlogcc.place(x=470,y=0)
    tchlogframee=Frame(tchlogcc,width=screenwidth-471,height=screenheight,bg="white")
    tchlogframee.place(x=470,y=0)
    tchlogcc.create_window((470, 0), anchor='nw',width=471,window=tchlogframee)
    Label(tchlog,text="LOGIN",font="algerian 30 underline",fg="firebrick4",bg="white").place(x=630,y=40)

    Label(tchlog,text="Username",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=100)
    entry1=Entry(tchlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry1.place(x=490,y=130)

    Label(tchlog,text="Password",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=160)
    entry2=Entry(tchlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry2.place(x=490,y=190)

    Button(tchlog,text="Forgot password?",
        font="century 10 bold",fg="black",
        bg="white",activebackground="skyblue4",
        activeforeground="blue4",
        highlightthickness=2,
        highlightbackground="black",
        highlightcolor="white",width=15,height=1,
        border=2,cursor="hand1").place(x=685,y=240)

    tchlog_log=Image.open("login.png") 
    resized_tchlog_log=tchlog_log.resize((270,160),Image.LANCZOS)
    photo_tchlog_log=ImageTk.PhotoImage(resized_tchlog_log)
    Button(tchlog,image=photo_tchlog_log,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=210,height=25,command=login).place(x=570,y=290)

    tchlog_sign=Image.open("signup.jpg") 
    resized_tchlog_sign=tchlog_sign.resize((270,160),Image.LANCZOS)
    photo_tchlog_sign=ImageTk.PhotoImage(resized_tchlog_sign)
    Button(tchlog,image=photo_tchlog_sign,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=210,height=25).place(x=570,y=360)

    tchlog.mainloop()

def loginadmin():
    pageclose()
    adminlog.deiconify()
    adminlog.protocol("WM_DELETE_WINDOW",on_closing)
    adminlog.title("Admin Login")
    adminlog.geometry("920x550")
    screenwidth = 920
    screenheight =550
    adminlog.resizable(False,False)
    adminlog.configure(bg="white")
    print(screenwidth)
    print(screenheight)
    adminlogc=Canvas(adminlog,width=470,height=screenheight,bg="white")
    adminlogc.place(x=0,y=0)
    adminlogframe=Frame(adminlogc,width=470,height=screenheight,bg="white")
    adminlogframe.pack()
    adminlogc.create_window((0, 0), anchor='nw',width=470,window=adminlogframe)

    login_adminlog=Image.open("login_admn.png") 
    resized_login_adminlog=login_adminlog.resize((300,400),Image.LANCZOS)
    photo_login_adminlog=ImageTk.PhotoImage(resized_login_adminlog)
    Label(adminlogframe,image=photo_login_adminlog,border=0).place(x=55,y=80)

    adminlogcc=Canvas(adminlog,width=screenwidth-471,height=screenheight,bg="white")
    adminlogcc.place(x=470,y=0)
    adminlogframee=Frame(adminlogcc,width=screenwidth-471,height=screenheight,bg="white")
    adminlogframee.place(x=470,y=0)
    adminlogcc.create_window((470, 0), anchor='nw',width=471,window=adminlogframee)
    Label(adminlog,text="LOGIN",font="algerian 30 underline",fg="firebrick4",bg="white").place(x=630,y=40)

    Label(adminlog,text="Username",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=100)
    entry1=Entry(adminlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry1.place(x=490,y=130)

    Label(adminlog,text="Password",font="catholic 12 bold",fg="dimgray",bg="white").place(x=490,y=160)
    entry2=Entry(adminlog,border=5,font="century 15",fg="black",width=30,bg="lavender")
    entry2.place(x=490,y=190)

    def forgot():
        adminlog.deiconify()
        forgot=Tk()
        forgot.title("Forgot Password")
        forgot.geometry("380x80")
        forgot.resizable(False,False)
        forgot.configure(bg="gray99")
        forgot.wm_iconbitmap("1.ico")
        Label(forgot,font="century 10 bold",bg="gray99",text="Your new password has been sent to your mail id.").place(x=5,y=10)
        def dialog_close():
            forgot.destroy()
        Button(forgot,command=dialog_close,text="Close",activebackground="gray75",fg="thistle4",font="century 10",bg="gray99").place(x=300,y=40)


    Button(adminlog,text="Forgot password?",
        font="century 10 bold",fg="black",
        bg="white",activebackground="skyblue4",
        activeforeground="blue4",
        highlightthickness=2,
        highlightbackground="black",
        highlightcolor="white",width=15,height=1,
        border=2,cursor="hand1",command=forgot).place(x=685,y=240)

    adminlog_log=Image.open("login.png") 
    resized_adminlog_log=adminlog_log.resize((270,160),Image.LANCZOS)
    photo_adminlog_log=ImageTk.PhotoImage(resized_adminlog_log)
    Button(adminlog,image=photo_adminlog_log,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=210,height=25).place(x=570,y=290)

    adminlog_sign=Image.open("signup.jpg") 
    resized_adminlog_sign=adminlog_sign.resize((270,160),Image.LANCZOS)
    photo_adminlog_sign=ImageTk.PhotoImage(resized_adminlog_sign)
    Button(adminlog,image=photo_adminlog_sign,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=210,height=25).place(x=570,y=360)

    adminlog.mainloop()

def signstudent():
    pageclose()
    sgst.deiconify()
    sgst.protocol("WM_DELETE_WINDOW",on_closing)
    sgst.title("Student Singup")
    screenwidth = 850
    screenheight =600
    sgst.geometry(f"{screenwidth}x{screenheight}")
    sgst.resizable(False,False)
    sgst.configure(bg="white")
    print(screenwidth)
    print(screenheight)
    canvas =Canvas(sgst,bg="lavender",height=screenheight,width=screenwidth)
    canvas.pack(fill=X)
    background_image = PhotoImage(file="33.png")
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.background = background_image

    Label(canvas,text="Sing Up",font="algerian 30 underline",fg="white",bg="firebrick4").place(x=screenwidth/2-50,y=10)
    Label(canvas,text="Name :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=80)
    Label(canvas,text="Course :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=150-20)
    Label(canvas,text="Phone No :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=200-20)
    Label(canvas,text="Father :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=250-20)
    Label(canvas,text="Mother :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=300-20)
    Label(canvas,text="D.O.B :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=350-20)
    Label(canvas,text="Joining Date :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=400-20)
    Label(canvas,text="Validity :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=450-20)
    Label(canvas,text="Username :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=500-20)
    Label(canvas,text="Password :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=550-20)

    name=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    name.place(x=250,y=80)
    course=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    course.place(x=250,y=130)
    phone=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    phone.place(x=250,y=180)
    father=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    father.place(x=250,y=230)
    mother=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    mother.place(x=250,y=280)
    dob=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    dob.place(x=250,y=330)
    jod=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    jod.place(x=250,y=380)
    vod=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    vod.place(x=250,y=430)
    newuser=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    newuser.place(x=250,y=480)
    newpassw=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    newpassw.place(x=250,y=530)
    canvas.create_line(600,0,600,screenheight,width=7,fill="firebrick4")
    canvas.create_line(600,screenheight/2,screenwidth,screenheight/2,width=7,fill="firebrick4")


    def insertdata():
        conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
        db=conn.cursor()
        print(conn.is_connected())
        db.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(newuser.get(),
                                                                                     newpassw.get(),
                                                                                     name.get(),
                                                                                     course.get(),
                                                                                     phone.get(),
                                                                                     dob.get(),
                                                                                     father.get(),
                                                                                     mother.get(),
                                                                                     jod.get(),
                                                                                     vod.get()
                                                                                     ))
        conn.commit()
        conn.close()

    tchlog_log=Image.open("login.png") 
    resized_tchlog_log=tchlog_log.resize((200,250),Image.LANCZOS)
    photo_tchlog_log=ImageTk.PhotoImage(resized_tchlog_log)
    Button(canvas,image=photo_tchlog_log,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=200,height=250,command=loginstudent).place(x=620,y=screenheight/2+25)

    tchlog_sign=Image.open("signup.jpg") 
    resized_tchlog_sign=tchlog_sign.resize((200,250),Image.LANCZOS)
    photo_tchlog_sign=ImageTk.PhotoImage(resized_tchlog_sign)
    Button(canvas,image=photo_tchlog_sign,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=200,height=250,command=insertdata).place(x=620,y=25)

    sgst.mainloop()
def signteacher():
    pageclose()
    sgtc.deiconify()
    sgtc.protocol("WM_DELETE_WINDOW",on_closing)
    sgtc.title("Teacher Singup")
    screenwidth = 850
    screenheight =600
    sgtc.geometry(f"{screenwidth}x{screenheight}")
    sgtc.resizable(False,False)
    sgtc.configure(bg="white")
    print(screenwidth)
    print(screenheight)
    canvas =Canvas(sgtc,bg="lavender",height=screenheight,width=screenwidth)
    canvas.pack(fill=X)
    background_image = PhotoImage(file="33.png")
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.background = background_image

    Label(canvas,text="Sing Up",font="algerian 30 underline",fg="white",bg="firebrick4").place(x=screenwidth/2-50,y=10)
    Label(canvas,text="Name :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=80)
    Label(canvas,text="Course :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=150-20)
    Label(canvas,text="Phone No :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=200-20)
    Label(canvas,text="Father :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=250-20)
    Label(canvas,text="Mother :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=300-20)
    Label(canvas,text="D.O.B :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=350-20)
    Label(canvas,text="Joining Date :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=400-20)
    Label(canvas,text="Extension :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=450-20)
    Label(canvas,text="Username :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=500-20)
    Label(canvas,text="Password :- ",font="algerian 20 underline",fg="white",bg="gray17").place(x=50,y=550-20)

    name=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    name.place(x=250,y=80)
    course=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    course.place(x=250,y=130)
    phone=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    phone.place(x=250,y=180)
    father=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    father.place(x=250,y=230)
    mother=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    mother.place(x=250,y=280)
    dob=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    dob.place(x=250,y=330)
    jod=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    jod.place(x=250,y=380)
    extension=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    extension.place(x=250,y=430)
    newuser=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    newuser.place(x=250,y=480)
    newpassw=Entry(canvas,border=3,font="century 18",fg="white",width=25,bg="gray60")
    newpassw.place(x=250,y=530)
    canvas.create_line(600,0,600,screenheight,width=7,fill="firebrick4")
    canvas.create_line(600,screenheight/2,screenwidth,screenheight/2,width=7,fill="firebrick4")

    def insertdata():
        conn=mysql.connector.connect(host="localhost",user="root",password="Rushaan@2006",database="hsc")
        db=conn.cursor()
        print(conn.is_connected())
        db.execute("insert into teacher_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(newuser.get(),
                                                                                     newpassw.get(),
                                                                                     name.get(),
                                                                                     course.get(),
                                                                                     phone.get(),
                                                                                     dob.get(),
                                                                                     father.get(),
                                                                                     mother.get(),
                                                                                     jod.get(),
                                                                                     extension.get()
                                                                                     ))
        conn.commit()
        conn.close()
    tchlog_log=Image.open("login.png") 
    resized_tchlog_log=tchlog_log.resize((200,250),Image.LANCZOS)
    photo_tchlog_log=ImageTk.PhotoImage(resized_tchlog_log)
    Button(canvas,image=photo_tchlog_log,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=200,height=250,command=loginteacher).place(x=620,y=screenheight/2+25)

    tchlog_sign=Image.open("signup.jpg") 
    resized_tchlog_sign=tchlog_sign.resize((200,250),Image.LANCZOS)
    photo_tchlog_sign=ImageTk.PhotoImage(resized_tchlog_sign)
    Button(canvas,image=photo_tchlog_sign,bg="black",
        highlightthickness=2,border=1,cursor="hand1",width=200,height=250,command=insertdata).place(x=620,y=25)
    sgtc.mainloop()

main=Tk()

tea=Toplevel(main)
tea.withdraw()

sgst=Toplevel(main)
sgst.withdraw()

sgtc=Toplevel(main)
sgtc.withdraw()

dash=Toplevel(main)
dash.withdraw()

stlog=Toplevel(main)
stlog.withdraw()

tchlog=Toplevel(main)
tchlog.withdraw()

adminlog=Toplevel(main)
adminlog.withdraw()

contact=Toplevel(main)
contact.withdraw()

coFounder=Toplevel(main)
coFounder.withdraw()

advc=Toplevel(main)
advc.withdraw()

ach=Toplevel(main)
ach.withdraw()

fee=Toplevel(main)
fee.withdraw()

facility=Toplevel(main)
facility.withdraw()

faculty=Toplevel(main)
faculty.withdraw()

gallery=Toplevel(main)
gallery.withdraw()

founder=Toplevel(main)
founder.withdraw()

aop=Toplevel(main)
aop.withdraw()

main.protocol("WM_DELETE_WINDOW", on_closing)

main.title("Hamdard Study Circle")
screenwidth = main.winfo_screenwidth()
screenheight = main.winfo_screenheight()
print(screenwidth)
print(screenheight)
main.wm_iconbitmap("1.ico")
main.geometry(f"{screenwidth}x{screenheight}")


canvas=Canvas(main,width=screenwidth-20,height=screenheight-30,bg="lavender")
canvas.pack(expand=True,fill=BOTH,side=LEFT)
mainframe=Frame(canvas,bg="lavender")
mainframe.pack(expand=1,fill=BOTH)
canvas.create_window((0, 0), anchor='nw',width=screenwidth,window=mainframe)
scrollbar = Scrollbar(main,command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)
canvas.update_idletasks()
canvas.config(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

logo=image1(mainframe,"hsc.png",130,55,255,100,100)
navbar(mainframe)
#images
window=image1(mainframe,"hscbuilding.jpg",screenwidth/2,150,screenwidth,300,1200)
canvas2=Canvas(mainframe,height=50,width=screenwidth)
canvas2.place(x=10,y=405)
canvas_text = canvas2.create_text(10, 10, text='', anchor=NW, font=("Bernard_MT" ,15), fill="black")

test_string = "THE LIST OF SELECTED CANDIDATES FOR UPSC C.S. PRELIMS COACHING PROGRAMME 23-24 RELEASED. PLEASE SEE THE DETAILS IN “LATEST NEWS & EVENT"

#Time delay between chars, in milliseconds
delta = 100 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas2.itemconfigure(canvas_text, text=s)
    canvas2.after(delay, update_text)
    delay += delta
Label(mainframe,text="WELCOME TO HUMDARD STUDY CIRCLE",bg="dark slate gray",fg="white",font="Bernard_MT 30 underline",justify=CENTER).place(x=50,y=450)
Label(mainframe,text='''Arise, awake and stop not till the goal is reached''',fg="black",bg="light skyblue3",font="Candara 20 italic").place(x=50,y=520)


main.mainloop()
