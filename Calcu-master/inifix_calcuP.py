#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA")
ventana.configure(background="gray36")
ventana.geometry("366x450")#490
numeroPantalla=StringVar()
from math import *
act_parent=False
resul_parent=0
signu=""
primr_parent=True

def numeroPulsado(n):
    global numero
    global exc
    if exc==True:
        clear()
        exc=False
    numero=numero+n
    numeroPantalla.set(numero)

def onediv():
    global numero
    global resultado
    global exc
    try:
        if abs(float(numeroPantalla.get()))==abs(float(numero)):
            numero=1/(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=1/float(resultado)
            numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")
    exc=True

def abrir_parent():
    global act_parent
    global signu
    if act_parent==False:
        act_parent=True
        signu=op

def cierra_parent():
    global act_parent
    print(resultado)
    print(resul_parent)

def opera_calculo(operador):
    global resultado
    global resul_parent
    if operador=="+":
        if act_parent==True:
            resul_parent=resul_parent+float(numero)
        else:
            resultado=resultado+float(numero)######
    elif operador=="-":
        if act_parent==True:
            resul_parent=resul_parent-float(numero)
        else:
            resultado=resultado-float(numero)######
    elif operador=="*":
        if act_parent==True:
            resul_parent=resul_parent*float(numero)
        else:
            resultado=resultado*float(numero)######
    elif operador=="/":
        if act_parent==True:
            resul_parent=resul_parent/float(numero)
        else:
            resultado=resultado/float(numero)######
    elif operador=="**":
        if act_parent==True:
            resul_parent=resul_parent**float(numero)
        else:
            resultado=resultado**float(numero)######
    elif operador=="%":
        if act_parent==True:
            resul_parent=resul_parent%float(numero)
        else:
            resultado=resultado%float(numero)
    elif operador=="log":
        if act_parent==True:
            resul_parent=log(resul_parent)/log(float(numero))
        else:
            resultado=log(resultado)/log(float(numero))
    print(resul_parent)

def loga():
    global numero
    global resultado
    global exc
    if primr==True:
        if numero=="":
            numero=0
    try:
        if numero!="":
            if abs(float(numeroPantalla.get()))==abs(float(numero)):
                numero=log(float(numero))
                numeroPantalla.set(numero)
            else:
                resultado=log(float(resultado))
                numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")


def rounde():
    global numero
    global resultado
    try:
        if abs(float(numeroPantalla.get()))==abs(float(numero)):
            numero=round(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=round(float(resultado))
            numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")
    

def funcis(f):
    global numero
    global resultado
    global exc
    global prev_func
    if primr==True:
        if numero=="":
            numero=0
    if numero!="" and numeroPantalla.get()!="ERROR":
        li=["sin","cos","tan"]
        if exc==False or prev_func in li:
            if abs(float(numeroPantalla.get()))==abs(float(numero)):
                numero=eval(f+"("+str(numero)+")")
                numeroPantalla.set(numero)
            else:
                resultado=eval(f+"("+str(resultado)+")")
                numeroPantalla.set(resultado)
        prev_func=f
        exc=True

def comas():
    global numero
    if numero!="" and not "." in numero and exc==False:
        numero=numero+"."
        numeroPantalla.set(numero)

def clear_error():
    global numero
    numero=""
    numeroPantalla.set("0")

def cambio_signo():
    global numero
    global resultado
    print(numero)
    print(resultado)
    try:
        if numero!="" and abs(float(numeroPantalla.get()))==abs(float(numero)):
            if float(numero)!=0:
                numero=float(numero)*(-1)
                numeroPantalla.set(numero)
        else:
            if resultado!=0:
                resultado=resultado*(-1)
                numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")

def raiz_cuadrada():
    global numero
    global resultado
    global exc
    try:
        if numero!="" and abs(float(numeroPantalla.get()))==abs(float(numero)):############
            numero=sqrt(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=sqrt(resultado)
            numeroPantalla.set(resultado)
    except:
        clear()#N
        numeroPantalla.set("ERROR")
    exc=True
        
def pee():
    global numero
    global exc
    if exc==True:
        clear()
    numero=pi
    numeroPantalla.set(numero)
    #exc=True

def calculo(o):
    global resultado
    global numero
    global primr
    global prev_sign
    global operacion
    global op
    global exc
    global primr_parent
    global resul_parent
    op=o
    if act_parent==True and primr_parent==True:
        if numero=="":
            numero=0
        resul_parent=float(numero)
        prev_sign=o
        numero=""
        primr_parent=False
        primr=False
    if primr==True:
        if numero=="":
            numero=0
        resultado=float(numero)
        prev_sign=o
        numero=""
        primr=False
    else:
        try:
            if o==prev_sign and numero!="" and exc==False:
                opera_calculo(o)
            elif o!=prev_sign and numero!="" and exc==False:
                opera_calculo(prev_sign)
                prev_sign=o
            numeroPantalla.set(resultado)
            #operacion=o
        except:
            clear()#N
            numeroPantalla.set("ERROR")
            resultado=0
            primr=True
    
        numero=""
    exc=False

def clear():
    global numero
    global resultado
    global primr
    global prev_sign
    global operacion
    global op
    global exc
    global prev_func
    op=""
    numero=""
    resultado=0
    primr=True
    prev_sign=""
    operacion=""
    exc=False
    prev_func="sin"
    numeroPantalla.set(resultado)

def result():
    global numero
    global resultado
    global prev_sign
    global operacion
    global primr
    global exc
    if primr==True:
        resultado=float(numeroPantalla.get())#########################
        primr=False###################################################
    try:
        operacion=op
        if numero=="":
            numero=resultado
        opera_calculo(operacion)
        numeroPantalla.set(resultado)
        prev_sign=operacion
    except:
        numeroPantalla.set("ERROR")
        primr=True
        numero=0
        resultado=0
        prev_sign=""
        operacion=""
    exc=True

t=[]
Entry(ventana,font=('Arial',23,'bold'),textvariable=numeroPantalla,width=21,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("7")).place(x=4,y=180)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("8")).place(x=78,y=180)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("9")).place(x=152,y=180)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2,command=clear_error).place(x=227,y=180)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2,command=clear).place(x=302,y=180)#302
Button(ventana,text="4",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("4")).place(x=4,y=238)
Button(ventana,text="5",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("5")).place(x=78,y=238)
Button(ventana,text="6",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("6")).place(x=152,y=238)
Button(ventana,text="x",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("*")).place(x=227,y=238)
Button(ventana,text="√",width=7,fg="white",bg="gray13",height=2,command=raiz_cuadrada).place(x=302,y=238)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("1")).place(x=4,y=296)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("2")).place(x=78,y=296)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("3")).place(x=152,y=296)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("+")).place(x=227,y=296)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("-")).place(x=302,y=296)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("0")).place(x=4,y=354)
Button(ventana,text="/",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("/")).place(x=78,y=354)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2,command=comas).place(x=152,y=354)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("**")).place(x=227,y=354)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2,command=result).place(x=302,y=354)

