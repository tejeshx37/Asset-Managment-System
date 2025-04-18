from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import ProfileScreenDB

def ShowWindow(pid):
    rootProfile=Tk()
    ob=ProfileScreen(rootProfile)
    ob.ShowControl(pid)
    rootProfile.mainloop()
    
class ProfileScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Profile")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="MY DETAILS",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============
        self.txtuserid=StringVar()
        self.txtid=StringVar()
        self.txtname=StringVar()
        self.txtemail=StringVar()
        self.txtphone=StringVar()
        self.txtaddress=StringVar()

    def ShowControl(self,pid):
        
        self.txtid=pid
        # self.txtuserid=2
        # self.txtname="Tejesh"
        # self.txtemail="Noemail@gmail.com"
        # self.txtphone="9042512878"
        # self.txtaddress="My Address"

        self.fetchdata()

        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=10,y=70,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()-150)


        #Controls
        # Frame 

        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=10,y=5,width=765,height=600)

        # user id
        getuserid=Label(details_Frame,text="User ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuserid.grid(row=2,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=2,column=5,pady=10,padx=22,sticky="w")

        getuseridvalue=Label(details_Frame,text=self.txtuserid,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridvalue.grid(row=2,column=10,pady=10,padx=22,sticky="w")

        ## id
        getid=Label(details_Frame,text="Profile ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getid.grid(row=4,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=4,column=5,pady=10,padx=22,sticky="w")

        getidvalue=Label(details_Frame,text=self.txtid,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getidvalue.grid(row=4,column=10,pady=10,padx=22,sticky="w")

        # Name
        getname=Label(details_Frame,text="Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=6,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=6,column=5,pady=10,padx=22,sticky="w")

        getnamevalue=Label(details_Frame,text=self.txtname,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getnamevalue.grid(row=6,column=10,pady=10,padx=22,sticky="w")


        # email id
        getname=Label(details_Frame,text="Email ID",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=8,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=8,column=5,pady=10,padx=22,sticky="w")

        getnamevalue=Label(details_Frame,text=self.txtemail,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getnamevalue.grid(row=8,column=10,pady=10,padx=22,sticky="w")

         # Phone
        getname=Label(details_Frame,text="Phone",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=10,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=10,column=5,pady=10,padx=22,sticky="w")

        getnamevalue=Label(details_Frame,text=self.txtphone,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getnamevalue.grid(row=10,column=10,pady=10,padx=22,sticky="w")

        

         # Address
        getname=Label(details_Frame,text="Address",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=12,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=12,column=5,pady=10,padx=22,sticky="w")

        getnamevalue=Label(details_Frame,text=self.txtaddress,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getnamevalue.grid(row=12,column=10,pady=10,padx=22,sticky="w")

        # empty space
        getuseridspace=Label(details_Frame,text=" ",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridspace.grid(row=16,column=5,pady=10,padx=22,sticky="w")

         # Close button
        btnClose=Button(details_Frame,text="Close",width=10,fg="darkblue",font=("times new roman",20,"bold"),command=self.onclose)
        btnClose.grid(row=18,column=10,padx=20,pady=10)

        details_Frame.pack()
       
       

    

    def onclose(self):
       self.root.destroy()

    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)


    def fetchdata(self):
        row=ProfileScreenDB.getProfileDetails(self.txtid) 
        if len(row)!=0:
            # self.txtid=row[0]
            self.txtuserid=row[0][0]
            self.txtname=row[0][1]
            self.txtemail=row[0][2]
            self.txtphone=row[0][3]
            self.txtaddress=row[0][4]
        return

    
    
# root=Tk()
# ob=BuildingScreen(root)
# root.mainloop()

   
