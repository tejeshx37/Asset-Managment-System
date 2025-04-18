from tkinter import messagebox
import DBconnection

def getProfileDetails(userid):
    sql="SELECT userid,Name,email,phoneno,address FROM project.profile where profileid="+ str(userid)
    return DBconnection.FetchData(sql)