Button(ventana,text="+/-",width=6,fg="white",bg="gray6",height=1,command=cambio_signo).place(x=4,y=100)
Button(ventana,text="sin",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("sin")).place(x=65,y=100)
Button(ventana,text="cos",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("cos")).place(x=126,y=100)
Button(ventana,text="tan",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("tan")).place(x=187,y=100)
Button(ventana,text="%",width=6,fg="white",bg="gray6",height=1,command=lambda:calculo("%")).place(x=248,y=100)
Button(ventana,text="1/x",width=6,fg="white",bg="gray6",height=1,command=onediv).place(x=309,y=100)
Button(ventana,text=")",width=6,fg="white",bg="cornflower blue",height=1,command=cierra_parent).place(x=65,y=136)
Button(ventana,text="R",width=6,fg="white",bg="gray6",height=1,command=rounde).place(x=126,y=136)
Button(ventana,text="π",width=6,fg="white",bg="gray6",height=1,command=pee).place(x=187,y=136)
Button(ventana,text="log",width=6,fg="white",bg="gray6",height=1,command=lambda:calculo("log")).place(x=248,y=136)
Button(ventana,text="ln",width=6,fg="white",bg="gray6",height=1,command=loga).place(x=309,y=136)
Button(ventana,text="(",width=6,fg="white",bg="cornflower blue",height=1,command=abrir_parent).place(x=4,y=136)
clear()
ventana.mainloop()
