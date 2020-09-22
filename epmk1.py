import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from io import BytesIO
from sympy.utilities.lambdify import lambdify
#import tkFont
#plt.ioff
#%%timeit
class testme:
    def __init__(self,frame1):
        self.frame1=frame1  
        #self.frame2=frame2
        self.font = Font(size=18)
        length_label1 = tk.Label(self.frame1, text=r'v', font=self.font).grid(column=0,row=2)
        length_label2 = tk.Label(self.frame1, text=r'g', font=self.font).grid(column=0,row=3)
        length_label3 = tk.Label(self.frame1, text=r'k', font=self.font).grid(column=0,row=4)
        length_label4 = tk.Label(self.frame1, text=r'a', font=self.font).grid(column=0,row=5)
        self.button=tk.Button(self.frame1,text="Plot",command=self.plot, font=self.font)
        self.button.grid(column=0,row=0)
        #self.button.get_tk_widget()
        self.button1=tk.Button(self.frame1,text="Clear Plot",command=self.clearme, font=self.font)
        self.button1.grid(column=1,row=0)
        self.scale1 = tk.Scale(self.frame1, from_=0, to=5,width=10,tickinterval=0.1, orient=tk.HORIZONTAL)#,
                             # command = self.plot)
        self.scale1.set(0)
        self.scale1.grid(column=0,row=2, columnspan=3)
        self.scale2 = tk.Scale(self.frame1, from_=0, to=5,width=10,tickinterval=0.1, orient=tk.HORIZONTAL)#,
                             # command = self.plot)
        self.scale2.set(0)
        self.scale2.grid(column=0,row=3, columnspan=3)
        self.scale3 = tk.Scale(self.frame1, from_=0, to=5,width=10,tickinterval=0.1, orient=tk.HORIZONTAL)#,
                              #command = self.plot)
        self.scale3.set(1)
        self.scale3.grid(column=0,row=4, columnspan=3)
        self.scale4 = tk.Scale(self.frame1, from_=0, to=5,width=10,tickinterval=0.1, orient=tk.HORIZONTAL)#,
                              #command = self.plot)
        self.scale4.set(1)
        self.scale4.grid(column=0,row=5, columnspan=3)
        self.var = tk.StringVar(self.frame1)
        self.var.set("H") # initial value
        self.option = tk.OptionMenu(self.frame1, self.var, "H", "NH")#, "PT")
        self.option.grid(column=1,row=1)
        self.img_lbl = tk.Label(self.frame1)
        self.img_lbl.grid(column = 3, row = 2)
        self.img_lbl2 = tk.Label(self.frame1)
        self.img_lbl2.grid(column = 2, row = 2)
    def plot(self):   
        try: 
            self.wierdobject.get_tk_widget().grid_forget()
        except AttributeError: 
            pass
        t = sp.Symbol('t')
        a = sp.Symbol('a')
        v = sp.Symbol('v')
        g = sp.Symbol('g')
        k = sp.Symbol('k')
        obj2 = BytesIO()
        H2 = sp.Matrix([[-a*t,v+1j*g],[v+1j*k,a*t]])
        sp.preview(H2, viewer='BytesIO', output='png', outputbuffer=obj2,dvioptions=['-D','150'])
        obj2.seek(0)
        self.img_lbl2.img = ImageTk.PhotoImage(Image.open(obj2))
        self.img_lbl2.configure(image=self.img_lbl2.img)
        tp = self.var.get()
        if tp == 'H':
            
            v = self.scale1.get()
            a = self.scale4.get()
            g = self.scale2.get()
            self.H1 = sp.Matrix([[-a*t,v+1j*g],[v-1j*g, a*t]])
            obj = BytesIO()
            sp.preview(self.H1, viewer='BytesIO', output='png', outputbuffer=obj,dvioptions=['-D','150'])
            obj.seek(0)
            self.img_lbl.img = ImageTk.PhotoImage(Image.open(obj))
            self.img_lbl.configure(image=self.img_lbl.img)
        elif tp =='NH':
            v = self.scale1.get()
            g = self.scale2.get()
            k = self.scale3.get()
            a = self.scale4.get()
            self.H1 = sp.Matrix([[-a*t,v+1j*g],[v+1j*k, a*t]])
            obj = BytesIO()
            sp.preview(self.H1, viewer='BytesIO', output='png', outputbuffer=obj,dvioptions=['-D','150'])
            obj.seek(0)
            #self.img_lbl = tk.Label(self.frame1)
            #self.img_lbl.grid(column = 2, row = 2)
            self.img_lbl.img = ImageTk.PhotoImage(Image.open(obj))
            self.img_lbl.config(image=self.img_lbl.img)
        #self.H1 = sp.Matrix([[-t,v],[v, t]])
        #[egvalsrall1,egvalsrall2,egvalsiall1,egvalsiall2, egprodsall, UR] = self.all_eigvals()
        [egvectsallvals,UR] = self.all_eigvals2()
        #f=Figure(figsize=(5,1)) 
        fig, (ax0, ax1) = plt.subplots(nrows = 1, ncols =2, figsize=(15,5))
        #Figure.figure(figsize=(15,5))
        #aplt=f.add_subplot(111)
        #k1 = self.scale1.get()
        #aplt.plot(UR, egvalsrall1,'--') 
        #ax0.plot(UR, egvalsiall1,color='C0',linestyle='--',label=r'$\Re{(E_{1})}$')
        #ax0.plot(UR, egvalsrall1,color='C0',linestyle='-',label = r'$\Im{(E_{1})}$')
        #ax0.plot(UR, egvalsiall2,color='C1',linestyle = '--',label=r'$\Im{(E_{2})}$')
        #ax0.plot(UR, egvalsrall2,color ='C1',linestyle ='-',label=r'$\Re{(E_{2})}$')
        ax0.plot(UR.real, egvectsallvals[0][0].real,color ='C0',linestyle ='-',label=r'$\Re{(E_{2})}$')
        ax0.plot(UR.real, egvectsallvals[1][0].real,color ='C1',linestyle ='-',label=r'$\Re{(E_{2})}$')
        ax0.plot(UR.real, egvectsallvals[0][0].imag,color ='C0',linestyle ='--',label=r'$\Re{(E_{2})}$')
        ax0.plot(UR.real, egvectsallvals[1][0].imag,color ='C1',linestyle ='--',label=r'$\Re{(E_{2})}$')
        ax0.set_xlabel('t',fontsize=15)
        ax0.set_ylabel('E',fontsize=15)
        #ax0.legend(fontsize=15)
        #ax1.plot(egvalsrall1,egvalsiall1,label=r'${E_{1}}$')
        #ax1.plot(egvalsrall2,egvalsiall2,label=r'${E_{2}}$')
        if tp=='H':
            egprodsall = np.zeros(len(UR))
        elif tp == 'NH':
            #print((egvectsallvals[0][2][0][0]))
            egvecs1 = np.stack((egvectsallvals[0][2][0][0][0], np.ones((len(UR)))),axis=-1) 
            egvecs2 = np.stack((egvectsallvals[1][2][0][0][0], np.ones((len(UR)))),axis=-1)
            egv1 = np.divide(egvecs1,np.array(np.sum(np.abs(egvecs1)**2,axis=-1)**(1./2)).reshape((-1,1)))
            egv2 = np.divide(egvecs2,np.array(np.sum(np.abs(egvecs2)**2,axis=-1)**(1./2)).reshape((-1,1)))
            egprodsall = 1-np.abs(np.einsum('ij,ij->i', egv1, egv2))**2
        ax1.plot(UR.real, egprodsall)
        #ax1.set_xlabel(r'$\Re{(E)}$',fontsize=15)
        #ax1.set_ylabel(r'$\Im{(E)}$',fontsize=15)
        #ax1.plot(UR, egvectsallvals[0][0].real,color ='C1',linestyle ='-',label=r'$\Re{(E_{2})}$')
        #ax1.plot(UR, egvectsallvals[1][0].real,color ='C1',linestyle ='-',label=r'$\Re{(E_{2})}$')
        ax1.set_ylabel(r'$|<\Phi_{i}|\Phi_{j}>|^{2}$',fontsize = 15)
        ax1.set_xlabel('t',fontsize=15)
        #ax1.legend(fontsize=15)
        egvectsallvals = None
        self.wierdobject = FigureCanvasTkAgg(fig, master=self.frame1) 
        self.wierdobject.get_tk_widget().grid(columnspan = 3) 
        self.wierdobject.draw() 

    def clearme(self):       
        self.wierdobject.get_tk_widget().grid_forget() 
        self.img_lbl.config(image='')
    def all_eigvals(self):
        t = sp.Symbol("t")
        egvects = list(self.H1.eigenvects())
        egval1 = egvects[0][0]
        egval2 = egvects[1][0]
        egvec1 = sp.Matrix(egvects[0][2])/(sp.Matrix(egvects[0][2]).norm())
        egvec2 = sp.Matrix(egvects[1][2])/(sp.Matrix(egvects[1][2]).norm())
        egprod = sp.conjugate(sp.Matrix(egvec1)).dot(egvec2)
        UR = np.arange(-5, 5, 0.1)
        egvalsrall1 = np.zeros((len(UR),1))
        egvalsiall1 = np.zeros((len(UR),1))
        egvalsrall2 = np.zeros((len(UR),1))
        egvalsiall2 = np.zeros((len(UR),1))
        egprodsall = np.zeros((len(UR),1))
        #egprodsiall = np.zeros((len(UR),1))
        for i in range(0,len(UR)):
            egvalsrall1[i] = sp.re(egval1.subs([(t,UR[i])]))#,(n,V[i,j])]))
            egvalsiall1[i] = sp.im(egval1.subs([(t,UR[i])]))#,(n,V[i,j])]))
            egvalsrall2[i] = sp.re(egval2.subs([(t,UR[i])]))#,(n,V[i,j])]))
            egvalsiall2[i] = sp.im(egval2.subs([(t,UR[i])]))#,(n,V[i,j])]))
            egprodsall[i] = sp.Abs(sp.simplify(egprod.subs([(t,UR[i])])))**2 
            #egprodsiall[i] = sp.im(sp.simplify(egprod.subs([(t,UR[i])]))) 
        return egvalsrall1,egvalsrall2,egvalsiall1,egvalsiall2,egprodsall,UR
    def all_eigvals2(self):
        t = sp.Symbol("t")
        egvectsall = self.H1.eigenvects()
        func = lambdify(t, egvectsall,'numpy')
        UR = np.arange(-5, 5, 0.1,dtype =complex)
        egvectsallsub = func(UR)
        return egvectsallsub, UR

root=tk.Tk()
root.title("Exceptional Points") 
aframe=tk.Frame(root)
#a1frame=tk.Frame(root)
testme(aframe)
aframe.pack()  #packs a frame which given testme packs frame 1 in testme
root.mainloop()
