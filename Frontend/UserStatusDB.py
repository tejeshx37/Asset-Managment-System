from tkinter import messagebox
import DBconnection

def getRecords():
    sql="SELECT profileid,userid,Name,email,phoneno,case when actstatus=1 then 'Active' else 'Deactive' END as status  FROM project.profile";
    return DBconnection.FetchData(sql)

   
def UpdateStatus(id,status):
    if status=="Active":
        status=1
    else:
        status=0


    sql="update project.profile set actstatus=%s where profileid=%s"
    values=status,id
    return DBconnection.executeTuple(sql,values)

def getSearchRecord(searchby,searchtxt):
    sql="select profileid,userid,Name,email,phoneno,address from project.profile  where actstatus=1 and "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    return DBconnection.FetchData(sql)