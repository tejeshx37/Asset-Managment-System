from tkinter import messagebox
import DBconnection

def getRecords():
    sql="SELECT profileid,userid,Name,email,phoneno,case when actstatus=1 then 'Active' else 'Deactive' END as status  FROM project.profile where actstatus=1";
    return DBconnection.FetchData(sql)

   
def UpdateStatus(id,newPwd):
    resetPwd="1"
    sql="update project.profile set paswd=%s, resetpwd=%s where actstatus=1 and profileid=%s"
    values=newPwd,resetPwd,id
    return DBconnection.executeTuple(sql,values)

def getSearchRecord(searchby,searchtxt):
    sql="select profileid,userid,Name,email,phoneno,address from project.profile  where actstatus=1 and "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    return DBconnection.FetchData(sql)