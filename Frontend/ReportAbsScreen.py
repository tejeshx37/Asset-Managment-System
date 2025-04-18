# from tkinter import *
# from tkinter import Toplevel, Button, Tk, Menu 
# from tkinter import messagebox
# from tkinter import ttk
# from PIL import ImageTk, Image
# import tkinter as tk
from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import numpy
import ReportAbsScreenDB
import DBconnection
import InwardScreenDB


def ShowWindow():
    rootReportAbsScreen=Tk()
    ob=ReportAbsScreen(rootReportAbsScreen)
    # ob.ShowControl()
    rootReportAbsScreen.mainloop()
    
class ReportAbsScreen:
    

    def __init__(self,root):
        
        self.root=root
        root.title("AMS - 360° Abstract Report")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="360° REPORT SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill='x')
        # title=Label(root,text="FLOOR SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        # title.pack(side=TOP,fill=X)

        #============= All Variables ============
        try:
            self.im_checked = ImageTk.PhotoImage(Image.open("checked.png"))
            self.im_unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))
        except Exception as X:
            print(X) 


        self.profileID=int()
        # self.search_by=StringVar()
        # self.search_txt=StringVar()

        self.txtBuildname=StringVar()
        self.txtFloorname=StringVar()
        self.txtRoomname=StringVar()
        self.txtassetname=StringVar()
        self.txtRoomTypename=StringVar()
        self.txtRoomSubTypename=StringVar()


        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0000C6")
        RIGHT_Frame.place(x=10,y=70,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()-150)

        #Controls
        # Frame 

        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=(self.root.winfo_screenwidth()/2)-450,y=135,width=self.root.winfo_screenwidth()-530,height=250)

        # Search by Building
        lb_search=Label(details_Frame,text="Building",width=10,bg="lightblue",justify="right",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=2,column=0,padx=0,pady=10,sticky="w")
    
        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=2,column=1,pady=0,padx=0,sticky="w")

        self.cboBuild=ttk.Combobox(details_Frame,values=self.loadBuilding(),textvariable=self.txtBuildname,width=10,font=("times new roman",12),state="readonly")
        self.cboBuild.grid(row=2,column=2,sticky="w")
        self.cboBuild.bind('<<ComboboxSelected>>', self.BuildingSelected)

        # Search by Floor
        lb_search=Label(details_Frame,text="Floor",width=10,justify="right",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=3,column=0,padx=10,pady=10,sticky="w")

        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=3,column=1,pady=0,padx=0,sticky="w")

        self.cboFloor=ttk.Combobox(details_Frame,width=10,textvariable=self.txtFloorname,font=("times new roman",12),state="readonly")
        # self.cboFloor["values"]=("userid","Name")
        self.cboFloor.grid(row=3,column=2,sticky="w")
        self.cboFloor.bind('<<ComboboxSelected>>', self.FloorSelected)

        # Search by room
        lb_search=Label(details_Frame,text="Room Name",width=10,justify="right",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=2,column=5,padx=10,pady=10,sticky="w")

        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=2,column=6,pady=0,padx=0,sticky="w")
    
        
        self.cboRoom=ttk.Combobox(details_Frame,textvariable=self.txtRoomname,width=10,font=("times new roman",12),state="readonly")
        self.cboRoom.grid(row=2,column=7,sticky="w")
        self.cboRoom.bind('<<ComboboxSelected>>', self.RoomSelected)

        # Search by Asset
        lb_search=Label(details_Frame,text="Asset",width=10,justify="right",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=3,column=5,padx=10,pady=10,sticky="w")

        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=3,column=6,pady=0,padx=0,sticky="w")

        self.cboAsset=ttk.Combobox(details_Frame,textvariable=self.txtassetname,width=10,font=("times new roman",12),state="readonly")
        self.cboAsset.grid(row=3,column=7,sticky="w")
        self.cboAsset.bind('<<ComboboxSelected>>', self.AssetSelected)


        # Search by room Type
        lb_search=Label(details_Frame,text="Room Type",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=2,column=15,padx=10,pady=10,sticky="w")
       
        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=2,column=16,pady=0,padx=0,sticky="w")
    
        self.cboRoomType=ttk.Combobox(details_Frame,textvariable=self.txtRoomTypename,width=10,font=("times new roman",12),state="readonly")
        self.cboRoomType["values"]=("All","Teaching","Non-Teaching")
        self.cboRoomType.grid(row=2,column=17,sticky="w")
        self.cboRoomType.bind('<<ComboboxSelected>>', self.RoomTypSelected)

        # Search by Room Sub Type 
        lb_search=Label(details_Frame,text="Room Sub Type",width=15,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=3,column=15,padx=10,pady=10,sticky="w")

        lblcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lblcolon.grid(row=3,column=16,pady=0,padx=0,sticky="w")

        self.cboRoomSubType=ttk.Combobox(details_Frame,textvariable=self.txtRoomSubTypename,width=10,font=("times new roman",12),state="readonly")
        self.cboRoomSubType.grid(row=3,column=17,sticky="w")


        lbl_empty=Label(details_Frame,text="",width=15,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lbl_empty.grid(row=4,column=15,padx=10,pady=10,sticky="w")

        self.searchbtn=Button(details_Frame,text="View",width=10,command=self.search_Chart)
        self.searchbtn.grid(row=6,column=7,padx=1,pady=1)

        # self.btnExport=Button(details_Frame,text="Export to Excel",width=20,command=self.search_Details)
        # self.btnExport.grid(row=1,column=38,padx=20,pady=10)


    def loadBuilding(self):
        result = []
        result.append("All")
        for row in ReportAbsScreenDB.loadBuilding():
           result.append(row[0])
        return result
    
    def onclose(self):
       self.root.destroy()
       return

    def SelectRow(self,event):
        print(event.x, event.y)
        rowid = self.Access_table.identify('item',event.x,event.y) 
        tag= self.Access_table.item(rowid,"tags")[0]
        tags= list(self.Access_table.item(rowid,"tags"))
        tags.remove(tag)
        self.Access_table.item(rowid,tags=tags)
        if( tag == "checked") :
            self.Access_table.item(rowid, tags="unchecked")
        else:
            self.Access_table.item(rowid, tags="checked")

        # curosor_row=self.Access_table.focus()
        # contents=self.Access_table.item(rowid)
        # row=contents['values']
        # print(row)   

    def showChart(self):
        return

    


    def onUpdate(self):
        menuid = []
        for index in self.Access_table.get_children():
            contents=self.Access_table.item(index)
            row=contents['values']
            tag= self.Access_table.item(index,"tags")[0]
            if( tag == "checked") :
                menuid.append(row[0])
        bResult=DBconnection.GrantAccess(menuid,str(self.profileID))
        if bResult:
            messagebox.showinfo(title="AMS",message="Record sucessfuly updated.")
        else:
            messagebox.showerror(title="AMS",message="Record not updated.")
        return

    def onclose(self):
       self.root.destroy()

    def BuildingSelected(self,event):
        # self.cboFloor.set("")
        # if self.txtBuildname.get().strip()=="All" :
        #     self.cboFloor['values']="All"
        #     return
        floors=ReportAbsScreenDB.GetFloors( self.txtBuildname.get().strip())
        result = []
        result.append("All")
        for row in floors:
           result.append(row[0])
    
        self.cboFloor.set("")
        self.cboFloor['values']= result
        self.cboFloor['state']= 'readonly'
        return
    
    def FloorSelected(self,event):
       
        if  self.txtBuildname.get().strip()== "All" and self.txtFloorname.get().strip()=="All" :
            self.cboRoom.set("")
            self.cboRoom['values']="All"
            return
        floors=ReportAbsScreenDB.GetRooms( self.txtBuildname.get().strip(),self.txtFloorname.get().strip())
        result = []
        result.append("All")
        for row in floors:
           result.append(row[0])
    
        self.cboRoom.set("")
        self.cboRoom['values']= result
        self.cboRoom['state']= 'readonly'
        return  
    
    def RoomSelected(self,event):
        # self.cboAsset.set("")
        # if self.txtRoomname.get().strip()=="All" :
        #     self.cboAsset['values']="All"
        #     return
        
        self.cboAsset.set("")
        result = []
        result.append("All")
        for row in InwardScreenDB.LoadAsset():
           result.append(row[0])

        self.cboAsset['values']= result
        self.cboAsset['state']= 'readonly'
        return result
    
    def AssetSelected(self,event):
        return
    def RoomTypSelected(self,event):
        self.cboRoomSubType.set("")
        # self.txtRoomTypename
        result = []
        result.append("All")
        for row in ReportAbsScreenDB.LoadRoomSubType(self.txtRoomTypename.get().strip()):
           result.append(row[0])

        self.cboRoomSubType['values']= result
        self.cboRoomSubType['state']= 'readonly'
        return result
    
    def validation(self):
        if (self.txtBuildname.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Building Name' option from the list.")
            self.cboBuild.focus()
            return False
        if (self.txtFloorname.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Floor Name' option from the list.")
            self.cboFloor.focus()
            return False
        if (self.txtRoomname.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Room Number' option from the list.")
            self.cboRoom.focus()
            return False
        if (self.txtassetname.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Asset Name' option from the list.")
            self.cboAsset.focus()
            return False
        if (self.txtRoomTypename.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Room Type' option from the list.")
            self.cboRoomType.focus()
            return False
        
        if (self.txtRoomSubTypename.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Room Sub Type' option from the list.")
            self.cboRoomSubType.focus()
            return False
        return True
    
    def absolute_value(self,val):
        # print(numpy.abs(self.asset_values - val/100.*self.asset_values.sum()).argmin())
        a  = self.asset_values[ numpy.abs(self.asset_values - val/100.*self.asset_values.sum()).argmin() ]
        print(a)
        return a
    def search_Chart(self):
        if self.validation()==False :
            return
        rows=ReportAbsScreenDB.GetChart( self.txtBuildname.get().strip(), self.txtFloorname.get().strip() , self.txtRoomname.get().strip() , self.txtassetname.get().strip() , self.txtRoomTypename.get().strip() , self.txtRoomSubTypename.get().strip())
        listColumn = []
        listValue = []
        listExplode=[]
        for row in rows :
            listColumn.append(row[0])
            listValue.append(int(str(row[1])))
            listExplode.append(0)

        print(listColumn)
        print(listValue)
        # print(listExplode)
        fig=plt.figure(figsize=(26,6),dpi=100)     
        # asset_performance=["In-Use","Damage"]
        # self.asset_values= numpy.array([5, 15,5,4,8,9,7,5,2])
        self.asset_performance=listColumn
        self.asset_values=numpy.array(listValue)
        # self.explode=[0.2,0.2,0.2,0,0,0.2,0.2,0.2,0.2]
        # self.asset_values=[75,15]
        # print(self.explode)
        
        autotexts=plt.pie(self.asset_values,labels=self.asset_performance,startangle=90,shadow=True,explode=listExplode,autopct=self.absolute_value)
        # autotexts=plt.pie(self.asset_values,labels=asset_performance,startangle=0,explode=listExplode,shadow=True,colors=["green","red"],autopct=self.absolute_value)
        # autotexts=plt.pie(self.asset_values,labels=self.asset_performance,startangle=0,shadow=True,autopct=self.absolute_value)
        # plt.pie(asset_values,labels=asset_performance,startangle=0,shadow=True,colors=["green","red"],autopct="%2.1f%%")
        Title = "DAV School " + self.txtBuildname.get().strip()
        plt.title(Title)
        plt.legend(title="Asset Names")
        plt.show()
        return
    def search_Details(self):
        if self.validation()==False :
            return
    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)



    
    

   
