from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import AssertMasterScreenDB

def ShowWindow():
    rootAssertMaster=Tk()
    ob=AssertMasterScreen(rootAssertMaster)
    ob.ShowControl()
    rootAssertMaster.mainloop()
    
class AssertMasterScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Asset Master")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="ASSET MASTER SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============
        self.txtid=StringVar()
        self.txtname=StringVar()
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
        getname=Label(self.manage_Frame,text="Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=4,column=1,pady=0,padx=0,sticky="w")

        self.txt_Name=Entry(self.manage_Frame,width=30,textvariable=self.txtname,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Name.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        # Description of Building
        getdescr=Label(self.manage_Frame,text="Description",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getdescr.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=5,column=1,pady=0,padx=0,sticky="w")

        txt_descr=Entry(self.manage_Frame,width=30,textvariable=self.txtdescr,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_descr.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        btn_Frame=Frame(self.manage_Frame,bd=4,relief=RIDGE,bg="BLUE")
        # btn_Frame.place(x=55,y=250,width=430)
        btn_Frame.place(x=100,y=250,width=410)

        # adding add,modify,delete,cancel buttons
        addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_Building).grid(row=0,column=0,padx=10,pady=10)
        modifybtn=Button(btn_Frame,text="Modify",width=10,command=self.Modify_Building).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.Delete_Building).grid(row=0,column=2,padx=10,pady=10)
        cancelbtn=Button(btn_Frame,text="Clear",width=10,command=self.Clear_Building).grid(row=0,column=3,padx=10,pady=10)
        
        # Search
        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=10,y=5,width=765,height=600)

        lb_search=Label(details_Frame,text="Search By:",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
        self.combo_search=ttk.Combobox(details_Frame,textvariable=self.search_by,width=10,font=("times new roman",12),state="readonly")
        self.combo_search["values"]=("ID","Name")
        self.combo_search.grid(row=0,column=1,sticky="w")

        self.txtsearch=Entry(details_Frame,textvariable=self.search_txt,width=30, font=("times new roman",12,"bold"))
        self.txtsearch.grid(row=0,column=2,padx=10,pady=10,sticky="w")

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
        self.Assert_table=ttk.Treeview(Table_Frame,columns=("aid","aname","adesc"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Assert_table.xview)
        scroll_y.config(command=self.Assert_table.yview)

        self.Assert_table.column("aid",anchor=CENTER, stretch=NO, width=70)
        self.Assert_table.column("aname",anchor=W, stretch=NO, width=170)
        self.Assert_table.column("adesc", anchor=W, stretch=NO, width=270)

        self.Assert_table.heading("aid",text="Assert ID")
        self.Assert_table.heading("aname", text="Assert Name")
        self.Assert_table.heading("adesc", text="Description")
        self.Assert_table['show']='headings'
        self.Assert_table.pack(fill=BOTH,expand=1)
        self.Assert_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
       

    def get_cursor(self,ev):
        curosor_row=self.Assert_table.focus()
        contents=self.Assert_table.item(curosor_row)
        row=contents['values']
        self.txtid.set(row[0])
        self.txtname.set(row[1])
        self.txtdescr.set(row[2])

    def search_data(self):
        if (self.search_by.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Search By' option from the list.")
            self.combo_search.focus()
            return
        if (self.search_txt.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please Enter valid input.")
            self.txtsearch.focus()
            return        
        icnt = int()
        icnt=0
        rows=AssertMasterScreenDB.getSearchRecord(self.search_by.get().strip(),self.search_txt.get().strip())
        if len(rows)!=0:
            self.Assert_table.delete(*self.Assert_table.get_children()) 
            for row in rows:
                self.Assert_table.insert('',END,values=row) 
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)

    def fetch_data(self):
        icnt = int()
        icnt=0
        rows=AssertMasterScreenDB.getRecords()
        if len(rows)!=0:
            self.Assert_table.delete(*self.Assert_table.get_children()) 
            for row in rows:
                self.Assert_table.insert('',END,values=row)
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)

    def IsEmpty(self):
        if (self.txtname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please ENTER valid Builiding Name.")
             self.txt_Name.focus()
             return True
        return False
    
    def add_Building(self):
        if self.IsEmpty():
            return
        bResult=AssertMasterScreenDB.IsAssertExist(self.txtname.get().strip())
        if(bResult):
            messagebox.showinfo(title="AMS",message="Already details exists.")
            return
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
        bInserted=AssertMasterScreenDB.addnewrecord(self.txtname.get().strip(),self.txtdescr.get().strip())
        if bInserted:
            self.Clear_Building()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly added.")
        else:
            messagebox.showerror(title="AMS",message="Record not saved.")
        return
    
    def Modify_Building(self):
        if (self.txtid.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select the record from the grid list.")
            #  self.combo_Building_Name.focus()
            return True
        if self.IsEmpty():
            return
        bResult=AssertMasterScreenDB.IsAssertExist(self.txtname.get().strip())
        if(bResult):
            messagebox.showinfo(title="AMS",message="Already details exists.")
            return
    
        bUpdated=AssertMasterScreenDB.UpdateBuilding(self.txtid.get().strip(),self.txtname.get().strip(),self.txtdescr.get().strip())
        if bUpdated:
            self.Clear_Building()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly Updated.")
        else:
            messagebox.showerror(title="AMS",message="Record not Updated.")
        return
    
    def Delete_Building(self):
        if (self.txtid.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select the record from the grid list.")
            #  self.combo_Building_Name.focus()
            return True
        answer = messagebox.askyesno(title='confirmation', message='Are you sure that you want to delete the selected reocrd?')
        if answer:         
            bDeleted=AssertMasterScreenDB.DeleteBuilding(self.txtid.get())
            # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
            if bDeleted:
                self.Clear_Building()
                self.fetch_data()
                messagebox.showinfo(title="AMS",message="Record sucessfuly Deleted.")
            else:
                messagebox.showerror(title="AMS",message="Record not Deleted.")
            return
    
    def Clear_Building(self):
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
        self.txtid.set("")
        self.txtname.set("")
        self.txtdescr.set("")
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtname.get()+self.txtdescr.get())
                    

    def onclickadd(a,b,c):
        messagebox.showinfo(title="AMS",message=a.get()+b.get()+c.get()) 
        print(a.get(),"Freash")

    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)


    def add(a,c):
        bInserted=AssertMasterScreenDB.addnewrecord(a,c)
        if bInserted:
            messagebox.showinfo(title="AMS",message="Record sucessfuly added.")
        else:
            messagebox.showerror(title="AMS",message="Record not saved.")
        return

    
    
# root=Tk()
# ob=BuildingScreen(root)
# root.mainloop()
# ShowWindow()    
   
