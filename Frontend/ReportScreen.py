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
import UserAccessDB
import DBconnection



def ShowWindow():
    rootUserAccess=Tk()
    ob=UserAccess(rootUserAccess)
    ob.ShowControl()
    rootUserAccess.mainloop()
    
class UserAccess:
    

    def __init__(self,root):
        
        self.root=root
        root.title("AMS - User Access")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="GRAND / REVOKE ACCESS",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
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
        self.search_by=StringVar()
        self.search_txt=StringVar()

        
    def ShowControl(self):


        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=10,y=70,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()-150)

        #Controls
        # Frame 

        details_Frame=Frame(RIGHT_Frame,bd=10,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=50,y=5,width=self.root.winfo_screenwidth()-200,height=100)

        # Search id
        lb_search=Label(details_Frame,text="Search By:",width=10,bg="lightblue",fg="darkblue",font=("times new roman",12,"bold"))
        lb_search.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
        # combo
        self.combo_search=ttk.Combobox(details_Frame,textvariable=self.search_by,width=10,font=("times new roman",12,"bold"),state="readonly")
        self.combo_search["values"]=("userid","Name")
        self.combo_search.grid(row=0,column=1,sticky="w")

        self.txtsearch=Entry(details_Frame,textvariable=self.search_txt,width=30, font=("times new roman",12,"bold"))
        self.txtsearch.grid(row=0,column=2,padx=10,pady=10,sticky="w")

        searchbtn=Button(details_Frame,text="Search",width=10,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=20,pady=10)

        GRID_Frame=Frame(RIGHT_Frame,bd=10,relief=RIDGE,bg="Grey")
        GRID_Frame.place(x=50,y=120,width=self.root.winfo_screenwidth()-200,height=self.root.winfo_screenheight()-(450))

        scroll_x=Scrollbar(GRID_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(GRID_Frame,orient=VERTICAL)

        self.Access_table=ttk.Treeview(GRID_Frame,columns=(1,2),height=130)
        # ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        

        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Access_table.xview)
        scroll_y.config(command=self.Access_table.yview)

        self.Access_table.column('#0',width=5)
        self.Access_table.column('#1',width=10)
        self.Access_table.column('#2',width=20)

        self.Access_table.heading('#0',text="")
        self.Access_table.heading('#1',text="Mennu ID")
        self.Access_table.heading('#2', text="Menu Name")
        # self.Access_table.heading("bdesc", text="Description")
        # self.Access_table['show']='headings'
        self.Access_table.pack(fill=BOTH,expand=1)

        self.style= ttk.Style(self.Access_table)
        self.style.configure('TreeView',rowheight=50)

        self.Access_table.tag_configure('checked',image=self.im_checked)
        self.Access_table.tag_configure('unchecked',image=self.im_unchecked)

        self.Access_table.bind('<Button 1>', self.SelectRow)
        # Bottom_LEFT_Frame=Frame(RIGHT_Frame,bd=10,relief=RIDGE,bg="Grey")
        # Bottom_LEFT_Frame.place(x=50,y=120,width=500,height=self.root.winfo_screenheight()-(120+170))
        
        # Bottom_LEFT_Frame=Frame(RIGHT_Frame,bd=10,relief=RIDGE,bg="lightgreen")
        # Bottom_LEFT_Frame.place(x=700,y=120,width=500,height=self.root.winfo_screenheight()-(120+170))
        
        Bottom_Frame=Frame(RIGHT_Frame,bd=10,relief=RIDGE,bg="lightgreen")
        Bottom_Frame.place(x=50,y=450,width=self.root.winfo_screenwidth()-200,height=90)


        # Sumit button
        btnSubmit=Button(Bottom_Frame,text="Submit",width=10,fg="darkblue",font=("times new roman",20,"bold"),command=self.onUpdate)
        btnSubmit.grid(row=1,column=10,padx=80,pady=10)

        # close button
        btnClose=Button(Bottom_Frame,text="Close",width=10,fg="darkblue",font=("times new roman",20,"bold"),command=self.onclose)
        btnClose.grid(row=1,column=25,padx=80,pady=10)
    

    # def toggleCheck(self):
	#     rid= self.Access_table.identify_row(event.y)
    #     tag=self.Access_table.item(rowid,"tags")[0]
        # self.Access_table.
        # tag= self.Access_table.item(rowid,"tags")[0]
        # 
        #
    


    
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


    def search_data(self):
        if (self.search_by.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please select 'Search By' option from the list.")
            self.combo_search.focus()
            return
        if (self.search_txt.get().strip()==""):
            messagebox.showinfo(title="AMS",message="Please Enter valid input.")
            self.txtsearch.focus()
            return   
        
        ### Load all menus
        rows= UserAccessDB.GetMenus()
        if len(rows)!=0:
            self.Access_table.delete(*self.Access_table.get_children()) 
            for row in rows:
                self.Access_table.insert('',END,values=row,tags="unchecked") 

        self.profileID= UserAccessDB.GetUserProfileid(self.search_by.get().strip(),self.search_txt.get().strip())
        if self.profileID == -1:
            msg=self.search_by.get().strip() + " ( " + self.search_txt.get().strip() + " )"
            msg += "not found."
            messagebox.showinfo(title="AMS",message=msg)
            return
        
        # Checkbox selected if the user have access to the screen   
        userrows= UserAccessDB.GetUserMenu(self.profileID)
        if len(userrows)!=0:
            for userrow in userrows:
                usermenuid=userrow[0]
                for i in self.Access_table.get_children():
                    contents=self.Access_table.item(i)
                    row=contents['values']
                    menuid=row[0]
                    if( menuid == usermenuid):
                        self.Access_table.item(i, tags="checked")
                        break


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

    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)



    
    

   
