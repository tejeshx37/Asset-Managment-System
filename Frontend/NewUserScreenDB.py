from tkinter import messagebox
import DBconnection

def IsUserExist(userid):
    sql="SELECT userid FROM project.profile where userid='"+userid.strip()+"';"
    return DBconnection.FetchData(sql)

def getRecords():
    sql="SELECT profileid,userid,Name,email,phoneno,address FROM project.profile where actstatus=1";
    return DBconnection.FetchData(sql)

def addnewrecord(password,userid,username,emailid,phone,address):
    sql="insert into project.profile(Name,address,email,phoneno,userid,paswd) "
    sql +=" values(%s,%s,%s,%s,%s,%s);"
    values=username,address,emailid,phone,userid,password
    return DBconnection.executeTuple(sql,values)
   
def UpdateUser(id,username,emailid,phone,address):
    sql="update project.profile set Name=%s,email=%s,phoneno=%s,address=%s where profileid=%s"
    # phonenumber=int(phone)
    values=username,emailid,phone,address,id
    return DBconnection.executeTuple(sql,values)

# def DeleteBuilding(id):
#     sql="delete from project.build_master where id="+id
#     values=id
#     return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    sql="select profileid,userid,Name,email,phoneno,address from project.profile  where actstatus=1 and "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    return DBconnection.FetchData(sql)