from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import UserStatusDB

def ShowWindow():
    rootUserStatus=Tk()
    ob=UserStatus(rootUserStatus)
    ob.ShowControl()
    rootUserStatus.mainloop()
    
class UserStatus:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - User Active / Deactive")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="USER ACTIVATE / DEACTIVE SCREEN",font=("times new roman",25,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============

        self.txtuserid=StringVar()
        self.txtid=StringVar()
        self.txtname=StringVar()
        self.txtemail=StringVar()
        self.txtphone=StringVar()
        self.txtstatus=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.labelCntText=StringVar()

        self.labelCntText="Showing Details - "


    def ShowControl(self):
        self.manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        self.manage_Frame.place(x=5,y=70,width=550,height=630)
        
        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=570,y=70,width=790,height=630)

        # Id of user
        getid=Label(self.manage_Frame,text="Profile ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=2,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=2,column=1,pady=0,padx=0,sticky="w")

        self.id=Entry(self.manage_Frame,width=30,textvariable=self.txtid,bg="lightgrey",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.id.grid(row=2,column=1,padx=20,sticky="w")
        self.id.config(state="readonly")

         # User Id of user
        getid=Label(self.manage_Frame,text="User ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=4,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=4,column=1,pady=0,padx=0,sticky="w")

        self.id=Entry(self.manage_Frame,width=30,textvariable=self.txtuserid,bg="lightgrey",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.id.grid(row=4,column=1,padx=20,sticky="w")

        #Name of User
        getname=Label(self.manage_Frame,text="Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=6,column=1,pady=0,padx=0,sticky="w")

        self.txt_Name=Entry(self.manage_Frame,width=30,textvariable=self.txtname,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Name.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        # eMail ID
        getemail=Label(self.manage_Frame,text="eMail ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getemail.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=8,column=1,pady=0,padx=0,sticky="w")

        txt_email=Entry(self.manage_Frame,width=30,textvariable=self.txtemail,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        # Phone
        getphone=Label(self.manage_Frame,text="Phone",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getphone.grid(row=10,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=10,column=1,pady=0,padx=0,sticky="w")

        txt_phone=Entry(self.manage_Frame,width=30,textvariable=self.txtphone,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_phone.grid(row=10,column=1,pady=10,padx=20,sticky="w")

        # Address
        getaddress=Label(self.manage_Frame,text="Status",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getaddress.grid(row=12,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=12,column=1,pady=0,padx=0,sticky="w")

        combo_status=ttk.Combobox(self.manage_Frame,textvariable=self.txtstatus,width=10,font=("times new roman",12,"bold"),state="readonly")
        combo_status["values"]=("Active","Deactive")
        combo_status.grid(row=12,column=1,pady=10,padx=22,sticky="w")

        btn_Frame=Frame(self.manage_Frame,bd=4,relief=RIDGE,bg="BLUE")
        btn_Frame.place(x=165,y=380,width=330)

        # adding add,modify,delete,cancel buttons
        modifybtn=Button(btn_Frame,text="Modify",width=10,command=self.Modify_User).grid(row=0,column=1,padx=50,pady=10)
        cancelbtn=Button(btn_Frame,text="Clear",width=10,command=self.Clear_User).grid(row=0,column=3,padx=10,pady=10)
        
        # Search
        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=10,y=5,width=765,height=600)

        #RIGHT_Frame.place(x=570,y=70,width=790,height=630)
        lb_search=Label(details_Frame,text="Search By:",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
        combo_search=ttk.Combobox(details_Frame,textvariable=self.search_by,width=10,font=("times new roman",12,"bold"),state="readonly")
        combo_search["values"]=("userid","Name")
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
        self.User_table=ttk.Treeview(Table_Frame,columns=("pid","puserid","pname","pemail","pphone","pstatus"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.User_table.xview)
        scroll_y.config(command=self.User_table.yview)

        self.User_table.column("pid",anchor=CENTER, stretch=NO, width=70)
        self.User_table.column("puserid",anchor=W, stretch=NO, width=90)
        self.User_table.column("pname",anchor=W, stretch=NO, width=150)
        self.User_table.column("pemail",anchor=W, stretch=NO, width=130)
        self.User_table.column("pphone", anchor=W, stretch=NO, width=90)
        self.User_table.column("pstatus", anchor=W, stretch=NO, width=80)

        self.User_table.heading("pid",text="Profile ID")
        self.User_table.heading("puserid",text="User ID")
        self.User_table.heading("pname", text="Name")
        self.User_table.heading("pemail", text="eMail")
        self.User_table.heading("pphone", text="Phone")
        self.User_table.heading("pstatus", text="Status")
        self.User_table['show']='headings'
        self.User_table.pack(fill=BOTH,expand=1)
        self.User_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
       

    def get_cursor(self,ev):
        curosor_row=self.User_table.focus()
        contents=self.User_table.item(curosor_row)
        row=contents['values']
        self.txtid.set(row[0])
        self.txtuserid.set(row[1])
        self.txtname.set(row[2])
        self.txtemail.set(row[3])
        self.txtphone.set(row[4])
        self.txtstatus.set(row[5])
        return


    def search_data(self):
        icnt = int()
        icnt=0
        rows=UserStatusDB.getSearchRecord(self.search_by.get(),self.search_txt.get().strip())
        if len(rows)!=0:
            self.User_table.delete(*self.User_table.get_children()) 
            for row in rows:
                self.User_table.insert('',END,values=row) 
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)

    def fetch_data(self):
        icnt = int()
        icnt=0
        rows=UserStatusDB.getRecords()
        if len(rows)!=0:
            self.User_table.delete(*self.User_table.get_children()) 
            for row in rows:
                self.User_table.insert('',END,values=row)
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)
    
    def Modify_User(self):
        bUpdated=UserStatusDB.UpdateStatus(self.txtid.get().strip(),self.txtstatus.get().strip())
        if bUpdated:
            self.Clear_User()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly Updated.")
        else:
            messagebox.showerror(title="AMS",message="Record not Updated.")
        return

    def Clear_User(self):
        # messagebox.showinfo(title="AMS",message=self.txtid.get()+self.txtuserid.get()+self.txtname.get()+self.txtemail.get()+self.txtphone.get()+self.txtstatus.get())
        self.txtid.set("")
        self.txtuserid.set("")
        self.txtname.set("")
        self.txtemail.set("")
        self.txtphone.set("")
        self.txtstatus.set("")


# root=Tk()
# ob=BuildingScreen(root)
# root.mainloop()

   
