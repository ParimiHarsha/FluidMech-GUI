from tkinter import *
import tkinter as tk
import sympy as sym
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np

#Finding acceleration expression
def Acceleration(U,b,A0,L,a) :

    x, y, z, t = sym.symbols('x y z t')

    Vo = U*(1+a*t)
    A = A0*(1-b*x)

    V = (Vo*A0)/A
    u = (U*(1+a*t)*A0)/(A0*(1-b*x))

    v = 0
    w = 0

    temp = u*sym.diff(V,x) + v*sym.diff(V,y) + w*sym.diff(V,z) + sym.diff(V,t)
    A = temp
    A = sym.N(temp,2)
    acceleration = Label(mainarea, text = "Acceleration , A = {}".format(A), font='Helvetica 18 bold',bg='#aec2ea')
    acceleration.grid(row=8,column=0,columnspan=50, padx=0, pady=15, sticky=W)

#Finding the acceleration at the given point
def Ap() :
    x, y, z, t = sym.symbols('x y z t')

    A0 =float(InA0.get())
    b = float(Inb.get())
    U = float(InC.get())
    a = float(Ina.get())
    L = float(InL.get())
    Xp = float(Inxp.get())
    Tp = float(Intp.get())

    if(Xp < 0 or Tp < 0 or A0<0 or L<0 ) :
        tk.messagebox.showerror('Error', 'Please enter valid input')
    else :
        Vo = U*(1+a*t)
        A = A0*(1-b*x)

        V = (Vo*A0)/A
        u = (U*(1+a*t)*A0)/(A0*(1-b*x))

        v = 0
        w = 0

        A = u*sym.diff(V,x) + v*sym.diff(V,y) + w*sym.diff(V,z) + sym.diff(V,t)

        res_exp = A.subs([(x, Xp), (t, Tp)])
        labres = Label(mainarea, text="A(Xp,Tp) = {}".format(res_exp), font='Helvetica 20 bold',bg='#aec2ea')
        labres.grid(row=13 , column=0, padx=15, pady=15, columnspan= 30)

def Submit():
    try :
        A0 =float(InA0.get())
        b = float(Inb.get())
        U = float(InC.get())
        a = float(Ina.get())
        L = float(InL.get())
        if(A0 < 0) :
            tk.messagebox.showerror('Error', 'Please enter valid input')

        elif(L < 0) :
            tk.messagebox.showerror('Error', 'Please enter valid input')
        else :
            Acceleration(U,b,A0,L,a)
    except :
        tk.messagebox.showerror('Error', 'Please enter valid input')

#Creating GUI
root = Tk()
root.title("Flow through nozzles")
root.geometry('1500x900')

# main area
mainarea = Frame(root, width=500, bg='#aec2ea', height=500, relief='raised', borderwidth=2, highlightbackground="black",highlightthickness=2)
mainarea.pack(expand=True, fill='both', side='left', anchor='nw')
#graph area
graph_area = Frame(root, bg='#CCC', width=400, height=500, highlightbackground="black",highlightthickness=1)
graph_area.pack(expand=True, fill='both', side='right')

#Creating Labels
label = Label(mainarea,text='Consider the incompressible flow of a fluid through a nozzle.The area of the nozzle is given by \n A = A0(1−bx) and the inlet velocity varies according to V = U(1+at), where',pady=10,font='20',bg='#f6e58d')
label.grid(row=0,column=0,columnspan=10,sticky=N)
label.configure(anchor = "center")

labA = Label(mainarea, text ="A0(in ft^2)", font='Helvetica 18 bold', bg='#aec2ea')
labA.grid(row=3,column=0, padx=15, pady=15)

InA0 = Entry(mainarea)
InA0.grid(row=3,column=1, padx=15, pady=15)

labb = Label(mainarea, text="b(in ft^-1)",font='Helvetica 18 bold',bg='#aec2ea')
labb.grid(row=3, column=3, padx=15, pady=15)
Inb = Entry(mainarea)
Inb.grid(row=3, column=4, padx=15, pady=15)

labC = Label(mainarea, text="U(in ft/sec)",font='Helvetica 18 bold',bg='#aec2ea')
labC.grid(row=4, column=0, padx=15, pady=15)
InC = Entry(mainarea)
InC.grid(row=4, column=1, padx=15, pady=15)

