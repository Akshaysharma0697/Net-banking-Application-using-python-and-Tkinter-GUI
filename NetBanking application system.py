from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import mysql.connector
import time

con = mysql.connector.connect(host='localhost', user='root', database='bankapp')  # password if there is password
cursor = con.cursor()

root = Tk()  # window creation
root.geometry("1366x768+0+0")
root.config(bg="black")
root.title("Net banking application")
root.resizable(0, 0)


def home():
    frame1 = Frame(root, width=1366, height=768)
    frame1.pack()
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\money.jpg'))
    Label(frame1, image=img, width='1366', height='768').place(x=0, y=0)
    Label(frame1, text=' Net Banking Application', bg='black', fg='white', font=('Yu Gothic', 40, 'bold')).place(x=410,
                                                                                                                 y=0)
    Label(frame1, width='62', height='30', bg='grey', bd=8).place(x=500, y=170)
    Label(frame1, text='LOGIN', fg='white', bg='black', font=('Yu Gothic', 15, 'bold')).place(x=670, y=180)

    accnt_no1 = IntVar()
    accnt_no1.set('')
    password1 = StringVar()

    Label(frame1, text='Account number', fg='white', bg='black', font=('Yu Gothic', 15, 'bold')).place(x=510, y=300)
    e1 = Entry(frame1, bd=5, width=30, text=accnt_no1).place(x=700, y=300)

    Label(frame1, text='Password', fg='white', bg='black', font=('Yu Gothic', 15, 'bold')).place(x=510, y=360)
    e2 = Entry(frame1, bd=5, width=30, show='*', text=password1).place(x=700, y=360)

    b1 = Button(frame1, text='LOGIN', width=14, bd=6, bg='gray', font=('arial', 10, 'bold'),
                command=lambda: login_check())
    b1.place(x=505, y=450)

    b2 = Button(frame1, text='SIGNUP', width=14, bd=6, bg='gray', font=('arial', 10, 'bold'),
                command=lambda: signup(frame1, root))
    b2.place(x=655, y=450)

    b3 = Button(frame1, text='FORGOT PASSWORD', width=16, bd=6, bg='gray', font=('arial', 10, 'bold'),
                command=lambda: forget_password(frame1, root))
    b3.place(x=800, y=450)

    b4 = Button(frame1, text='EXIT', width=16, bd=6, bg='gray', font=('arial', 10, 'bold'), command=lambda: iExit(root))
    b4.place(x=655, y=550)

    def login_check():
        accnt_no = accnt_no1.get()
        password = password1.get()
        query1 = f'select accnt_no,password from details'
        cursor.execute(query1)
        records = cursor.fetchall()
        dict = {}
        for a, b in records:
            dict[a] = b
        if dict[accnt_no] == password:
            login(frame1, root, accnt_no)
            exit()
        else:
            q = tkinter.messagebox.showerror("ERROR", "wrong account number or password")
            reset(frame1, root)
        """for row in records:
            if row[0] == accnt_no and row[1] == password:
                login(frame1,root,accnt_no)
                exit()
            else:
                #q = tkinter.messagebox.showerror("ERROR", "wrong account number or password")

                reset(frame1, root)
        """

    frame1.mainloop()


def reset(frame1, root):
    frame1.destroy()
    home()


def login(frame1, root, accnt_no):
    frame1.destroy()
    frame2 = Frame(root, width='1366', height='768')
    frame2.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\onlinebanking.jpg'))
    Label(frame2, image=img, height='768', width='1366').place(x=0, y=0)
    l1 = Label(frame2, text='WELCOME', font=('arial', 40, 'bold'), bg='black', fg='white')
    l1.place(x=550, y=0)

    # Label(frame2, width='100', height='20', bg='gray').place(x=330, y=170)

    button2 = Button(frame2, text='DEBIT', width='20', bd=8, bg='black', fg='white', font=('arial', 15, 'bold'),
                     command=lambda: debit(frame2, root, accnt_no))
    button2.place(x=350, y=200)
    button3 = Button(frame2, text='CREDIT', width='20', bd=8, bg='black', fg='white', font=('arial', 15, 'bold'),
                     command=lambda: credit(frame2, root, accnt_no))
    button3.place(x=850, y=200)
    button4 = Button(frame2, text='CHECK BALANCE', bg='black', fg='white', width='20', bd=8, font=('arial', 15, 'bold'),
                     command=lambda: check_balance(frame2, root, accnt_no))
    button4.place(x=350, y=420)
    button5 = Button(frame2, text='EXIT', width='20', bd=8, bg='black', fg='white', font=('arial', 15, 'bold'),
                     command=lambda: iBacklogin(frame2))
    button5.place(x=850, y=420)

    frame2.mainloop()


