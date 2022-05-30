from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
#raiz.geometry("392x488")
#operacion=""
#resultado=0
oper=False
prime_ope=True

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

def numeroPulsado(num):
    global operacion
    global oper
    global prime_ope
    if oper==True:
        numeroPantalla.set(num)
        oper=False
    else:
        if prime_ope==True:
            num=num.replace(numeroPantalla.get(),num)
            prime_ope=False
            numeroPantalla.set(num)
        else:
            numeroPantalla.set(numeroPantalla.get()+num)

def clear():
    global operacion
    global resultado
    global oper
    global prime_ope
    operacion=""
    resultado=0
    oper=False
    numeroPantalla.set(resultado)
    if prime_ope==False:
        prime_ope=True
    
def division(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="divi"
    if resultado!=0:
        resultado/=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def multiplic(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="multi"
    if resultado!=0:
        resultado*=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def suma(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="suma"
    resultado+=float(num)
    numeroPantalla.set(resultado)

def resta(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="resta"
    if resultado!=0:
        resultado-=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def el_resultado():
    global resultado
    if operacion=="suma":
        numeroPantalla.set(resultado+float(numeroPantalla.get()))
    if operacion=="resta":
        numeroPantalla.set(resultado-float(numeroPantalla.get()))
    if operacion=="multi":
        numeroPantalla.set(resultado*float(numeroPantalla.get()))
    if operacion=="divi":
        numeroPantalla.set(resultado/float(numeroPantalla.get()))
    resultado=0
    
clear()

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=2, column=4)

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonRes=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=3, column=4)

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:multiplic(numeroPantalla.get()))
botonMult.grid(row=4, column=4)

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botoncoma=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botoncoma.grid(row=5, column=2)
botonResul=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonResul.grid(row=5, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=5, column=4)
botonclear=Button(miFrame, text="C", width=3, command=clear)
botonclear.grid(row=6,column=1)

raiz.mainloop()

