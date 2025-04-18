import mysql.connector as ms
from tkinter import messagebox
Hostname='127.0.0.1'
Username='root'
Password="Tejeshsms@Mithra"
Database="project"

def GrantAccess(menuidList,profileID):
    bResult=False
    try:
        mc=getconnection()
        cr=mc.cursor()
        sql=" delete from project.menuaccess where project.menuaccess.profileid='"+profileID+"';"
        cr.execute(sql)
        for menuid in menuidList:
            print(menuid,profileID)
            menustr=str(menuid)
            sql="insert into project.menuaccess (project.menuaccess.menuid,project.menuaccess.profileid)"
            sql +=" values('"+menustr+"','"+profileID+"');"
            cr.execute(sql)
        bResult=True
    except Exception as X:
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
    return bResult

def ForeResetPassword(profileid):
    sql="select project.profile.resetpwd FROM project.profile  where project.profile.resetpwd=1 and project.profile.profileid='"+profileid+"';"
    return FetchData(sql)

def getconnection():
    mc=ms.connect(host=Hostname,user=Username,passwd=Password,database=Database,auth_plugin='mysql_native_password')
    #cr=mc.cursor()
    return mc
   

def Isvaliduser(a,s):
    sql="select profileid from profile where userid='"+a+"' and paswd='"+s+"' and actstatus=1;"
    #sql="select name from profile where userid='"
    #+a
    #+"' and paswd='"
    #+s
    #+"' and actstatus=1;"
    mc=''
    try:
        #mc=ms.connect(host=Hostname,user=Username,passwd=Password,database=Database,auth_plugin='mysql_native_password')
        mc=getconnection()
        cr=mc.cursor()
        cr.execute(sql)
        h=cr.fetchone()
        w=cr.rowcount
        # if more than one record donot allow to login
        if w>1 :
            v=0
        if h==None:
            v=0
        else:
            v=h[0]
    
    except Exception as X:
        print(X)   
        messagebox.showerror(title="AMS",message=X)
        
        
    finally:
        if mc.is_connected():
            cr.close()
            mc.close()
        else:
             messagebox.showerror("Some problem when with the DB")
    if v>1:
       return v
    else:
        return v
    
def FetchData(sql):
    d=''
    try:
        mc=getconnection()
        cr=mc.cursor()
        cr.execute(sql)
        d=cr.fetchall()
       
    except Exception as X:
        d=''
        print(X) 
        messagebox.showerror(title="AMS",message=X)

    finally:
        if mc.is_connected():
            cr.close()
            # if bResult==True:
                # mc.commit()
            mc.close()
        else:
             messagebox.showerror("Some problem when with the DB")
    # print(d)
    return d

def executeTuple(sql,values):
    bResult=False
    try:
        mc=getconnection()
        cr=mc.cursor()
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
  
def execute(sql):
    bResult=False
    try:
        mc=getconnection()
        cr=mc.cursor()
        cr.execute(sql)
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

def getmenus(id):
    sql="select menudetails.menuid,menudetails.menuname from menuaccess,menudetails where menuaccess.menuid=menudetails.menuid and profileid="+str(id)+";"
    try:
        mc=getconnection()
        cr=mc.cursor()
        cr.execute(sql)
        d=cr.fetchall()
    except Exception as X:
        print(X) 
        messagebox.showerror(title="AMS",message=X)
        
    finally:
        if mc.is_connected():
            cr.close()
            mc.close()
        else:
             messagebox.showerror("Some problem when with the DB")
    print(d)
    return d