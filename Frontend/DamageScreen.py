from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import DamageScreenDB

def ShowWindow():
    rootDamageScreen=Tk()
    ob=DamageScreen(rootDamageScreen)
    ob.ShowControl()
    rootDamageScreen.mainloop()
    
class DamageScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Asset Screen ")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="DAMAGE ENTRY SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============
        self.txtid=StringVar()
        self.txtassetid=StringVar()
        self.txtBuildname=StringVar()
        self.txtFloorname=StringVar()
        self.txtRoomname=StringVar()
        self.txtRoomTypename=StringVar()
        self.txtRoomSubTypename=StringVar()
        self.txtassetname=StringVar()
        self.txtassetcnt=StringVar()
        self.txtdamage=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        self.labelCntText=StringVar()
        self.labelCntText="Showing Details - "


    def ShowControl(self):
        self.manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        self.manage_Frame.place(x=5,y=70,width=550,height=630)
        
        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=570,y=70,width=790,height=630)

        # Id of room
        getid=Label(self.manage_Frame,text="ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=1,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=1,column=1,pady=0,padx=0,sticky="w")

                     
        self.id=Entry(self.manage_Frame,width=30,textvariable=self.txtid,bg="lightgrey",font=("times new roman",12,"bold"),state="readonly")
        self.id.grid(row=1,column=1,padx=20,sticky="w")

        getid=Label(self.manage_Frame,text="Asset ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=2,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=2,column=1,pady=0,padx=0,sticky="w")

        self.assertid=Entry(self.manage_Frame,width=30,textvariable=self.txtassetid,bg="lightgrey",font=("times new roman",12,"bold"),state="readonly")
        self.assertid.grid(row=2,column=1,padx=20,sticky="w")
    

        #Name of building
        getlblBuilding=Label(self.manage_Frame,text="Build Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getlblBuilding.grid(row=4,column=0,pady=10,padx=22,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=4,column=1,pady=0,padx=0,sticky="w")

        self.txt_Bulding=ttk.Entry(self.manage_Frame,textvariable=self.txtBuildname,width=30,font=("times new roman",12,"bold"),state="readonly")
        self.txt_Bulding.grid(row=4,column=1,pady=10,padx=20,sticky="w")


        #Name of Floor
        getroomname=Label(self.manage_Frame,text="Floor Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomname.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=6,column=1,pady=0,padx=0,sticky="w")

        self.txt_Floor=ttk.Entry(self.manage_Frame,textvariable=self.txtFloorname,width=30,font=("times new roman",12,"bold"),state="readonly")
        self.txt_Floor.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        self.txt_Floor.config(state="readonly")


        # NAME of ROOM 
        getroomname=Label(self.manage_Frame,text="Room Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomname.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=7,column=1,pady=0,padx=0,sticky="w")

        self.txt_Room_Name=ttk.Entry(self.manage_Frame,textvariable=self.txtRoomname,width=30,font=("times new roman",12,"bold"),state="readonly")
        self.txt_Room_Name.grid(row=7,column=1,pady=5,padx=20,sticky="w")
        self.txt_Room_Name.config(state="readonly")

        #Name of room Type
        getroomTypename=Label(self.manage_Frame,text="Room Type",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomTypename.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=8,column=1,pady=0,padx=0,sticky="w")

        self.txt_roomType=Entry(self.manage_Frame,width=30,textvariable=self.txtRoomTypename,bg="lightgrey",font=("times new roman",12,"bold"))
        self.txt_roomType.grid(row=8,column=1,padx=20,sticky="w")
        self.txt_roomType.config(state="readonly")

        #Name of Sub room Type
        getroomSubTypename=Label(self.manage_Frame,text="Room SubType",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomSubTypename.grid(row=9,column=0,pady=5,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row=9,column=1,pady=0,padx=0,sticky="w")

        self.txt_roomSubType=Entry(self.manage_Frame,width=30,textvariable=self.txtRoomSubTypename,bg="yellow",font=("times new roman",12,"bold"),state="readonly")
        self.txt_roomSubType.grid(row=9,column=1,padx=20,sticky="w")

        #Name of Asset
        getroomname=Label(self.manage_Frame,text="Item Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomname.grid(row=10,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row= 10,column=1,pady=0,padx=0,sticky="w")

        self.txt_Assert=ttk.Entry(self.manage_Frame,textvariable=self.txtassetname,width=30,font=("times new roman",12,"bold"),state="readonly")
        self.txt_Assert.grid(row=10,column=1,pady=5,padx=20,sticky="w")
        self.txt_Assert.config(state="readonly")

        #Name of Asset Count
        getroomname=Label(self.manage_Frame,text="Item Count",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomname.grid(row=11,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row= 11,column=1,pady=0,padx=0,sticky="w")

        self.txt_AssertCount=ttk.Entry(self.manage_Frame,textvariable=self.txtassetcnt,width=30,font=("times new roman",12,"bold"),state="readonly")
        self.txt_AssertCount.grid(row=11,column=1,pady=5,padx=20,sticky="w")
        self.txt_Assert.config(state="readonly")

        #damage
        getroomname=Label(self.manage_Frame,text="Damage",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getroomname.grid(row=12,column=0,pady=10,padx=20,sticky="w")

        lblcolon=Label(self.manage_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        lblcolon.grid(row= 12,column=1,pady=0,padx=0,sticky="w")

        self.cbodamage=ttk.Combobox(self.manage_Frame,textvariable=self.txtdamage,width=28,font=("times new roman",12,"bold"),state="readonly")
        self.cbodamage.grid(row=12,column=1,pady=5,padx=20,sticky="w")
        self.cbodamage["values"]=("Damage","Active")


        btn_Frame=Frame(self.manage_Frame,bd=4,relief=RIDGE,bg="BLUE")
        btn_Frame.place(x=210,y=550,width=280)

        self.modifybtn=ttk.Button(btn_Frame,text="Modify",width=10,command=self.Modify_Record)
        self.modifybtn.grid(row=0,column=5,padx=35,pady=10)

        self.cancelbtn=ttk.Button(btn_Frame,text="Clear",width=10,command=self.Clear_Screen)
        self.cancelbtn.grid(row=0,column=6,padx=30,pady=10)
  
        # Search

        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=10,y=5,width=765,height=600)

        lb_search=Label(details_Frame,text="Search By:",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
        combo_search=ttk.Combobox(details_Frame,textvariable=self.search_by,width=10,font=("times new roman",12),state="readonly")
        combo_search["values"]=("Asset ID","Category ID","Item Name","Room","Room Type","Room SubType","Build Name","Floor Name")
        combo_search.grid(row=0,column=1,sticky="w")


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
        self.Floor_table=ttk.Treeview(Table_Frame,columns=("adid","assetid","damage","itemname","itemcnt","roomname","roomtype","roomsubtype","buildname","floorname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Floor_table.xview)
        scroll_y.config(command=self.Floor_table.yview)

        self.Floor_table.column("adid",anchor=CENTER, stretch=NO, width=50)
        self.Floor_table.column("assetid",anchor=CENTER, stretch=NO, width=50)
        self.Floor_table.column("damage",anchor=CENTER, stretch=NO, width=55)
        self.Floor_table.column("itemname",anchor=W, stretch=NO, width=67)
        self.Floor_table.column("itemcnt",anchor=CENTER, stretch=NO, width=67)
        self.Floor_table.column("roomname",anchor=CENTER, stretch=NO, width=50)
        self.Floor_table.column("roomtype",anchor=CENTER, stretch=NO, width=67)
        self.Floor_table.column("roomsubtype",anchor=W, stretch=NO, width=89)
        self.Floor_table.column("buildname",anchor=W, stretch=NO, width=87)
        self.Floor_table.column("floorname",anchor=CENTER, stretch=NO, width=70)

        self.Floor_table.heading("adid",text="Asset ID")
        self.Floor_table.heading("assetid",text="Category ID")
        self.Floor_table.heading("damage", text="Status")
        self.Floor_table.heading("itemname", text="Item Name")
        self.Floor_table.heading("itemcnt", text="Item Count")
        self.Floor_table.heading("roomname",text="Room")
        self.Floor_table.heading("roomtype", text="Room type")
        self.Floor_table.heading("roomsubtype", text="Room Sub type")
        self.Floor_table.heading("buildname", text="Building Name")
        self.Floor_table.heading("floorname",text="Floor Name")

        self.Floor_table['show']='headings'
        self.Floor_table.pack(fill=BOTH,expand=1)
        self.Floor_table.bind("<ButtonRelease-1>",self.get_cursor)  
        self.fetch_data()

   
    def get_cursor(self,ev):
        curosor_row=self.Floor_table.focus()
        contents=self.Floor_table.item(curosor_row)
        row=contents['values']
        self.txtid.set(row[0])
        self.txtassetid.set(row[1])
        self.txtdamage.set(row[2])
        self.txtassetname.set(row[3])
        self.txtassetcnt.set(row[4])
        self.txtRoomname.set(row[5])  
        self.txtRoomTypename.set(row[6])
        self.txtRoomSubTypename.set(row[7])
        self.txtBuildname.set(row[8])
        self.txtFloorname.set(row[9])
        
    def search_data(self):
        icnt = int()
        icnt=0
        rows=DamageScreenDB.getSearchRecord(self.search_by.get(),self.search_txt.get())
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
        rows=DamageScreenDB.getRecords()
        if len(rows)!=0:
            self.Floor_table.delete(*self.Floor_table.get_children()) 
            for row in rows:
                self.Floor_table.insert('',END,values=row)
                icnt+=1
            cnt=self.labelCntText+str(icnt)
            self.lb_recordCnt.config(text=cnt)
        
    def IsEmpty(self):
        if (self.txtBuildname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Building name from the list.")
             self.txt_Bulding.focus()
             return True
        elif (self.txtFloorname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Floor name from the list.")
             self.txt_Floor.focus()
             return True
        elif (self.txtRoomname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Room name from the list.")
             self.txt_Room_Name.focus()
             return True
        elif (self.txtRoomTypename.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Room Type from the list.")
             self.cboRoomType.focus()
             return True
        elif (self.txtRoomSubTypename.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Room SubType from the list.")
             self.cboRoomSubType.focus()
             return True
        elif (self.txtassetname.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Item name from the list.")
             self.txt_Assert.focus()
             return True
        elif (self.txtassetcnt.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the Item count from the list.")
             self.txt_AssertCount.focus()
             return True
        return False
    
    
    
    def Modify_Record(self):
        if (self.txtdamage.get().strip()==""):
             messagebox.showinfo(title="AMS",message="Please select the status from the grid list.")
             self.cbodamage.focus()
             return True
        if self.IsEmpty():
            return
        # bResult=DamageScreenDB.IsAssetExist(self.txtassetcnt.get().strip(),self.txtassetname.get().strip(),self.txtBuildname.get().strip(),self.txtFloorname.get().strip(),self.txtRoomname.get().strip(),self.txtRoomTypename.get().strip(),self.txtRoomSubTypename.get().strip())
        # if(bResult):
        #     messagebox.showinfo(title="AMS",message="Already details exists.")
        #     return

        bUpdated=DamageScreenDB.UpdateRecord(self.txtid.get(),self.txtdamage.get().strip())
        if bUpdated:
            self.Clear_Screen()
            self.fetch_data()
            messagebox.showinfo(title="AMS",message="Record sucessfuly Updated.")
        else:
            messagebox.showerror(title="AMS",message="Record not Updated.")
        return
    
   
    
    def Clear_Screen(self):
        self.txtid.set("")
        self.txtdamage.set("")
        self.txtRoomname.set("")
        self.txtRoomTypename.set("")
        self.txtRoomSubTypename.set("")
        self.txtBuildname.set("")
        self.txtFloorname.set("")
        self.txtassetname.set("")
        self.txtassetcnt.set("")
        self.txtassetid.set("")

    
# ShowWindow()    
   