def signup(frame1, root):
    frame1.destroy()
    frame3 = Frame(root, width='1366', height='768')
    frame3.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\onlinebanking.jpg'))
    Label(frame3, image=img, height='768', width='1366').place(x=0, y=0)
    l1 = Label(frame3, text='Sign up Page', font=('arial', 40, 'bold'), bg='black', fg='white')
    l1.place(x=550, y=0)

    name1 = StringVar()
    ph_no1 = StringVar()
    email1 = StringVar()
    address1 = StringVar()

    balance1 = StringVar()
    password1 = StringVar()

    Label(frame3, width='60', height='25', bg='grey').place(x=450, y=200)

    l1 = Label(frame3, text="Name : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=240)
    e1 = Entry(frame3, bd=5, width=30, text=name1).place(x=650, y=240)

    l2 = Label(frame3, text="E-Mail ID : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=290)
    e2 = Entry(frame3, bd=5, width=30, text=email1).place(x=650, y=290)

    l3 = Label(frame3, text="Phone No. : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=340)
    e3 = Entry(frame3, bd=5, width=30, text=ph_no1).place(x=650, y=340)

    l4 = Label(frame3, text="Initial Balance : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500,
                                                                                                            y=390)
    e4 = Entry(frame3, bd=5, width=30, text=balance1).place(x=650, y=390)

    l5 = Label(frame3, text="Address : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=440)
    e5 = Entry(frame3, bd=5, width=30, text=address1).place(x=650, y=440)
    l6 = Label(frame3, text="Password : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=490)
    e6 = Entry(frame3, bd=5, width=30, text=password1).place(x=650, y=490)

    b1 = Button(frame3, text='SIGNUP', bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: retrieve())
    b1.place(x=500, y=540)
    b2 = Button(frame3, text=' BACK ', bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: iBackSignup(frame3))
    b2.place(x=780, y=540)

    def retrieve():
        name = name1.get()
        email = email1.get()
        ph_no = ph_no1.get()
        balance = balance1.get()
        address = address1.get()
        password = password1.get()
        query = f'insert into details(name,ph_no,email,address,balance,password)values("{name}","{ph_no}","{email}","{address}","{balance}","{password}")'
        cursor.execute(query)
        query = f'commit'
        cursor.execute(query)

        query2 = f'select *from details'
        cursor.execute(query2)
        records = cursor.fetchall()
        q = tkinter.messagebox.showinfo("SIGNED IN", "Congratulation .You just signed in")

        for row in records:
            if row[1] == name and row[3] == email:
                asd = row[0]
        text_area = Text(frame3, width=20, height=20)
        text_area.insert(INSERT, ("your account number is: ", asd))
        text_area.place(x=1000, y=200)

    frame3.mainloop()


def debit(frame2, root, accnt_no):
    frame2.destroy()
    frame4 = Frame(root, width=1366, height=768, bg='blue')
    frame4.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\money.jpg'))
    Label(frame4, image=img, height='768', width='1366').place(x=0, y=0)
    l1 = Label(frame4, text='Welcome to Debit service', font=('arial', 40, 'bold'), bg='black', fg='white')
    l1.place(x=420, y=0)
    Label(frame4, width='80', height='15', bg='gray').place(x=450, y=200)

    amount1 = IntVar()
    amount1.set('')
    Label(frame4, text='Enter Debeting Amount :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=520,
                                                                                                            y=250)
    e1 = Entry(frame4, bd=3, width=30, text=amount1).place(x=780, y=250)

    b8 = Button(frame4, text="Proceed", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: debitfn(accnt_no))
    b8.place(x=600, y=330)
    b9 = Button(frame4, text="Back", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: iBackDebit(frame4, accnt_no))
    b9.place(x=800, y=330)

    def debitfn(accnt_no):
        amount = amount1.get()
        query4 = f'update details set balance=balance-"{amount}" where accnt_no={accnt_no}'
        cursor.execute(query4)
        query5 = f'commit'
        cursor.execute(query5)
        text_area = Text(frame4, width=70, height=10)
        text_area.insert(INSERT, ("your account has been debited with amount:-  ", amount))
        text_area.place(x=450, y=450)

    frame4.mainloop()


def credit(frame2, root, accnt_no):
    frame2.destroy()
    frame5 = Frame(root, width=1366, height=768, bg='red')
    frame5.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\saving.jpg'))
    Label(frame5, image=img, height='768', width='1366').place(x=0, y=0)
    l1 = Label(frame5, text='Welcome to Credit service', font=('arial', 40, 'bold'), bg='black', fg='white')
    l1.place(x=420, y=0)
    # Label(frame5, width='80', height='15', bg='gray').place(x=450, y=200)
    amount1 = IntVar()
    amount1.set('')
    Label(frame5, text='Enter Credeting Amount :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=520,
                                                                                                             y=250)
    e1 = Entry(frame5, bd=3, width=30, text=amount1).place(x=780, y=250)

    b8 = Button(frame5, text="Proceed", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: creditfn(accnt_no))
    b8.place(x=600, y=330)
    b9 = Button(frame5, text="Back", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: iBackCredit(frame5, accnt_no))
    b9.place(x=800, y=330)

    def creditfn(accnt_no):
        amount = amount1.get()
        query5 = f'update details set balance=balance +"{amount}" where accnt_no={accnt_no}'
        cursor.execute(query5)
        query6 = f'commit'
        cursor.execute(query6)
        text_area = Text(frame5, width=70, height=10)
        text_area.insert(INSERT, ("your account has been Credited with amount:-  ", amount))
        text_area.place(x=450, y=450)

    frame5.mainloop()


def check_balance(frame2, root, accnt_no):
    frame2.destroy()
    frame6 = Frame(root, width=1366, height=768, bg='green')
    frame6.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\counting.jpg'))
    Label(frame6, image=img, height='768', width='1366').place(x=0, y=0)
    Label(frame6, width='80', height='8', bg='gray').place(x=360, y=220)
    accnt1 = IntVar()
    accnt1.set('')
    Label(frame6, text='Enter Account number :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400, y=250)
    e1 = Entry(frame6, bd=3, width=30, text=accnt1).place(x=700, y=250)
    a = Button(frame6, text="Proceed", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
               command=lambda: check_fn())
    a.place(x=400, y=300)
    b = Button(frame6, text="Back", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
               command=lambda: iBackCheck(frame6, accnt_no))
    b.place(x=850, y=300)

    def check_fn():
        accnt_no = accnt1.get()
        query6 = f'select accnt_no,balance from details'
        cursor.execute(query6)
        records = cursor.fetchall()
        dict = {}
        for a, b in records:
            dict[a] = b
        if accnt_no in dict.keys():
            text_area = Text(frame6, width=70, height=10)
            text_area.insert(INSERT, ("your account Balance is :-  ", dict[accnt_no]))
            text_area.place(x=450, y=450)
            # text_area.after(self,5,self.destroy())

        else:
            q = tkinter.messagebox.showerror("ERROR", "wrong account number or password")
            # reset(frame1, root)

        """for row in records:
            if row[0] == accnt_no:
                text_area = Text(frame6, width=70, height=10)
                text_area.insert(INSERT, ("your account Balance is :-  ", row[5]))
                text_area.place(x=450, y=450)
                #text_area.after(self,5,self.destroy())
                exit()
            else:
                q = tkinter.messagebox.showerror("ERROR", "wrong account number!!!")
                if q:
        """  # return reset(frame6, root)

    frame6.mainloop()


def forget_password(frame1, root):
    frame1.destroy()
    frame7 = Frame(root, width=1366, height=768, bg="cyan")
    frame7.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\password.jpg'))
    Label(frame7, image=img, width="1366", height="768").place(x=0, y=0)

    accnt1 = IntVar()
    accnt1.set('')
    email1 = StringVar()
    new_potp = StringVar()

    Label(frame7, text='Enter Account number :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400, y=250)
    e1 = Entry(frame7, bd=3, width=30, text=accnt1).place(x=700, y=250)

    Label(frame7, text='Enter Associated Email :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400,
                                                                                                             y=300)
    e1 = Entry(frame7, bd=3, width=30, text=email1).place(x=700, y=300)

    b8 = Button(frame7, text="Proceed", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: changepas())
    b8.place(x=500, y=400)
    b9 = Button(frame7, text="Back", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: iBackpass(frame7))
    b9.place(x=800, y=400)

    def changepas():
        accnt_no = accnt1.get()
        email = email1.get()
        """query2 = 'select accnt_no,password from details'
        cursor.execute(query2)
        records = cursor.fetchall()
        dict = {}
        for a, b in records:
            dict[a] = b
        """
        dict = {}
        query3 = f'select accnt_no,email from details'
        cursor.execute(query3)
        records = cursor.fetchall()
        for a, b in records:
            dict[a] = b

        if accnt_no in dict.keys():
            # call here the mail function
            new_potp = mail(accnt_no, email)
            # otp = input('enter your otp')
            otp_veri(frame7, root, accnt_no, new_potp)

            # if otp == new_potp:
            # new_password = input('enter new password')
            # data[ac]['password']=new_password

        else:
            q = tkinter.messagebox.showerror("ERROR", "wrong account number or Email")
            # reset(frame1, root)

    frame7.mainloop()


def otp_veri(frame7, root, accnt_no, new_potp):
    frame7.destroy()
    frame8 = Frame(root, width=1366, height=768, bg="cyan")
    frame8.pack()
    img = ImageTk.PhotoImage(Image.open('password.jpg'))
    Label(frame8, image=img, width="1366", height="768").place(x=0, y=0)

    newotp1 = StringVar()
    Label(frame8, text='Enter Received OTP :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400, y=250)
    e1 = Entry(frame8, bd=3, width=30, text=newotp1).place(x=700, y=250)

    b8 = Button(frame8, text="CONFIRM", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: confirm(accnt_no, new_potp))
    b8.place(x=500, y=400)

    def confirm(accnt_no, new_potp):
        otp1 = newotp1.get()
        if otp1 == new_potp:
            new_pas(frame8, root, accnt_no)
        else:
            q = tkinter.messagebox.showerror("ERROR", "OTP's do not match ")

    frame8.mainloop()


def new_pas(frame8, root, accnt_no):
    frame8.destroy()
    frame9 = Frame(root, width=1366, height=768, bg="cyan")
    frame9.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\password.jpg'))
    Label(frame9, image=img, width="1366", height="768").place(x=0, y=0)

    newpas1 = StringVar()
    conpas1 = StringVar()
    Label(frame9, text='Enter New Password :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400, y=250)
    e1 = Entry(frame9, bd=3, width=30, text=newpas1).place(x=700, y=250)

    Label(frame9, text='Confirm Password :', fg='white', bg='black', font=('arial', 15, 'bold')).place(x=400, y=300)
    e1 = Entry(frame9, bd=3, width=30, text=conpas1).place(x=700, y=300)

    b8 = Button(frame9, text="Proceed", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: new_pasfn(accnt_no))
    b8.place(x=500, y=400)

    b9 = Button(frame9, text="Back", bd=8, bg='black', fg='white', font=('arial', 10, 'bold'), command=lambda: home())
    b9.place(x=800, y=400)

    def new_pasfn(accnt_no):
        newpas = newpas1.get()
        conpas = conpas1.get()
        if newpas == conpas:
            query7 = f'update details set password="{newpas}" where accnt_no={accnt_no}'
            cursor.execute(query7)
            query8 = f'commit'
            cursor.execute(query8)
            q = tkinter.messagebox.showinfo("CONGRATS", "Password has been Updated ")

        else:
            q = tkinter.messagebox.showerror("ERROR", "Passwords do not match ")

    frame9.mainloop()


def mail(accnt_no, email):
    import smtplib  # lib for sending mail (simple mail transfer protocol
    # first we make a connection
    connection = smtplib.SMTP('smtp.gmail.com', 587)  # port no for gmail if using tls is 587
    # for running a connection
    connection.ehlo()
    # for startiing a connection
    connection.starttls()
    # first we login into gmail
    # p=getpass('enter password of your mail id')
    connection.login('as9728648@gmail.com', 'akshay0697')
    # create a string for the otp passing
    # otp=OTP()
    potp = otp()
    # for sending message
    connection.sendmail('as9728648@gmail.com', email, f'Subject:OTP TO RESET PASSWORD IS:\n\n{potp}')
    # pass variable in place of message for passing otp to them
    return potp


def otp():
    import string
    import random
    pas = string.ascii_letters + string.digits
    random_password = ''
    for var in range(6):
        random_password = random_password + random.choice(pas)
    return random_password


def iExit(root):
    qExit = tkinter.messagebox.askyesno("Quit system", "Do you want to quit?")
    if qExit:
        root.destroy()
        return


def iBacklogin(frame2):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back to home?")
    if qBack:
        frame2.destroy()
        return home()


def iBackSignup(frame3):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back to home?")
    if qBack:
        frame3.destroy()
        return home()


def iBackDebit(frame4, accnt_no):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back ?")
    if qBack:
        frame4.destroy()
        return login(frame4, root, accnt_no)


def iBackCredit(frame5, accnt_no):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back ?")
    if qBack:
        frame5.destroy()
        return login(frame5, root, accnt_no)


def iBackCheck(frame6, accnt_no):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back ?")
    if qBack:
        frame6.destroy()
        return login(frame6, root, accnt_no)


def iBackpass(frame7):
    qBack = tkinter.messagebox.askyesno("Back system", "Do you want to go back to home?")
    if qBack:
        frame7.destroy()
        return home()


home()


