# import tkinter as tk
from tkinter import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
# ,NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
# from tkinter import Toplevel, Button, Tk, Menu 
# from tkinter import messagebox
# from tkinter import ttk
import AbstractReportDB


def ShowWindow(pid):
    rootAbstractReport=Tk()
    ob=AbstractReport(rootAbstractReport)
    ob.ShowControl(pid)
    rootAbstractReport.mainloop()

class AbstractReport:
    def __init__(self,root):    
        self.root=root
        root.title("AMS - Abstract Report")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
        title=Label(root,text="Asset Cost Abstract Report",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill='x')
 
    def GetValues(self):
        Valuelist=AbstractReportDB.GetAbtDetails()
        for row in Valuelist: 
            if row[0] !=0 :
                self.inuseCnt=row[0]
            if row[1] !=0 :
                self.damageCnt=row[1]

    def ShowControl(self,pid):
        self.inuseCnt=StringVar()
        self.damageCnt=StringVar()
        self.damageCnt=0

        self.GetValues()
        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0000C6")
        RIGHT_Frame.place(x=10,y=70,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()-150)

        self.details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        self.details_Frame.place(x=(self.root.winfo_screenwidth()/2)-220,y=55,width=400,height=230)

        getinuse=Label(self.details_Frame,text="In-Use",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getinuse.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=1,column=1,pady=10,padx=10,sticky="w")

        getinusecnt=Label(self.details_Frame,text=self.inuseCnt,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getinusecnt.grid(row=1,column=2,pady=1,padx=1,sticky="w")

        getdmg=Label(self.details_Frame,text="Damage",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getdmg.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        getdmg=Label(self.details_Frame,text=self.damageCnt,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getdmg.grid(row=2,column=2,pady=1,padx=1,sticky="w")

        self.searchbtn=Button(self.details_Frame,text="View",width=10,command=self.ShowChart)
        self.searchbtn.grid(row=3,column=1,pady=10,padx=0)

    def ShowChart(self):
        fig=plt.figure(figsize=(6,6),dpi=100)     
        asset_performance=["In-Use","Damage"]
        asset_values=[self.inuseCnt,self.damageCnt]
        plt.pie(asset_values,labels=asset_performance,startangle=0,explode=[0.2,0],shadow=True,colors=["green","red"],autopct="%2.1f%%")
        plt.title("Asset Details")
        plt.legend(title="Performance")
        plt.show()

    
