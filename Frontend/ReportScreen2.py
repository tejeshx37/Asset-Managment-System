from tkinter import *





def ShowWindow():
    rootReport=Tk()
    ob=ReportScreen(rootReport)
    ob.ShowControl()
    rootReport.mainloop()
    
class ReportScreen:
    
    def __init__(self,root):
        
        self.root=root
        root.title("AMS - Report")
        root.geometry("1350x700+0+0")
        root.state(newstate='zoomed')  
 
        title=Label(root,text="Report SCREEN",font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        title.pack(side=TOP,fill=X)
    
    def ShowControl(self):

        RIGHT_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="darkblue")
        RIGHT_Frame.place(x=3,y=60,width=1360,height=643)

        



    

ShowWindow()