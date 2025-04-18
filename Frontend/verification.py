from tkinter import *
from tkinter import messagebox
from screeninfo import get_monitors
import DBconnection

def ForeResetPassword(profileid):
    for row in DBconnection.ForeResetPassword(profileid):
        return True
    return False
     
def Show():
        root=Tk()
        ob=verification(root)
        return ob.valid()
       

class verification:

    def __init__(self,root):
        self.root=root
        self.root.title("AMS - Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False,False)
        # self.root.state(newstate='zoomed') 

    def valid(self):
       
        self.profileid=int()
        self.txtusername=StringVar()
        self.txtpassword=StringVar()

        self.profileid=0

        # self.txtusername.set("0901005")
        # self.txtpassword.set("Tejesh")
        global loginsucess
        loginsucess="False"

        self.img=PhotoImage(file='login.png')
        Label(self.root,image=self.img,bg='white').place(x=50,y=50)

        frame=Frame(self.root,width=350,height=350,bg="white")
        frame.place(x=480,y=70)
        heading=Label(frame,text='Sign in', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)

        ############################
        def on_enter(e):
            self.user.delete(0,'end')
 
        def on_leave(e):
            name=self.user.get()    
            if name=='':
                self.user.insert(0,'Username')

        self.user= Entry(frame,width=25,fg='black',border=0,bg="white",textvariable=self.txtusername,font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30,y=80)
        self.user.insert(0,'Username')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        #########################
        def on_enter(e):
            self.code.delete(0,'end')
            self.code.config(show='*')
 
        def on_leave(e):
            name=self.code.get()    
            if name=='':
                self.code.insert(0,'Password')
                self.code.config(show='')

        self.code= Entry(frame,width=25,fg='black',border=0,textvariable=self.txtpassword,bg="white",font=('Microsoft YaHei UI Light',11))

        self.code.place(x=30,y=150)
        self.code.insert(0,'Password')
        self.code.bind('<FocusIn>',on_enter)
        self.code.bind('<FocusOut>',on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
        #############################

        Button(frame,width=39,pady=7,text='Sign in',bg='#57a1fe',fg='white',border=0,command=self.login).place(x=35,y=204)


    
        # l1=Label(self.root,text="Userid:",font=(16))
        # l2=Label(self.root,text="Password:",font=(16))
        # l1.grid(row=0,column=0,padx=5,pady=5)
        # l2.grid(row=1,column=0,padx=5,pady=5)

       
        # t1=Entry(self.root,textvariable=self.txtusername,font=(16))
        # t2=Entry(self.root,textvariable=self.txtpassword,font=(16),show="*")
        # t1.grid(row=0,column=1)
        # t2.grid(row=1,column=1)
        # h=t1.get()
        # print(h)
        # b1=Button(self.root,command=self.login,text="Login",font=(16))
        # b2=Button(self.root,command=self.root.quit,text="Exit",font=(16))
        # b1.grid(row=2,column=1,sticky=W)
        # b2.grid(row=2,column=1,sticky=E)


        self.root.mainloop()
        print(self.profileid,"correct")
        return self.profileid

    

    # def on_enter(self,e):
    #     self.code.delete(0,'end')
 
    # def on_leave(self,e):
    #     name=self.code.get()    
    #     if name=='':
    #         self.code.insert(0,'Password')
            
        # def login(txtusername,txtpassword):
    def login(self):
            # global profileid
            # profileid=0
            b=self.txtusername.get()
            print(b,"fresh")
            x=len(b.strip())
            if x==0:
                messagebox.showinfo(title="AMS",message="Please enter userid")
                self.t1.focus()
                return
            if len(self.txtpassword.get().strip())==0:
                messagebox.showinfo(title="AMS",message="Please enter valid password")
                self.t2.focus()
                return
            try:
                self.profileid=DBconnection.Isvaliduser(b,self.txtpassword.get().strip())
            except Exception as X:
                profileid=0

            if self.profileid>0:
                messagebox.showinfo(title='AMS',message="Sucessfully Logged in")
                self.root.destroy()
            else:
                messagebox.showerror(title='AMS',message="Invalid username or password ")
                
                
            #if username.get()=="root" and password.get()=="Tejesh":
            #   return TRUE
            #else:
            #    return FALSE   

            # b1=Button(self.root,command=lambda:login(txtusername,txtpassword),text="Login",font=(16))
          


# root=Tk()
# ob=verification(root)
# root.mainloop()