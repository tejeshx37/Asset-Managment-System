from tkinter import messagebox
import DBconnection

def GetMenus():
    sql="select menudetails.menuid,menudetails.menuname from project.menudetails  where menudetails.activestatus=1"
    return DBconnection.FetchData(sql)

def GetUserProfileid(searchby,searchVal):
    condition=" where project.profile.actstatus=1 and project.profile.userid='"+searchVal+"';"
    if(searchby == "Name"):
        condition=" where project.profile.actstatus=1 and project.profile.Name='"+searchVal+"';"
        
    sql="select project.profile.profileid FROM project.profile "
    sql +=condition
    for profileid in DBconnection.FetchData(sql) :
        return profileid[0]
    return -1
   


def GetUserMenu(profileid):
    sql="select menudetails.menuid,menudetails.menuname from project.menudetails "
    sql += " left JOIN project.menuaccess ON project.menudetails.menuid = project.menuaccess.menuid"
    sql += " where project.menudetails.activestatus=1 and project.menuaccess.profileid="+str(profileid)
    return DBconnection.FetchData(sql)
