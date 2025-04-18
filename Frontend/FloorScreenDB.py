from tkinter import messagebox
import DBconnection




def getBuildID(buildname):
    sql="SELECT id FROM project.build_master where Name='"+buildname.strip()+"';"
    for building in DBconnection.FetchData(sql) :
        buildingid=building[0]
    return buildingid

def IsbuildFloorExist(Buildname,floorname):
    buildingid=getBuildID(Buildname.strip())
    print(buildingid)
    sql="SELECT * FROM project.floor_master "
    sql +=" where project.floor_master.buildingid='"+str(buildingid)+"'"
    sql +=" and project.floor_master.name='"+floorname.strip()+"';"
    for rows in DBconnection.FetchData(sql) :
        return True
    return False

def loadBuilding():
    sql="SELECT name FROM project.build_master order by Name asc;"
    return DBconnection.FetchData(sql)

def getRecords():
    # sql="SELECT * FROM project.floor_master order by Name asc;"
    sql="SELECT project.floor_master.id,project.build_master.name as building_name,project.floor_master.name as floor_name,project.floor_master.description,project.floor_master.activestatus FROM project.floor_master LEFT JOIN project.build_master ON project.floor_master.buildingid = project.build_master.id;"

    return DBconnection.FetchData(sql)

   
def addnewrecord(buildname,floorName,floorDesc):
    buildingid=getBuildID(buildname.strip())
   

    sql="insert into project.floor_master(buildingid,name,description,activestatus) values(%s,%s,%s,%s)";
    values=buildingid,floorName.strip(),floorDesc.strip(),1
    # return DBconnection.execute(sql)
    return DBconnection.executeTuple(sql,values)

   
def UpdateRecord(floorid,buildingname,floorname,buildDesc):
    buildingid=getBuildID(buildingname.strip())
    sql="update project.floor_master set buildingid=%s,Name=%s, description=%s where id=%s"
    values=buildingid,floorname.strip(),buildDesc.strip(),floorid
    return DBconnection.executeTuple(sql,values)

def DeleteRecord(id):
    sql="delete from project.floor_master where id="+id
    values=id
    return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    condition=" where project.floor_master.name LIKE '%"+str(searchtxt)+"%'"
    if (searchby=="Build Name"):
        condition=" where project.build_master.name LIKE '%"+str(searchtxt)+"%'"


    # sql="select * from project.floor_master where "+ str(searchby)+" LIKE '%"+str(searchtxt)+"%'"
    sql="SELECT project.floor_master.id,project.build_master.name as building_name,"
    sql +=" project.floor_master.name as floor_name,"
    sql +=" project.floor_master.description,project.floor_master.activestatus"
    sql +=" FROM project.floor_master"
    sql +=" left  JOIN project.build_master"
    sql +=" ON project.floor_master.buildingid = project.build_master.id"
    # sql +="where project.build_master.name LIKE '%Building'"
    sql +=condition

    return DBconnection.FetchData(sql)