labela = Label(mainarea, text="a(in sec^-1)",font='Helvetica 18 bold',bg='#aec2ea')
labela.grid(row=4, column=3, padx=15, pady=15)
Ina = Entry(mainarea)
Ina.grid(row=4, column=4, padx=15, pady=15)

labL = Label(mainarea, text="L(in ft)",font='Helvetica 18 bold',bg='#aec2ea')
labL.grid(row=5, column=0, padx=15, pady=15)
InL = Entry(mainarea)
InL.grid(row=5, column=1, padx=15, pady=15)

labA = Label(mainarea, text=" ",font='Helvetica 18 bold',bg='#aec2ea')
labA.grid(row=8, column=0, padx=0, pady=15,columnspan=30, sticky= W)

labg = Label(mainarea, text=" ",font='Helvetica 18 bold',bg='#aec2ea')
labg.grid(row=13, column=0, padx=0, pady=15,columnspan=30, sticky= W)

labxp = Label(mainarea, text="Xp(in ft)", font='Helvetica 20 bold',bg='#aec2ea')
labxp.grid(row=11, column=0, padx=15, pady=15)
Inxp = Entry(mainarea)
Inxp.grid(row=11, column=1, padx=5, pady=5)

labtp = Label(mainarea, text="Tp(in sec)", font='Helvetica 20 bold',bg='#aec2ea')
labtp.grid(row=11, column=3, padx=15, pady=15)
Intp = Entry(mainarea)
Intp.grid(row=11, column=4, padx=15, pady=15)

labxt = Label(mainarea, text="Enter the values for X and T at which you want to find the acceleration:", font='Helvetica 18 bold',bg='#aec2ea')
labxt.grid(row=10, column= 0, columnspan= 30, padx=15, pady=15, sticky= W)


#Drawing graphs
def draw_graphs():
    A0 = float(InA0.get())
    b = float(Inb.get())
    U = float(InC.get())
    a = float(Ina.get())
    L = float(InL.get())
    xp = float(Inxp.get())
    tp = float(Intp.get())

    if(xp < 0 or tp < 0 or A0<0 or L<0 ) :
        tk.messagebox.showerror('Error', 'Please enter valid input')

    else :
        graph = Figure(figsize=(4, 4), dpi=80)
        x = np.arange(0, L, 0.1)
        y = ((b * (U ** 2)) * (1 + a * tp) ** 2) / (1 - b * x) ** 3 + a * U / (1 - b * x)
        plot1 = graph.add_subplot(111)
        plot1.plot(x, y)

        canvas1 = FigureCanvasTkAgg(graph, master=graph_area)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=2, column=0, columnspan=2,padx=10)
        labg1 = Label(graph_area, text="A vs x :", font='Helvetica 18 bold', bg='#CCC')
        labg1.grid(row=0, column=0, padx=0, pady=15, columnspan=30, sticky=W)

        graph1 = Figure(figsize=(4, 4), dpi=80)
        t = np.arange(0, L, 0.1)
        y1 = ((b * (U ** 2)) * (1 + a * t) ** 2) / (1 - b * xp) ** 3 + a * U / (1 - b * xp)
        plot2 = graph1.add_subplot(111)
        plot2.plot(t, y1)
        canvas2 = FigureCanvasTkAgg(graph1, master=graph_area)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=4, column=0)
        labg2 = Label(graph_area, text="A vs t :",bg='#CCC', font='Helvetica 18 bold')
        labg2.grid(row=3, column=0, padx=0, pady=15, columnspan=30, sticky=W)

#Creating buttons
submitbutton = Button(mainarea, text="Submit", command=Submit, activebackground='#33ff33',font=25)
submitbutton.grid(row=4, column=5)

inputxt = Button(mainarea, text="Submit", command = lambda : Ap(), activebackground='#33ff33',font=25)
inputxt.grid(row=11, column=5, padx=15, pady=15)

graphbutton = Button(mainarea, text="Show graphs", activebackground='#33ff33',font=25, command=lambda : draw_graphs())
graphbutton.grid(row= 14, column=2, padx=15, pady=15)

root.mainloop()
