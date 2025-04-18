from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
from tkinter import ttk
import re
import ProfileScreenDB
import PasswordChangeScreenDB

def ShowWindow(pid,autoclose):
    rootPwdScreen=Tk()
    ob=PasswordChangeScreen(rootPwdScreen)
    ob.ShowControl(pid,autoclose)
    rootPwdScreen.mainloop()
    return ob.pwdUpdated
    
class PasswordChangeScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Change Password")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="CHANGE PASSWORD SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)

        #============= All Variables ============
        self.txtuserid=StringVar()
        self.txtid=StringVar()
        self.txtname=StringVar()
        # self.txtemail=StringVar()
        self.txtoldpwd=StringVar()
        self.txtnewpwd=StringVar()
        self.txtnewpwdconfirm=StringVar()
        self.autoclose=BooleanVar()
        self.pwdUpdated= BooleanVar()

    def onChange(s):
        print(s.txtoldpwd.get(),"old")
        
        return
    def ShowControl(self,pid,autoclose):
        self.autoclose=autoclose
        self.txtid=pid

        self.GetDetails()

        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=10,y=70,width=self.root.winfo_screenwidth()-20,height=self.root.winfo_screenheight()-150)

        #Controls
        details_Frame=Frame(RIGHT_Frame,bd=35,relief=RIDGE,bg="lightblue")
        details_Frame.place(x=250,y=5,width=765,height=600)

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

        getuseridvalue=Label(details_Frame,text=self.txtid,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridvalue.grid(row=4,column=10,pady=10,padx=22,sticky="w")

        # Name
        getname=Label(details_Frame,text="Name",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=6,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=6,column=5,pady=10,padx=22,sticky="w")

        getnamevalue=Label(details_Frame,text=self.txtname,bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getnamevalue.grid(row=6,column=10,pady=10,padx=22,sticky="w")


        # Old Password
        getname=Label(details_Frame,text="Old Password",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=8,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=8,column=5,pady=10,padx=22,sticky="w")

        self.txt_oldpwd=Entry(details_Frame,show='*',width=30,textvariable=self.txtoldpwd,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_oldpwd.grid(row=8,column=10,pady=10,padx=20,sticky="w")

        # New  Password
        getname=Label(details_Frame,text="New Password",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=10,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=10,column=5,pady=10,padx=22,sticky="w")

        self.txt_Newpwd=Entry(details_Frame,show='*',width=30,textvariable=self.txtnewpwd,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Newpwd.grid(row=10,column=10,pady=10,padx=20,sticky="w")

         # confirm pwd
        getname=Label(details_Frame,text="Confirm Password",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getname.grid(row=12,column=0,pady=10,padx=22,sticky="w")

        getuseridcolon=Label(details_Frame,text=":",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridcolon.grid(row=12,column=5,pady=10,padx=22,sticky="w")

        self.txt_Confirmpwd=Entry(details_Frame,show='*',width=30,textvariable=self.txtnewpwdconfirm,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Confirmpwd.grid(row=12,column=10,pady=10,padx=20)

        # empty space
        getuseridspace=Label(details_Frame,text=" ",bg="lightblue",fg="darkblue",font=("times new roman",20,"bold"))
        getuseridspace.grid(row=16,column=5,pady=10,padx=22,sticky="w")

        # Sumit button
        btnSubmit=Button(details_Frame,text="Submit",width=10,fg="darkblue",font=("times new roman",20,"bold"),command=self.onChangePassword)
        btnSubmit.grid(row=18,column=0,padx=0,pady=0)

        # close button
        btnClose=Button(details_Frame,text="Close",width=10,fg="darkblue",font=("times new roman",20,"bold"),command=self.onclose)
        btnClose.grid(row=18,column=10,padx=0,pady=0)

    def GetDetails(self):
        for row in PasswordChangeScreenDB.GetDetails(str(self.txtid)):
            self.txtuserid=row[0]
            self.txtname=row[1]

    def PasswordPolicyValid(self):
        # Must include at least one uppercase character
        # Must include at least one lowercase character
        # Must include at least one number
        # Must include at least one special character
        # Must have a length of at least 8 and a max of 20
        password=self.txtnewpwdconfirm.get().strip()
        re_exp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        if re.search(re.compile(re_exp),password):
            return True
        else:
            return False

       
    def onChangePassword(self):
        if self.txtoldpwd.get().strip() =="" or self.txtoldpwd.get().strip() == "" or self.txtnewpwd.get().strip()=="" :
            messagebox.showerror(title="AMS",message="Mandatory fields are missing")
            return
            # To check the old and new password are same
        if self.txtoldpwd.get().strip() == self.txtnewpwd.get().strip() :
            messagebox.showerror(title="AMS",message="Old and New password are same.\nPlease enter different password.")
            return
        if self.txtnewpwdconfirm.get().strip() != self.txtnewpwd.get().strip() :
            messagebox.showerror(title="AMS",message="New and Confirmation password not matching.")
            return
        
        if self.PasswordPolicyValid()==False:
            sMsg="Must include at least one uppercase character.\n"
            sMsg+="Must include at least one lowercase character.\n"
            sMsg+="Must include at least one number.\n"
            sMsg+="Must include at least one special character.\n"
            sMsg+="Must have a length of at least 8 and a max of 20.\n"
            messagebox.showerror(title="AMS",message=sMsg)
            return

        bUpdated=PasswordChangeScreenDB.UpdatePassword(str(self.txtid),self.txtoldpwd.get().strip(),self.txtnewpwd.get().strip())
        if bUpdated:
            self.pwdUpdated=True
            messagebox.showinfo(title="AMS- Password Policy",message="Password successfully Updated.")
            if(self.autoclose == True):
                self.root.destroy()

        else:
            self.pwdUpdated=False
            messagebox.showerror(title="AMS",message="Password not Updated.")
        return
    

    def onclose(self):
       self.root.destroy()

    #def onclick():
    #  messagebox.showinfo(title="AMS",message="This function is working in progress")  

    # def onclick():
    #     messagebox.showinfo(title="AMS",message="This fuction is working in progress",parent=tkwindow)


    # def fetchdata(self):
    #     row=ProfileScreenDB.getProfileDetails(self.txtid) 
    #     if len(row)!=0:
    #         # self.txtid=row[0]
    #         self.txtuserid=row[0][0]
    #         self.txtname=row[0][1]
    #         self.txtemail=row[0][2]
    #         self.txtphone=row[0][3]
    #         self.txtaddress=row[0][4]
    #     return

    
    
# root=Tk()
# ob=BuildingScreen(root)
# root.mainloop()

   
