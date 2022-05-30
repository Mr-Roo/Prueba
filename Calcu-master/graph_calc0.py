#from tkinter import *
import Pmw
import string
from math import *
import numpy as np

Calculadora = Pmw.initialise(fontScheme = 'pmw1')
#Calculadora = Tk()
Calculadora.title("GRAPH_CALC")
Calculadora.config(bg='gray40')
formula = ""
result = ""
mem = ""
ndact = False
type_op = "MATH"

def push(car):
    global formula
    formula=formula+car
    #print(formula)
    display.appendtext(car)

def typer(m):
    global type_op
    type_op = m
    print(type_op)
    clear()
    #display.appendtext(type_op+"\n")

def del_():
    global mem
    if mem!="":
        mem=""
    
def clear():
    global formula, mem, result
    formula = ""
    mem = ""
    result = ""
    display.clear()

def store():
    global mem
    if mem=="" and result!="" and result!="ERROR":
        mem = str(result)
        #display.appendtext("STORED: "+mem+"\n\n")
    else:
        push(mem)
    
def matr_demo():
    a1 = np.array([[1,2,3],[1,2,8]], float)
    a2 = np.array([[4,5,6],[2,3,4]], float)
    display.appendtext(a1+a2)

def change_sign():
    global result
    if result!="ERROR" and result!="":
        result = eval(str(result)+"*(-1)")
        text = '{:^29}'.format(str(result))
        display.appendtext((text)+"\n")

def nd():
    global ndact
    if ndact == False:
        ndact = True

def pi():
    if ndact == True:
        #numb = pi
        #display.appendtext(pi)
        push('3.141592653589793')
        
def operation():
    global formula, result
    print(formula)
    if type_op=="MATH" and formula!="":
        try:
            result = eval(formula)
        except:
            result = "ERROR"
        text = '{:^30}'.format(str(result))
        display.appendtext("\n"+text+"\n\n")
        formula=""

#PANTALLA
display = Pmw.ScrolledText(Calculadora, hscrollmode='none',#dynamic
                      vscrollmode='dynamic', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=29, #ancho pantalla #29
                      text_foreground='black', text_height=9,#alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Arial', 12, 'bold') )
display.pack(padx=0,pady=0)

buttons1 = Pmw.ButtonBox(Calculadora,
                         hull_background='gray40')

buttons1.pack(fill='both', expand=1, padx=1, pady=1)
#buttons1.alignbuttons()

buttons1.add('2nd',width=5,bg='steelblue3',fg='white',command=nd)
buttons1.add('Mode',bg='gray30',fg='white')
buttons1.add('Del',bg='gray30',fg='white',command=del_)
buttons1.add('Alpha',bg='gray50',fg='white')
buttons1.add('Stat',bg='gray30',fg='white')
    
buttons2 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons2.pack(fill='both', expand=1, padx=1, pady=1)
#buttons2.alignbuttons()
buttons2.add('Math',width=5,fg='white',bg='gray30',command=lambda:typer("MATH"))#,command=lambda:typer("MATH")
buttons2.add("Mtrx",fg='white',bg='gray30',command=lambda:typer("MTRX"))#
buttons2.add("Pgrm",fg='white',bg='gray30')
buttons2.add("Vars",fg='white',bg='gray30')
buttons2.add("Clr",fg='white',bg='gray30')

buttons3 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons3.pack(fill='both', expand=1, padx=1, pady=1)
buttons3.add('X-1',width=5,fg='white',bg='gray30')
buttons3.add("Sin",fg='white',bg='gray30',command=lambda:push("sin("))
buttons3.add("Cos",fg='white',bg='gray30',command=lambda:push("cos("))
buttons3.add("Tan",fg='white',bg='gray30',command=lambda:push("tan("))
buttons3.add("^ π",fg='white',bg='gray30',command=pi)

buttons4 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons4.pack(fill='both', expand=1, padx=1, pady=1)
buttons4.add('X2',width=5,fg='white',bg='gray30')
buttons4.add(",",fg='white',bg='gray30',command=lambda:push(","))
buttons4.add("(",fg='white',bg='gray30',command=lambda:push("("))
buttons4.add(")",fg='white',bg='gray30',command=lambda:push(")"))
buttons4.add("/",bg='steelblue3',fg='white',command=lambda:push("/"))

buttons5 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons5.pack(fill='both', expand=1, padx=1, pady=1)
buttons5.add('Log',width=5,bg='gray30',fg='white',command=lambda:push("log("))
buttons5.add("7",bg='gray50',fg='white',command=lambda:push("7"))
buttons5.add("8",bg='gray50',fg='white',command=lambda:push("8"))
buttons5.add("9",bg='gray50',fg='white',command=lambda:push("9"))
buttons5.add("x",bg='steelblue3',fg='white',command=lambda:push("*"))

buttons6 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons6.pack(fill='both', expand=1, padx=1, pady=1)
buttons6.add('Ln',width=5,bg='gray30',fg='white')
buttons6.add("4",bg='gray50',fg='white',command=lambda:push("4"))
buttons6.add("5",bg='gray50',fg='white',command=lambda:push("5"))
buttons6.add("6",bg='gray50',fg='white',command=lambda:push("6"))
buttons6.add("-",bg='steelblue3',fg='white',command=lambda:push("-"))

buttons7 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons7.pack(fill='both', expand=1, padx=1, pady=1)
buttons7.add('STO',width=5,bg='gray30',fg='white',command=store)
buttons7.add("1",bg='gray50',fg='white',command=lambda:push("1"))
buttons7.add("2",bg='gray50',fg='white',command=lambda:push("2"))
buttons7.add("3",bg='gray50',fg='white',command=lambda:push("3"))
buttons7.add("+",bg='steelblue3',fg='white',command=lambda:push("+"))

buttons8 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons8.pack(fill='both', expand=1, padx=1, pady=1)
buttons8.add('Off',width=5,bg='gray30',fg='white',command=clear)
buttons8.add("0",bg='gray50',fg='white',command=lambda:push("0"))
buttons8.add(".",bg='gray50',fg='white',command=lambda:push("."))
buttons8.add("(-)",bg='gray50',fg='white',command=change_sign)
buttons8.add("Enter",bg='steelblue3',fg='white',command=operation)

bts = (buttons1,buttons2,buttons3,buttons4,buttons5,buttons6,
       buttons7,buttons8)
for i in bts:
    i.alignbuttons()


Calculadora.mainloop()
