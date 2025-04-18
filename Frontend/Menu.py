from tkinter import Toplevel, Button, Tk, Menu 
from tkinter import messagebox
import time
import helpdlg
import verification
import DBconnection

# import Logout

from tkinter import *

def showapp(pid):
   root=Tk()
   ob=LandingScreen(root)
   ob.pid=pid
   # root.mainloop()
   ob.showapp()
   return 
   
   
 

class LandingScreen:

   def __init__(self,root):
      self.root=root
      self.root.title('AMS')
      #============= All Variables ============
      self.pid=StringVar()

   def onclickInward(self):
      pid=self.pid
      self.root.destroy()
      import InwardScreen
      InwardScreen.ShowWindow()
      showapp(pid)
      return   
   
   def onclickabsreport(self):
      pid=self.pid
      self.root.destroy()
      import ReportAbsScreen
      ReportAbsScreen.ShowWindow()
      # import AbstractReport
      # AbstractReport.ShowWindow(pid)
      showapp(pid)
      return
   
   def onclickCostAbstractReport(self):
      pid=self.pid
      self.root.destroy()
      import AbstractReport
      AbstractReport.ShowWindow(1)
      showapp(pid)
      return
   def onclickDamage(self):
      pid=self.pid
      self.root.destroy()
      import DamageScreen
      DamageScreen.ShowWindow()
      showapp(pid)
      return
   
   def onclickassertmaster(self):
      pid=self.pid
      self.root.destroy()
      import AssertMasterScreen
      AssertMasterScreen.ShowWindow()
      showapp(pid)
      return 

   def onclickRoom(self):
      pid=self.pid
      self.root.destroy()
      import RoomScreen
      RoomScreen.ShowWindow()
      showapp(pid)
      return 
   

   def onclickfloor(self):
      pid=self.pid
      self.root.destroy()
      import FloorScreen
      FloorScreen.ShowWindow()
      showapp(pid)
      return 

   def onclickbuliding(self):  
      pid=self.pid
      self.root.destroy()
      import BulidingScreen
      BulidingScreen.ShowWindow()
      showapp(pid)
      # messagebox.showinfo(title="AMS",message="This menu is working in progress")
      return 
   
   def onCreateNewUser(self):
      pid=self.pid
      self.root.destroy()
      import NewUserScreen
      NewUserScreen.ShowWindow(1)
      showapp(pid)
      return
   
   def onUserReset(self):
      pid=self.pid
      self.root.destroy()
      import PasswordReset
      PasswordReset.ShowWindow()
      showapp(pid)
      return
   
   def onUserstatus(self):
      pid=self.pid
      self.root.destroy()
      import UserStatus
      UserStatus.ShowWindow()
      showapp(pid)
      return
   
   def onUserAccess(self):
      pid=self.pid
      self.root.destroy()
      import UserAccess
      UserAccess.ShowWindow()
      showapp(pid)
      return
   
   def onMyDetails(self):
      pid=self.pid
      self.root.destroy()
      import ProfileScreen
      ProfileScreen.ShowWindow(pid)
      showapp(pid)
      return
   
   def onChangePassword(self):
      pid=self.pid
      self.root.destroy()
      import PasswordChangeScreen
      PasswordChangeScreen.ShowWindow(pid,False)
      showapp(pid)
      return
   
   def onhelp(self):
      helpdlg.hlp()
      return 

   def onclickprofile(self):
      messagebox.showinfo(title="AMS",message="This menu is working in progress")  
      return 
   
   

   def logout(self):
      answer = messagebox.askyesno(title='confirmation', message='Are you sure want to logout?')
      if answer: 
         self.root.destroy()
         import AMS
         AMS.start()
         
         # import Menu 
         # import verification

         # pid=verification.Show()
         # print(pid,"Returned value")
         # if pid>0:
         #    self.pid
         #    Menu.showapp(pid)
         # import Logout
         # Logout.logout()
      

   def showapp(self):
      # tkWindow = Tk()  
      # tkWindow.title('AMS')
      bg=PhotoImage(file="D:\\Wallpaper\\sample.png")
      mylabel=Label(self.root,image=bg)
      mylabel.place(x=0,y=0,relwidth=1,relheight=1)
      menubar=Menu(self.root)
      Mlist=DBconnection.getmenus(self.pid)

      masters = Menu(menubar, tearoff=0)
      transcation= Menu(menubar, tearoff=0)
      report = Menu(menubar, tearoff=0)
      useraccessMenu = Menu(menubar, tearoff=0)
      adminMenu = Menu(menubar, tearoff=0)

      flagreport=False
      flagtranscation=False
      flagmaster=False
      flagAdmin=False

      for i in range(0,len(Mlist)):
         if Mlist[i][1]=="Building":
            masters.add_command(label="Building",command=self.onclickbuliding)
            flagmaster=True
         elif Mlist[i][1]=="Floor":
            masters.add_command(label="Floor",command=self.onclickfloor)
            flagmaster=True 
         elif Mlist[i][1]=="Room":
            masters.add_command(label="Room",command=self.onclickRoom)
            flagmaster=True  
         elif Mlist[i][1]=="Type of asset":
            masters.add_command(label="Asset Master",command=self.onclickassertmaster) 
            flagmaster=True
         

         elif Mlist[i][1]=="New User":
            adminMenu.add_command(label="New User Account",command=self.onCreateNewUser)
            flagAdmin=True 
         elif Mlist[i][1]=="User access":
            adminMenu.add_command(label="Grand / Revoke Access",command=self.onUserAccess)
            flagAdmin=True 
         elif Mlist[i][1]=="User Status":
            adminMenu.add_command(label="User Activate / Deactive ",command=self.onUserstatus)
            flagAdmin=True 
         elif Mlist[i][1]=="Password Reset":
            adminMenu.add_command(label="Password Reset",command=self.onUserReset)
            flagAdmin=True 

         
         elif Mlist[i][1]=="Inwards":
            
            transcation.add_command(label="Inward Entry",command=self.onclickInward) 
            flagtranscation=True
            transcation.add_separator()  
         elif Mlist[i][1]=="Damage":
            transcation.add_command(label="Damage Entry ",command=self.onclickDamage)
            flagtranscation=True  
            

         else:
            if Mlist[i][1]=="Abstract Details":
               report.add_command(label="360° Abstract Report",command=self.onclickabsreport)
               flagreport=True
            elif Mlist[i][1]=='Asset Cost Abstract Report':
               report.add_command(label="Asset Cost Abstract Report",command=self.onclickCostAbstractReport)
               flagreport=True
               


      profile=Menu(menubar,tearoff=0)
      profile.add_command(label="My Details",command=self.onMyDetails)
      profile.add_separator()  
      profile.add_command(label="Change Password",command=self.onChangePassword)
      profile.add_separator()
      profile.add_command(label="Log Out", command=self.logout)
      menubar.add_cascade(label="Profile",menu=profile)

      if flagmaster:
         menubar.add_cascade(label="Masters", menu=masters)
      help = Menu(menubar, tearoff=0) 

      if flagreport:
         menubar.add_cascade(label="Report", menu=report) 
  


      if flagtranscation:
         menubar.add_cascade(label="Transcations", menu=transcation) 

      if flagAdmin:
         menubar.add_cascade(label="Admin", menu=adminMenu) 
      
      # useraccessMenu.add_command(label="New User",command=self.onCreateNewUser)
      # useraccessMenu.add_separator()  

      # useraccessMenu.add_command(label="User Status",command=self.onUserstatus)
      # useraccessMenu.add_separator()

      # useraccessMenu.add_command(label="User Password Reset",command=self.onUserReset)
      # useraccessMenu.add_separator()
      
      # useraccessMenu.add_command(label="User Access", command=self.onUserAccess)
      # menubar.add_cascade(label="Admin",menu=useraccessMenu)

      help.add_command(label="About",command=self.onhelp)  
      menubar.add_cascade(label="Help", menu=help)
      
      self.root.config(menu=menubar)
      self.root.state(newstate='zoomed')  

      self.root.mainloop()

      
   # root=Tk()
   # ob=LandingScreen(root)
   # root.mainloop()
