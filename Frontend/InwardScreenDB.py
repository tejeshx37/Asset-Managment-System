from tkinter import messagebox
import DBconnection

def GetTypeAndSubType(roomid):
    sql="SELECT project.room_master.roomtypename,project.room_master.roomsubtypename FROM project.room_master "
    sql +=" where project.room_master.roomname='"+str(roomid)+"'"
    return DBconnection.FetchData(sql)

def GetRooms(buildname,floorname):
    buildingRows=GetID(buildname,floorname,"")
    bFound=True
    buildingid=""
    floorid=0
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):
        return False
    print(buildingid,floorid)
    sql="SELECT project.room_master.roomname FROM project.room_master "
    sql +=" where  project.room_master.buildingid='"+str(buildingid)+"'"
    sql +=" and project.room_master.floorid='"+str(floorid)+"'"
    # sql +=" and project.room_master.roomtypename='"+roomtype.strip()+"'"
    # sql +=" and project.room_master.roomsubtypename='"+roomsubtype.strip()+"'"
    # sql +=" and project.room_master.roomname='"+roomname.strip()+"';"
    return DBconnection.FetchData(sql)

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



def LoadAsset():
    sql="SELECT project.asset_master.name FROM project.asset_master order by project.asset_master.name asc;"
    return DBconnection.FetchData(sql)
   
def loadBuilding():
    sql="SELECT name FROM project.build_master order by Name asc;"
    return DBconnection.FetchData(sql)

def getRecords():
    sql =" select  project.asset_details.id,  project.asset_master.id,project.asset_master.name,project.asset_details.assetcount,"
    sql += " project.room_master.roomname,project.room_master.roomtypename,project.room_master.roomsubtypename,"
    sql += " project.build_master.name AS buildname, project.floor_master.name as floorname,"
    sql += " project.asset_details.AssetPrice as price "
    sql += "  from project.asset_details"
    sql += " left JOIN project.build_master ON project.asset_details.buildingid = project.build_master.id"
    sql += " left JOIN project.floor_master ON  project.asset_details.floorid = project.floor_master.id"
    sql += " left JOIN project.room_master ON  project.asset_details.roomid = project.room_master.id"
    sql += " left JOIN project.asset_master ON  project.asset_details.assetid = project.asset_master.id"
    sql += " where project.asset_details.damage=0;"
    return DBconnection.FetchData(sql)

def GetassetID(assertname):
    sql =" SELECT project.asset_master.id FROM project.asset_master where project.asset_master.name='"+assertname.strip()+"';"
    for row in DBconnection.FetchData(sql):
        assetid=str(row[0])
        return assetid
    return ""


def GetID(buildingname,floorname,roomid):
    sql=" SELECT  project.build_master.id as buildid,"
    sql +=" project.floor_master.id as floorid, project.room_master.id as roomid"
    sql +=" FROM project.build_master"
    sql +=" left JOIN project.floor_master ON project.floor_master.buildingid = project.build_master.id"
    sql +=" left JOIN  project.room_master ON  project.floor_master.id = project.room_master.floorid"
    sql +=" where  project.floor_master.activestatus=1"
    sql +=" and project.build_master.name ='"+buildingname.strip()+"'"
    if roomid !="":
        sql +=" and project.room_master.roomname ='"+roomid.strip()+"'"
    sql +=" and project.floor_master.name='"+floorname.strip()+"';"
    return DBconnection.FetchData(sql)

def addnewrecord(itemcnt,assetname,buildname,floorName,roomname,roomtypename,roomsubtypename,Assetprice):
    assetid=GetassetID(assetname)
    bFound=False
    #To get building id and floor id
    buildingRows=GetID(buildname,floorName,roomname)
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        roomid=str(row[2])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):  
        return False
    damage="0"
    sql="insert into project.asset_details (assetcount,buildingid,floorid,roomid,assetid,roomtypename,roomsubtypename,damage,AssetPrice) "
    sql +=" values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    bResult=False
    try:
        mc=DBconnection.getconnection()
        cr=mc.cursor()
        loopcnt= int(itemcnt)
        for icnt in range(loopcnt):
            values=str(1),buildingid,floorid,roomid,assetid,roomtypename,roomsubtypename,damage,Assetprice
            cr.execute(sql,(values))
        # d=cr.fetchall()
        bResult=True
    except Exception as X:
        bResult=False
        print(X) 
        messagebox.showerror(title="AMS",message=X)

    finally:
        if mc.is_connected():
            cr.close()
            if bResult==True:
                mc.commit()
            mc.close()
        else:
             messagebox.showerror("Some problem when with the DB")
    # print(d)
    return bResult

    # return DBconnection.executeTuple(sql,values)

