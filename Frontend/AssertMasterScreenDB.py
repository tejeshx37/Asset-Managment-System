from tkinter import messagebox
import DBconnection

def IsAssertExist(assertname):
    sql="Select id,Name,desc1 from  project.asset_master where Name='"+assertname.strip()+"';"
    return DBconnection.FetchData(sql)

def getRecords():
    sql="Select id,Name,desc1 from  project.asset_master;"
    return DBconnection.FetchData(sql)

def addnewrecord(assertname,assertDesc):
    sql="insert into project.asset_master(Name,desc1) values('"+assertname+"','"+assertDesc+"');"
    return DBconnection.execute(sql)
   
def UpdateBuilding(id,assertname,assertDesc):
    sql="update project.asset_master set Name=%s, desc1=%s where id=%s"
    values=assertname,assertDesc,id
    return DBconnection.executeTuple(sql,values)

def DeleteBuilding(id):
    sql="delete from project.asset_master where id="+id
    values=id
    return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    sql="select * from project.asset_master where "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    return DBconnection.FetchData(sql)