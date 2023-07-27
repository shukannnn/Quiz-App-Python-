import sqlite3
from statistics import mode
import tkinter as Tk
from tkinter import *

from question_model import Question
from quiz_brain import QuizBrain
from quiz_interface import QuizInterface
from random import shuffle
import html
import requests


fo=open("data.txt","a+")

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width = 1420,height = 730,bg="#b392ac")
    login_canvas.pack()
 
    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
 
    heading = Label(login_frame,text="Quiz App Login",fg="#735d78",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)
 
    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='#735d78',bg='white')
    ulabel.config(font=('calibri 20'))
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)
 
    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='#735d78',bg='white')
    plabel.config(font=('calibri 20'))
    plabel.place(relx=0.21,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)
 
    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                fo.write(b)
                fo.write("\n")
                menu()
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='#735d78',bg='white')
            error.config(font=('calibri 20'))
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=2, activebackground = "grey", relief = FLAT, bg="grey",fg='#735d78')
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()    
 
def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width = 1420,height = 730,bg="#b392ac")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
 
    heading = Label(sup_frame,text="Quiz App SignUp",fg="#735d78",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)
 
    #full name
    flabel = Label(sup_frame,text="Full Name",fg='#735d78',bg='white',)
    flabel.config(font=('calibri 20'))
    flabel.place(relx=0.21,rely=0.3)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.3)
 
    #username
    ulabel = Label(sup_frame,text="Username",fg='#735d78',bg='white')
    ulabel.config(font=('calibri 20'))
    ulabel.place(relx=0.21,rely=0.4)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.4)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='#735d78',bg='white')
    plabel.config(font=('calibri 20'))
    plabel.place(relx=0.21,rely=0.5)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='#735d78',bg='white')
    clabel.config(font=('calibri 20'))
    clabel.place(relx=0.21,rely=0.6)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.6)
    
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text PRIMARY KEY,PASSWORD text,COUNTRY text)')
        try:
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            conn.close()
            loginPage(z)
        except sqlite3.IntegrityError:
            alert=Label(sup_frame,text="Username already exist",fg='red',bg='white')
            alert.place(relx=0.4,rely=0.9)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,fg='#735d78')
    sp.configure(width =15,height=2, activebackground = "#33B5E5", relief = RAISED)
    sp.place(relx=0.4,rely=0.7)
 
    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='#735d78')
    log.configure(width =15,height=2, activebackground = "#33B5E5", relief = RAISED)
    log.place(relx=0.4,rely=0.8)
 
    sup.mainloop()

def menu():
    login.destroy()
    global menu
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width = 1420,height = 730,bg="#f7d1cd")
    menu_canvas.grid()
 
    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
 
    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#735d78")
    wel.config(font=('Broadway 40'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="white",font="calibri 30",fg="#735d78")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Easy',fg="#735d78",bg="white",font="calibri 20",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Medium',fg="#735d78",bg="white",font="calibri 20",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Hard',fg="#735d78",bg="white",font="calibri 20",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    def navigate():
        x = var.get()
        question_bank = []
        print(x)
        if x == 1:
            menu.destroy()
            response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple")
            question_data = response.json()["results"]
            for question in question_data:
                choices = []
                question_text = html.unescape(question["question"])
                correct_answer = html.unescape(question["correct_answer"])
                incorrect_answers = question["incorrect_answers"]
                for ans in incorrect_answers:
                    choices.append(html.unescape(ans))
                choices.append(correct_answer)
                shuffle(choices)
                new_question = Question(question_text, correct_answer, choices)
                question_bank.append(new_question)
        elif x == 2:
            menu.destroy()
            response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple")
            question_data = response.json()["results"]
            for question in question_data:
                choices = []
                question_text = html.unescape(question["question"])
                correct_answer = html.unescape(question["correct_answer"])
                incorrect_answers = question["incorrect_answers"]
                for ans in incorrect_answers:
                    choices.append(html.unescape(ans))
                choices.append(correct_answer)
                shuffle(choices)
                new_question = Question(question_text, correct_answer, choices)
                question_bank.append(new_question)
            
        elif x == 3:
            menu.destroy()
            response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=hard&type=multiple")
            question_data = response.json()["results"]
            for question in question_data:
                choices = []
                question_text = html.unescape(question["question"])
                correct_answer = html.unescape(question["correct_answer"])
                incorrect_answers = question["incorrect_answers"]
                for ans in incorrect_answers:
                    choices.append(html.unescape(ans))
                choices.append(correct_answer)
                shuffle(choices)
                new_question = Question(question_text, correct_answer, choices)
                question_bank.append(new_question)
        else:
            pass
        
        quiz = QuizBrain(question_bank)
        quiz_ui = QuizInterface(quiz)

        
        
    letsgo = Button(menu_frame,text="Let's Go",bg="#735d78",fg="#735d78",font="calibri 20",command=navigate,height=1,width=6)
    letsgo.place(relx=0.25,rely=0.7)

    menu.mainloop()
    
def start():
    global root
    root = Tk()
    canvas = Canvas(root,width = 1420,height = 730)
    canvas.grid(column = 0 , row = 1)
    button = Button(root, text='Click here to start the quiz',command = signUpPage)
    button.configure(width = 102,height=3, activebackground = "black", bg ='white', relief = RAISED)
    button.grid(column = 0 , row = 2)
 
    root.mainloop()

start()