def IsAssetExist(itemcnt,assetname,buildname,floorName,roomname,roomtypename,roomsubtypename):
    assetid=GetassetID(assetname)
    bFound=False
    #To get building id and floor id
    buildingRows=GetID(buildname,floorName,roomname)
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        roomid=str(row[2])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):  
        return False
    print(buildingid,floorid)
    sql="SELECT * FROM project.asset_details "
    sql +=" where  project.asset_details.buildingid='"+buildingid+"'"
    sql +=" and project.asset_details.floorid='"+floorid+"'"
    sql +=" and project.asset_details.roomid='"+roomid+"'"
    sql +=" and project.asset_details.assetid='"+assetid+"'"
    # sql +=" and project.asset_details.assetcount='"+itemcnt+"'"
    sql +=" and project.asset_details.roomtypename='"+roomtypename+"'"
    sql +=" and project.asset_details.roomsubtypename='"+roomsubtypename+"'"
    

    for rows in DBconnection.FetchData(sql) :
        return True
    return False
  
def UpdateRecord(id,assetid,itemcnt,assetname,buildname,floorName,roomname,roomtypename,roomsubtypename,itemprice):
    assetid=GetassetID(assetname)
    bFound=False
    #To get building id and floor id
    buildingRows=GetID(buildname,floorName,roomname)
    for row in buildingRows :
        buildingid=str(row[0])
        floorid=str(row[1])
        roomid=str(row[2])
        bFound=True
        break
    # if we can't able to find the id then return
    if(bFound==False):  
        return False
    # assetcount=%s
    sql=" update project.asset_details "
    sql +=" set buildingid=%s,floorid=%s,roomid=%s,assetid=%s,roomtypename=%s,roomsubtypename=%s,AssetPrice=%s"
    sql +=" where id=%s"
    values=buildingid,floorid,roomid,assetid,roomtypename,roomsubtypename,itemprice,id
    return DBconnection.executeTuple(sql,values)

def DeleteRecord(id):
    sql="delete from project.asset_details where id="+id
    return DBconnection.execute(sql)

def getSearchRecord(searchby,searchtxt):
    # condition=" where project.room_master.roomname LIKE '%"+searchtxt+"%'"

    if (searchby=="Asset ID"):
        condition=" where  project.asset_details.damage=0 and project.asset_details.id='"+searchtxt+"%'"
    elif (searchby=="Category ID"):
        condition=" where  project.asset_details.damage=0 and project.asset_master.id='"+searchtxt+"%'"
    elif (searchby=="Item Name"):
        condition=" where  project.asset_details.damage=0 and project.asset_master.name LIKE '%"+searchtxt+"%'"
    elif (searchby=="Room"):
        condition=" where  project.asset_details.damage=0 and project.room_master.roomname Like '"+searchtxt+"%'"
    elif (searchby=="Room Type"):
        condition=" where  project.asset_details.damage=0 and project.asset_details.roomtypename LIKE '%"+searchtxt+"%'"
    elif (searchby=="Room SubType"):
        condition=" where  project.asset_details.damage=0 and project.asset_details.roomsubtypename  LIKE '"+searchtxt+"%'"
    elif (searchby=="Build Name"):
        condition=" where  project.asset_details.damage=0 and project.build_master.name  LIKE '%"+searchtxt+"%'"
    elif (searchby=="Floor Name"):
        condition=" where  project.asset_details.damage=0 and project.floor_master.name  LIKE '%"+searchtxt+"%'"


    sql =" select  project.asset_details.id,  project.asset_master.id,project.asset_master.name,project.asset_details.assetcount,"
    sql += " project.room_master.roomname,project.room_master.roomtypename,project.room_master.roomsubtypename,"
    sql += " project.build_master.name AS buildname, project.floor_master.name as floorname,"
    sql += " project.asset_details.AssetPrice as price "
    sql += "  from project.asset_details"
    sql += " left JOIN project.build_master ON project.asset_details.buildingid = project.build_master.id"
    sql += " left JOIN project.floor_master ON  project.asset_details.floorid = project.floor_master.id"
    sql += " left JOIN project.room_master ON  project.asset_details.roomid = project.room_master.id"
    sql += " left JOIN project.asset_master ON  project.asset_details.assetid = project.asset_master.id"


    sql +=condition

    return DBconnection.FetchData(sql)