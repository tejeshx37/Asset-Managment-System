from tkinter import messagebox
import DBconnection

def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return substring + s[:-amount]

def right(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[-amount:]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return s[:-amount] + substring
    
def BuildingID(buildingname):
    sql=" SELECT  project.build_master.id from project.build_master where  project.build_master.name = '"+buildingname.strip()+"';"
    for row in DBconnection.FetchData(sql):
        builiding=str(row[0])
        return builiding
    return "1"

def GetFloorIDS(floorname):
    sql=" select id from project.floor_master where name like '"+floorname.strip()+"%';"
    result=""
    for row in DBconnection.FetchData(sql):
        result +=(str(row[0]))
        result+=","
    result=left(result,len(result)-1)
    return result

def GetRoomID(roomname):
    sql=" select id from project.room_master  where roomname='"+roomname.strip()+"'"
    for row in DBconnection.FetchData(sql):
        roomid=str(row[0])
        return roomid
    return "1"

def GetassetID(assertname):
    sql =" SELECT project.asset_master.id FROM project.asset_master where project.asset_master.name='"+assertname.strip()+"';"
    for row in DBconnection.FetchData(sql):
        assetid=str(row[0])
        return assetid
    return ""

def GetBuildingAndFloorID(buildingname,floorname):
    sql=" SELECT project.floor_master.id as floorid "
    sql +=" FROM project.build_master"
    sql +=" left JOIN project.floor_master ON project.floor_master.buildingid = project.build_master.id"
    sql +=" left JOIN  project.room_master ON  project.floor_master.id = project.room_master.floorid"
    sql +=" where  project.floor_master.activestatus=1"
    sql +=" and project.build_master.name ='"+buildingname.strip()+"'"
    sql +=" and project.floor_master.name='"+floorname.strip()+"';"
    for row in DBconnection.FetchData(sql):
        floorid=str(row[0])
        return floorid

def GetChart(txtBuildname,txtFloorname,txtRoomname ,txtassetname,txtRoomTypename,txtRoomSubTypename):
    sql=" SELECT project.asset_master.name, count(project.asset_master.id) FROM project.asset_details "
    sql +=" left JOIN project.asset_master ON project.asset_master.id = project.asset_details.assetid"
    sql +=" where project.asset_details.activestatus=1 and project.asset_details.damage=0"
    # if txtBuildname== "All" and txtFloorname== "All" and txtRoomname== "All" and txtassetname== "All" and txtRoomTypename== "All" and txtRoomSubTypename== "All" :
    #     sql+=""
    # elif txtBuildname!= "All" and txtFloorname== "All" and txtRoomname== "All" and txtassetname== "All" and txtRoomTypename== "All" and txtRoomSubTypename== "All" :
    #     sql +=" and project.asset_details.buildingid='"+BuildingID(txtBuildname)+"'"

    if txtBuildname!= "All" :
        sql +=" and project.asset_details.buildingid='"+BuildingID(txtBuildname)+"'"

    if txtFloorname!= "All" and  txtBuildname== "All":
        sql +="  and project.asset_details.floorid in ("+str(GetFloorIDS(txtFloorname)) +")"
    elif txtFloorname!= "All" and  txtBuildname!= "All":
        sql +="  and project.asset_details.floorid in ("+str(GetBuildingAndFloorID(txtBuildname,txtFloorname)) +")"

    if txtRoomname!= "All" :
        sql +="  and project.asset_details.roomid='"+GetRoomID(txtRoomname)+"'"
    if txtassetname!= "All" :
        sql +="  and project.asset_details.assetid='"+GetassetID(txtassetname)+"'"
    if txtRoomTypename!= "All" :
        sql +=" and project.asset_details.roomtypename='"+txtRoomTypename.strip()+"'"
    if txtRoomSubTypename!= "All" :
        sql +=" and project.asset_details.roomsubtypename='"+txtRoomSubTypename.strip()+"'"

    sql +=" group by project.asset_master.id order by project.asset_master.name asc;"
    return DBconnection.FetchData(sql)

def LoadRoomSubType(roomtypename):
    sql=" SELECT distinct(roomsubtypename ) FROM project.room_master "
    if roomtypename !="All" :
        sql +=" where roomtypename = '"+str(roomtypename)+"'"
    return DBconnection.FetchData(sql)

def GetFloors(buildname):
    sql = " SELECT  distinct(project.floor_master.name) as floor_name  FROM project.floor_master"
    sql +=" left  JOIN project.build_master ON project.floor_master.buildingid = project.build_master.id"
    sql += " where  project.floor_master.activestatus=1 "
    if buildname !="All" :
         sql += " and  project.build_master.name ='"+buildname.strip()+"';"
    return DBconnection.FetchData(sql)

def GetID(buildingname,floorname):
    sql=" SELECT  project.build_master.id as buildid,"
    sql +=" project.floor_master.id as floorid, project.room_master.id as roomid"
    sql +=" FROM project.build_master"
    sql +=" left JOIN project.floor_master ON project.floor_master.buildingid = project.build_master.id"
    sql +=" left JOIN  project.room_master ON  project.floor_master.id = project.room_master.floorid"
    sql +=" where  project.floor_master.activestatus=1"
    sql +=" and project.build_master.name ='"+buildingname.strip()+"'"
    sql +=" and project.floor_master.name='"+floorname.strip()+"';"
    return DBconnection.FetchData(sql)

def GetRooms(buildname,floorname):
    bFound=True
    sql="SELECT project.room_master.roomname FROM project.room_master "
    if buildname!="All":
        buildingRows=GetID(buildname,floorname)     
        buildingid=""
        floorid=0
        for row in buildingRows :
            buildingid=str(row[0])
            floorid=str(row[1])
            bFound=True
            break
        # print(buildingid,floorid)
        sql +=" where  project.room_master.buildingid='"+str(buildingid)+"'"
        sql +=" and project.room_master.floorid='"+str(floorid)+"'"
    else:
        sql +="  where  project.room_master.floorid in ("+str(GetFloorIDS(floorname)) +")"
    # if we can't able to find the id then return
    if(bFound==False):
        return False
   
    
    
    # sql +=" and project.room_master.roomtypename='"+roomtype.strip()+"'"
    # sql +=" and project.room_master.roomsubtypename='"+roomsubtype.strip()+"'"
    # sql +=" and project.room_master.roomname='"+roomname.strip()+"';"
    return DBconnection.FetchData(sql)
def loadBuilding():
    sql="SELECT name FROM project.build_master order by Name asc;"
    return DBconnection.FetchData(sql)

