from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import FloorScreenDB

def ShowWindow():
    rootFloor=Tk()
    ob=FloorScreen(rootFloor)
    ob.ShowControl()
    rootFloor.mainloop()
    
class FloorScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Floor Master")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="FLOOR MASTER SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============
        self.txtid=StringVar()
        self.txtBuildname=StringVar()
        self.txtFloorname=StringVar()
        self.txtdescr=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.labelCntText=StringVar()

        self.labelCntText="Showing Details - "


    def ShowControl(self):
        self.manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        self.manage_Frame.place(x=5,y=70,width=550,height=630)
        
        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=570,y=70,width=790,height=630)

        # Id of building
        getid=Label(self.manage_Frame,text="ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=2,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=2,column=1,pady=0,padx=0,sticky="w")

        self.id=Entry(self.manage_Frame,width=30,textvariable=self.txtid,bg="lightgrey",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.id.grid(row=2,column=1,padx=20,sticky="w")
        self.id.config(state="readonly")
        print("End")

        #Name of building
        getlblBuilding=Label(self.manage_Frame,text="Build Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getlblBuilding.grid(row=4,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=4,column=1,pady=0,padx=0,sticky="w")

        self.combo_Building_Name=ttk.Combobox(self.manage_Frame,values=self.loadBuilding(),textvariable=self.txtBuildname,width=36,font=("times new roman",12,"bold"),state="readonly")
        self.combo_Building_Name.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #Name of Floor
        getfloorname=Label(self.manage_Frame,text="Floor Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getfloorname.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=6,column=1,pady=0,padx=0,sticky="w")

        self.txt_Name=Entry(self.manage_Frame,width=30,textvariable=self.txtFloorname,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Name.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        # Description of FLOOR
        getdescr=Label(self.manage_Frame,text="Description",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getdescr.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=7,column=1,pady=0,padx=0,sticky="w")

        txt_descr=Entry(self.manage_Frame,width=30,textvariable=self.txtdescr,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_descr.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        btn_Frame=Frame(self.manage_Frame,bd=4,relief=RIDGE,bg="BLUE")
        btn_Frame.place(x=126,y=250,width=390)

        # adding add,modify,delete,cancel buttons
        self.addbtn=ttk.Button(btn_Frame,text="Add",width=10,command=self.add_Record)
        self.addbtn.grid(row=0,column=0,padx=15,pady=10)

        self.modifybtn=ttk.Button(btn_Frame,text="Modify",width=10,command=self.Modify_Record)
        self.modifybtn.grid(row=0,column=1,padx=10,pady=10)

        self.deletebtn=ttk.Button(btn_Frame,text="Delete",width=10,command=self.Delete_Record)
        self.deletebtn.grid(row=0,column=2,padx=10,pady=10)

        self.cancelbtn=ttk.Button(btn_Frame,text="Clear",width=10,command=self.Clear_Screen)
        self.cancelbtn.grid(row=0,column=3,padx=10,pady=10)
  
        # Search

        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=10,y=5,width=765,height=600)

        #RIGHT_Frame.place(x=570,y=70,width=790,height=630)
        lb_search=Label(details_Frame,text="Search By:",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
        combo_search=ttk.Combobox(details_Frame,textvariable=self.search_by,width=10,font=("times new roman",12),state="readonly")
        combo_search["values"]=("Build Name","Floor Name")
        combo_search.grid(row=0,column=1,sticky="w")
        # combo_search.grid(row=0,column=1,padx=100,pady=15,sticky="w")

        txtsearch=Entry(details_Frame,textvariable=self.search_txt,width=30, font=("times new roman",12,"bold"))
        txtsearch.grid(row=0,column=2,padx=10,pady=10,sticky="w")

        searchbtn=Button(details_Frame,text="Search",width=10,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=20,pady=10)

        showallbtn=Button(details_Frame,text="Showall",width=10,command=self.fetch_data)
        showallbtn.grid(row=0,column=4,padx=20,pady=10)

        self.lb_recordCnt=Label(details_Frame,text="",width=20,bg="yellow",fg="darkblue",font=("times new roman",10,"bold"))
        self.lb_recordCnt.grid(row=1,column=2,padx=10,pady=0,sticky="w")

        #========Table======
        Table_Frame=Frame(details_Frame,bd=0,relief=RIDGE,bg="lightblue")
        Table_Frame.place(x=10,y=70,width=680,height=450)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Floor_table=ttk.Treeview(Table_Frame,columns=("fid","fbname","fname","fdesc"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Floor_table.xview)
        scroll_y.config(command=self.Floor_table.yview)

        self.Floor_table.column("fid",anchor=CENTER, stretch=NO, width=70)
        self.Floor_table.column("fbname", anchor=W, stretch=NO, width=170)
        self.Floor_table.column("fname",anchor=W, stretch=NO, width=80)
        self.Floor_table.column("fdesc", anchor=W, stretch=NO, width=200)

        self.Floor_table.heading("fid",text="Floor ID")
        self.Floor_table.heading("fbname", text="Building Name")
        self.Floor_table.heading("fname",text="Floor Name")
        self.Floor_table.heading("fdesc", text="Description")

        self.Floor_table['show']='headings'
        self.Floor_table.pack(fill=BOTH,expand=1)
        self.Floor_table.bind("<ButtonRelease-1>",self.get_cursor)  
        self.fetch_data()
        

    def DisableButton(self,mode):
        if (mode==1) :
            self.addbtn.config(state=NORMAL)
            self.modifybtn.config(state=DISABLED)
            self.deletebtn.config(state=DISABLED)
            self.cancelbtn.config(state=NORMAL)
        elif(mode==2):
            self.addbtn.config(state=DISABLED)
            self.modifybtn.config(state=NORMAL)
            self.deletebtn.config(state=NORMAL)
            self.cancelbtn.config(state=NORMAL)
        return
    
    def loadBuilding(self):
        result = []
        for row in FloorScreenDB.loadBuilding():
           result.append(row[0])
        return result

    def get_cursor(self,ev):
        curosor_row=self.Floor_table.focus()
        contents=self.Floor_table.item(curosor_row)
        row=contents['values']
        self.txtid.set(row[0])
        self.txtBuildname.set(row[1])
        self.txtFloorname.set(row[2])
        self.txtdescr.set(row[3])

    def search_data(self):
        icnt = int()
        icnt=0
        rows=FloorScreenDB.getSearchRecord(self.search_by.get(),self.search_txt.get())
        if len(rows)!=0:
            self.Floor_table.delete(*self.Floor_table.get_children()) 
            for row in rows:
                self.Floor_table.insert('',END,values=row) 
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)

    def fetch_data(self):
        icnt = int()
        icnt=0
        rows=FloorScreenDB.getRecords()
        if len(rows)!=0:
            self.Floor_table.delete(*self.Floor_table.get_children()) 
            for row in rows:
                self.Floor_table.insert('',END,values=row)
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)
        # self.DisableButton(1)
        
    def IsEmpty(self):
        if (self.txtBuildname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Building name from the list.")
             self.combo_Building_Name.focus()
             return True
        elif (self.txtFloorname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please ENTER valid Floor Details.")
             self.txt_Name.focus()
             return True
        return False
    
    def add_Record(self):
        if self.IsEmpty():
            return
        bResult=FloorScreenDB.IsbuildFloorExist(self.txtBuildname.get(),self.txtFloorname.get())
        if(bResult):
            messagebox.showinfo(title="AMS",message="Already details exists.")
            return
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
        bInserted=FloorScreenDB.addnewrecord(self.txtBuildname.get(),self.txtFloorname.get(),self.txtdescr.get())
        if bInserted:
            self.Clear_Screen()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly added.")
        else:
            messagebox.showerror(title="AMS",message="Record not saved.")
        return
    
    def Modify_Record(self):
        if (self.txtid.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the record from the grid list.")
            #  self.combo_Building_Name.focus()
             return True
        if self.IsEmpty():
            return
        bResult=FloorScreenDB.IsbuildFloorExist(self.txtBuildname.get(),self.txtFloorname.get())
        if(bResult):
            messagebox.showinfo(title="AMS",message="Already details exists.")
            return
        bUpdated=FloorScreenDB.UpdateRecord(self.txtid.get(),self.txtBuildname.get(),self.txtFloorname.get(),self.txtdescr.get())
        if bUpdated:
            self.Clear_Screen()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly Updated.")
        else:
            messagebox.showerror(title="AMS",message="Record not Updated.")
        return
    
    def Delete_Record(self):
        if (self.txtid.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select the record from the grid list.")
            #  self.combo_Building_Name.focus()
            return True
        answer = messagebox.askyesno(title='confirmation', message='Are you sure that you want to delete the selected reocrd?')
        if answer:         
            bDeleted=FloorScreenDB.DeleteRecord(self.txtid.get())
            # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
            if bDeleted:
                self.Clear_Screen()
                self.fetch_data()
                messagebox.showinfo(title="AMS",message="Record sucessfuly Deleted.")
            else:
                messagebox.showerror(title="AMS",message="Record not Deleted.")
                
            return
    
    def Clear_Screen(self):
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtFloorname.get()+self.txtdescr.get())
        self.txtid.set("")
        self.txtBuildname.set("")
        self.txtFloorname.set("")
        self.txtdescr.set("")
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtFloorname.get()+self.txtdescr.get())
                    

    def onclickadd(a,b,c):
        messagebox.showinfo(title="AMS",message=a.get()+b.get()+c.get()) 
        print(a.get(),"Freash")

    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)


    # def add(a,c):
    #     bInserted=FloorScreenDB.addnewrecord(a,c)
    #     if bInserted:
    #         messagebox.showinfo(title="AMS",message="Record sucessfuly added.")
    #     else:
    #         messagebox.showerror(title="AMS",message="Record not saved.")
    #     return

    
    
# root=Tk()
# ob=BuildingScreen(root)
# root.mainloop()
# ShowWindow()    
   
