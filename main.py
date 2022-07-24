import datetime
import mysql.connector as sqlctr
from tkinter import *

root = Tk()
root.title("Shyam Computer Academy")
# functions


def connect_server():
    ps = e1.get()
    tmp = 0
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=ps
        )
        Label(root, text="Login Sucessful !!!", bg="black", fg="green").grid()
    except:
        Label(root, text="Incorrect Password Entered !!!",
              bg="black", fg="red").grid()
        tmp = 1
    # CODE STARTS FROM HERE----
    if tmp != 1:
        # functions
        def connect_database():
            ps = e1.get()
            connection = None
            try:
                connection = sqlctr.connect(
                    host="localhost",
                    user="root",
                    password=ps,
                    database="SCA_DB"
                )
            except:
                pass
            return connection

        def execute_query(connection, query):
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

        def read_query(connection, query):
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        def connect_server1():
            ps = e1.get()
            tmp = 0
            connection = None
            try:
                connection = sqlctr.connect(
                    host="localhost",
                    user="root",
                    password=ps
                )
            except:
                pass
            return connection
        q1 = f"""create database if not exists SCA_DB;"""
        cs = connect_server1()
        eq = execute_query(cs, q1)
        options = Tk()
        options.title("SCA")
        options.geometry("900x400")
        options.maxsize(900, 400)
        options.minsize(900, 400)
        label = Label(options, text="SHYAM COMPUTER ACADEMY\nClick On Any Button To Proceed.",
                      bg="blue", fg="yellow", font="bold")
        label.grid(row=0)
        btn1 = Button(
            options, text="For Storing Student & Fee in Server", command=lambda: func(1), padx=50, pady=5)
        btn2 = Button(options, text="To Check Fee Status",
                      command=lambda: func(2), padx=50, pady=5)
        btn3 = Button(options, text="For Updating Details",
                      command=lambda: func(3), padx=50, pady=5)
        btn4 = Button(options, text="For Deleting Details",
                      command=lambda: func(4), padx=50, pady=5)
        btn5 = Button(options, text="For Check All Data in Server",
                      command=lambda: func(5), padx=50, pady=5)
        btn1.grid(row=1, column=1)
        btn2.grid(row=2, column=1)
        btn3.grid(row=3, column=1)
        btn4.grid(row=4, column=1)
        btn5.grid(row=5, column=1)
        # Connecting Database
        cd = connect_database()

        def func(n):
            d = 0
            d += n

            # if else Ladder and new window
            if d == 1:  # tested OK
                Label(options, text="Opening  Storing Student & Fee in Server  Window!",
                      bg="black", fg="green").grid()
                w1 = Tk()
                w1.title("SCA | Storing Fee details.")
                w1.geometry("900x400")
                w1.maxsize(900, 400)
                w1.minsize(900, 400)
                # CODE FROM HERE
                ct = f"""
                    create table if not exists stud_details(
                    admn_no int,
                    student_name varchar(30) not null,
                    class varchar(3) not null,
                    course varchar(55) not null,
                    fee_paid float(50),
                    date varchar(50));"""
                execute_query(cd, ct)
                # labels
                name = Label(w1, text="Enter Students's Name : ")
                admn_no = Label(
                    w1, text="Enter Students's Admission Number : ")
                cls = Label(w1, text="Enter Students's Class : ")
                course = Label(w1, text="Enter Cource opted By Student : ")
                f_paid = Label(w1, text="Enter Fee Paid By Student : ")
                name.grid()
                admn_no.grid()
                cls.grid()
                course.grid()
                f_paid.grid()
                # variables
                name = StringVar()
                admn_no = StringVar()
                cls = StringVar()
                course = StringVar()
                f_paid = StringVar()
                # text fields
                name1 = Entry(w1, textvariable=name)
                admn_no1 = Entry(w1, textvariable=admn_no)
                cls1 = Entry(w1, textvariable=cls)
                course1 = Entry(w1, textvariable=course)
                f_paid1 = Entry(w1, textvariable=f_paid)
                name1.grid(row=0, column=1)
                admn_no1.grid(row=1, column=1)
                cls1.grid(row=2, column=1)
                course1.grid(row=3, column=1)
                f_paid1.grid(row=4, column=1)

                def store():
                    try:
                        n = (name1.get()).capitalize()
                        a = int(admn_no1.get())
                        c = (cls1.get()).capitalize()
                        co = (course1.get()).capitalize()
                        f = float(f_paid1.get())
                    except:
                        Label(w1, text="Invalid Syntax !!!",
                              bg="black", fg="red").grid()
                    try:
                        q1 = "use sca_db;"
                        x = datetime.datetime.now()
                        q2 = f"""insert into stud_details values({a},"{n}","{c}","{co}",{f},"{x}");"""
                        execute_query(cd, q1)
                        execute_query(cd, q2)
                        Label(w1, text="Entry Sucessfull !!!",
                              bg="black", fg="green").grid()
                    except:
                        Label(w1, text="An Unexpected Error Occured ..Please Try Again...",
                              bg="black", fg="red").grid()
                Button(w1, text="Submit", command=store,
                       bg="green", fg="white").grid(row=5, column=1)
                w1.mainloop()
            elif d == 2:  # tested OK
                Label(options, text="Opening Check Fee Status Window!",
                      bg="black", fg="green").grid()
                w2 = Tk()
                w2.title("SCA | Check Fee Status.")
                w2.geometry("900x400")
                w2.maxsize(900, 400)
                w2.minsize(900, 400)
                # labels
                name = Label(w2, text="Enter Students's Name : ")
                admn_no = Label(
                    w2, text="Enter Students's Admission Number : ")
                course = Label(w2, text="Enter Course opted By Student : ")
                name.grid()
                admn_no.grid()
                course.grid()
                # variables
                name = StringVar()
                admn_no = StringVar()
                course = StringVar()
                # textfields
                name1 = Entry(w2, textvariable=name)
                admn_no1 = Entry(w2, textvariable=admn_no)
                course1 = Entry(w2, textvariable=course)
                name1.grid(row=0, column=1)
                admn_no1.grid(row=1, column=1)
                course1.grid(row=2, column=1)

                def get():
                    q1 = "use sca_db"
                    q2 = f"""select fee_paid from stud_details where student_name ="{(name1.get()).capitalize()}";"""
                    execute_query(cd, q1)
                    k = read_query(cd, q2)
                    # Fee Structures:
                    if course1.get() == "Python":
                        tf = 10000
                    elif course1.get() == "Java":
                        tf = 10000
                    elif course1.get() == "C++":
                        tf = 9000
                    elif course1.get() == "C":
                        tf = 9000
                    else:
                        tf = None
                    try:
                        if k[0][0] == tf:
                            Label(w2, text="Total Fee Paid...",
                                  bg="black", fg="green", font="bold").grid()
                        else:
                            s = 0
                            for i in k:
                                s += k[0][0]
                            s = tf-s
                            Label(
                                w2, text=f"""Remaining Fee To be Paid By {name1.get().capitalize()} is ₹{s}""", bg="black", fg="green", font="bold").grid()
                    except:
                        pass
                Button(w2, text="Submit", command=get, bg="green",
                       fg="white").grid(row=3, column=1)
                w2.mainloop()
            elif d == 3:  # tested ok
                Label(options, text="Opening  Updating Details Window!",
                      bg="black", fg="green").grid()
                w3 = Tk()
                w3.title("SCA | Updating details.")
                w3.geometry("900x400")
                w3.maxsize(900, 400)
                w3.minsize(900, 400)
                # labels
                name = Label(w3, text="Enter Students's Name : ")
                admn_no = Label(
                    w3, text="Enter Students's Admission Number : ")
                n_name = Label(w3, text="Enter New Name : ")
                name.grid(row=0, column=0)
                admn_no.grid(row=1, column=0)
                n_name.grid(row=2, column=0)
                # variables
                name = StringVar()
                admn_no = StringVar()
                n_name = StringVar()
                # textfields
                name1 = Entry(w3, textvariable=name)
                admn_no1 = Entry(w3, textvariable=admn_no)
                n_name1 = Entry(w3, textvariable=n_name)
                name1.grid(row=0, column=1)
                admn_no1.grid(row=1, column=1)
                n_name1.grid(row=2, column=1)

                def update():
                    try:
                        a = int(admn_no1.get())
                        q1 = """use sca_db;"""
                        q2 = f"""update stud_details set student_name="{(n_name1.get()).capitalize()}" where student_name="{(name1.get()).capitalize()}" || admn_no={a};"""
                        execute_query(cd, q1)
                        execute_query(cd, q2)
                        Label(w3, text="Updated Sucessfully !!!",
                              bg="black", fg="green").grid(row=5, column=0)
                    except:
                        Label(w3, text="Something Went Wrong Please Try Again !!!",
                              bg="black", fg="red").grid(row=5, column=0)
                Button(w3, text="Submit", command=update,
                       bg="green", fg="white").grid(row=4, column=1)
                w3.mainloop()
            elif d == 4:  # tested OK
                Label(options, text="Opening  Deleting Details Window!",
                      bg="black", fg="green").grid()
                w4 = Tk()
                w4.title("SCA | Deleting details.")
                w4.geometry("900x400")
                w4.maxsize(900, 400)
                w4.minsize(900, 400)
                # labels
                name = Label(w4, text="Enter Students's Name : ")
                admn_no = Label(
                    w4, text="Enter Students's Admission Number : ")
                name.grid(row=0, column=0)
                admn_no.grid(row=1, column=0)
                # variables
                name = StringVar()
                admn_no = StringVar()
                # textfields
                name1 = Entry(w4, textvariable=name)
                admn_no1 = Entry(w4, textvariable=admn_no)
                name1.grid(row=0, column=1)
                admn_no1.grid(row=1, column=1)

                def delete():
                    try:
                        a = int(admn_no1.get())
                        q1 = """use sca_db;"""
                        q2 = f"""delete from stud_details where student_name="{(name1.get()).capitalize()}" && admn_no={a};"""
                        execute_query(cd, q1)
                        execute_query(cd, q2)
                        Label(w4, text="Deleted Sucessfully !!!",
                              bg="black", fg="green").grid(row=4, column=0)
                    except:
                        Label(w4, text="Something Went Wrong Please Try Again !!!",
                              bg="black", fg="red").grid(row=4, column=0)
                Button(w4, text="Submit", command=delete,
                       bg="green", fg="white").grid(row=3, column=1)
                w4.mainloop()
            elif d == 5:  # tested OK
                Label(options, text="Opening  Check All Data in Server Window!",
                      bg="black", fg="green").grid()
                w5 = Tk()
                w5.title("SCA | Check All Data in Server.")
                w5.geometry("900x400")
                w5.maxsize(900, 400)
                w5.minsize(900, 400)
                # labels
                name = Label(w5, text="Enter Students's Name : ")
                admn_no = Label(
                    w5, text="Enter Students's Admission Number : ")
                name.grid(row=0, column=0)
                admn_no.grid(row=1, column=0)
                # variables
                name = StringVar()
                admn_no = StringVar()
                # textfields
                name1 = Entry(w5, textvariable=name)
                admn_no1 = Entry(w5, textvariable=admn_no)
                name1.grid(row=0, column=1)
                admn_no1.grid(row=1, column=1)

                def read():
                    try:
                        q1 = "use sca_db;"
                        q2 = f"""select * from stud_details where student_name="{(name1.get()).capitalize()}" && admn_no={admn_no1.get()};"""
                        execute_query(cd, q1)
                        k = read_query(cd, q2)
                        j = 0
                        for i in k:
                            l = Label(
                                w5, text=f"{k[j]}", bg="black", fg="white", font="bold")
                            l.grid()
                            j += 1

                    except:
                        Label(w5, text="Something Went Wrong Please Try Again",
                              bg="black", fg="red").grid(row=3, column=0)
                Button(w5, text="Submit", command=read, bg="green",
                       fg="white").grid(row=2, column=1)
                w5.mainloop()
        options.mainloop()

    return connection


root.geometry("900x400")
root.maxsize(900, 400)
root.minsize(900, 400)
bg = PhotoImage(file="bg.png")
labelI = Label(root, image=bg)
labelI.place(x=0, y=0)
photo = PhotoImage(file = "bg.png")
root.iconphoto(False, photo)
label = Label(root, text="SHYAM COMPUTER ACADEMY",bg="blue", fg="yellow", font="bold")
label.grid()
pw = Label(root, text="Enter Server Password : ")
pw.grid(row=1)
pw = StringVar()
e1 = Entry(root, textvariable=pw)
e1.grid(row=1, column=2)
Button(text="Submit", command=connect_server,
       bg="green", fg="white").grid(row=2, column=2)
root.mainloop()
