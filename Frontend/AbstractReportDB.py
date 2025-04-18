from tkinter import messagebox
import DBconnection

def GetAbtDetails():
    # sql=" select   sum( case when project.asset_details.damage=0  then AssetPrice else 0 end ) as InUse from project.asset_details  "
    # sql +=" group  by project.asset_details.damage "
    # sql +=" union "
    # sql +=" select   sum( case when project.asset_details.damage=1  then AssetPrice else 0 end ) as Damage from project.asset_details "  
    # sql +=" group  by project.asset_details.damage;" 

    sql=" select   sum( case when project.asset_details.damage=0 then AssetPrice else 0 end ) as InUse "
    sql +=" , sum( case when project.asset_details.damage=1    then AssetPrice else 0 end ) as Damage  "
    sql +=" from project.asset_details  group by project.asset_details.damage ;"

    
    return DBconnection.FetchData(sql)
