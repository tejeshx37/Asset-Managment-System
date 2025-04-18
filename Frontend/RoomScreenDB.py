from tkinter import messagebox
import DBconnection

def GetFloors(buildname):
    sql = " SELECT  project.floor_master.name as floor_name FROM project.floor_master"
    sql +=" left  JOIN project.build_master ON project.floor_master.buildingid = project.build_master.id"
    sql += " where  project.floor_master.activestatus=1 and  project.build_master.name ='"+buildname.strip()+"';"
    return DBconnection.FetchData(sql)


def getBuildID(buildname):
    sql="SELECT id FROM project.build_master where Name='"+buildname.strip()+"';"
    for building in DBconnection.FetchData(sql) :
        buildingid=building[0]
    return buildingid

def IsbuildRoomExist(Buildname,floorname,roomname,roomtype,roomsubtype):
    buildingRows=GetID(Buildname,floorname)
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):
        return False
    print(buildingid,floorid)
    sql="SELECT * FROM project.room_master "
    sql +=" where  project.room_master.buildingid='"+str(buildingid)+"'"
    sql +=" and project.room_master.floorid='"+floorid+"'"
    sql +=" and project.room_master.roomtypename='"+roomtype.strip()+"'"
    sql +=" and project.room_master.roomsubtypename='"+roomsubtype.strip()+"'"
    sql +=" and project.room_master.roomname='"+roomname.strip()+"';"

    for rows in DBconnection.FetchData(sql) :
        return True
    return False

def loadBuilding():
    sql="SELECT name FROM project.build_master order by Name asc;"
    return DBconnection.FetchData(sql)

def getRecords():
    sql="select  project.room_master.id,project.room_master.roomname,"
    sql += " project.room_master.roomtypename,project.room_master.roomsubtypename,"
    sql += " project.build_master.name AS buildname, project.floor_master.name as floorname"
    sql += " from project.room_master"
    sql += " left JOIN project.build_master ON project.room_master.buildingid = project.build_master.id"
    sql += " left JOIN project.floor_master ON  project.room_master.floorid = project.floor_master.id"
    # sql += " where project.build_master.name ='"+buildingname.strip()+"'"
    # sql += " and project.floor_master.name='"+buildingname.strip()+"'"


    return DBconnection.FetchData(sql)

def GetID(buildingname,floorname):
    sql="SELECT project.build_master.id as buildid,project.floor_master.id as floorid FROM project.build_master "
    sql +=" left JOIN project.floor_master ON project.floor_master.buildingid = project.build_master.id "
    sql +="where  project.floor_master.activestatus=1 "
    sql +="and project.build_master.name ='"+buildingname.strip()+"'"
    sql +="and project.floor_master.name='"+floorname.strip()+"';"
    return DBconnection.FetchData(sql)

def addnewrecord(buildname,floorName,roomname,roomtypename,roomsubtypename):
    bFound=False
    #To get building id and floor id
    buildingRows=GetID(buildname.strip(),floorName.strip())
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):
        return False
   
    sql="insert into project.room_master "
    sql +=" (buildingid,floorid,roomname,roomtypename,roomsubtypename)"
    sql +=" values(%s,%s,%s,%s,%s)"

    values=buildingid,floorid,roomname,roomtypename,roomsubtypename
    return DBconnection.executeTuple(sql,values)
   
def UpdateRecord(roomid,buildname,floorName,roomname,roomtypename,roomsubtypename):
    bFound=False
    #To get building id and floor id
    buildingRows=GetID(buildname.strip(),floorName.strip())
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):
        return False
    sql="update project.room_master set buildingid=%s,floorid=%s,roomname=%s,roomtypename=%s,roomsubtypename=%s  where id=%s"
    values=buildingid,floorid,roomname,roomtypename,roomsubtypename,roomid
    return DBconnection.executeTuple(sql,values)

def DeleteRecord(id):
    sql="delete from project.room_master where id="+id
    values=id
    return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    condition=" where project.room_master.roomname LIKE '%"+searchtxt+"%'"

    if (searchby=="Build Name"):
        condition=" where project.build_master.name LIKE '%"+searchtxt+"%'"
    elif (searchby=="Floor Name"):
        condition=" where project.floor_master.name LIKE '%"+searchtxt+"%'"
    elif (searchby=="Room Type"):
        condition=" where project.room_master.roomtypename LIKE '"+searchtxt+"%'"
    elif (searchby=="Room SubType"):
        condition=" where project.room_master.roomsubtypename LIKE '%"+searchtxt+"%'"

    sql="select  project.room_master.id,project.room_master.roomname,"
    sql += " project.room_master.roomtypename,project.room_master.roomsubtypename,"
    sql += " project.build_master.name AS buildname, project.floor_master.name as floorname"
    sql += " from project.room_master"
    sql += " left JOIN project.build_master ON project.room_master.buildingid = project.build_master.id"
    sql += " left JOIN project.floor_master ON  project.room_master.floorid = project.floor_master.id"
    # sql += " where project.build_master.name LIKE'"+buildingname.strip()+"'"
    # sql += " and project.floor_master.name LIKE'"+buildingname.strip()+"'"

    sql +=condition

    return DBconnection.FetchData(sql)