from tkinter import messagebox
import DBconnection

def UpdatePassword(userid,oldpwd,newpwd):
    sql="select  project.profile.userid from project.profile where project.profile.paswd='"+oldpwd+"'"
    bOldpwdExist=False
    for row in DBconnection.FetchData(sql) :
       bOldpwdExist=True
   
    if bOldpwdExist==False:
        return False
    
    forceResetpwd="0"
    sql="update project.profile  set project.profile.paswd=%s,project.profile.resetpwd=%s "
    sql +="where project.profile.profileid=%s and project.profile.paswd=%s;"
    values=newpwd,forceResetpwd,userid,oldpwd
    return DBconnection.executeTuple(sql,values)

def GetDetails(profileid):
    try:
        sql="select  project.profile.userid,project.profile.name from project.profile where project.profile.profileid='"+profileid+"';"
        print(sql) 
    except Exception as X:
        d=''
        print(X) 
    return DBconnection.FetchData(sql)