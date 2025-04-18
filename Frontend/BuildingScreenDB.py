from tkinter import messagebox
import DBconnection

def IsbuildExist(buildname):
    sql="Select id,Name,desc1 from  project.build_master where Name='"+buildname.strip()+"';"
    return DBconnection.FetchData(sql)

def getRecords():
    sql="Select id,Name,desc1 from  project.build_master;"
    return DBconnection.FetchData(sql)

def addnewrecord(buildName,buildDesc):
    # sql="insert into project.build_master (Name,desc1) values(%s,%s)",(buildName,buildDesc)
    # sql="insert into project.build_master(Name,desc1) values(buildName,buildDesc)";
    sql="insert into project.build_master(Name,desc1) values('"+buildName+"','"+buildDesc+"');"
    return DBconnection.execute(sql)
   
def UpdateBuilding(id,buildName,buildDesc):
    sql="update project.build_master set Name=%s, desc1=%s where id=%s"
    values=buildName,buildDesc,id
    return DBconnection.executeTuple(sql,values)

def DeleteBuilding(id):
    sql="delete from project.build_master where id="+id
    values=id
    return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    sql="select * from project.build_master where "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    return DBconnection.FetchData(sql)