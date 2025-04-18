import Menu
import verification



# import PasswordChangeScreen
# PasswordChangeScreen.ShowWindow(1,True)

# with all filters
# import ReportAbsScreen
# ReportAbsScreen.ShowWindow()

#chart
# import AbstractReport
# AbstractReport.ShowWindow(1)

# import ProfileScreen
# ProfileScreen.ShowWindow(1)

# import NewUserScreen
# NewUserScreen.ShowWindow(1)

# import UserStatus
# UserStatus.ShowWindow()

# import UserAccess
# UserAccess.ShowWindow()

# import BulidingScreen
# BulidingScreen.ShowWindow()

# import FloorScreen
# FloorScreen.ShowWindow()

# import PasswordReset
# PasswordReset.ShowWindow()

# import RoomScreen
# RoomScreen.ShowWindow()

# import AssertMasterScreen
# AssertMasterScreen.ShowWindow()

# import InwardScreen
# InwardScreen.ShowWindow()

# import DamageScreen
# DamageScreen.ShowWindow()

# import ReportAbsScreen
# ReportAbsScreen.ShowWindow()


def start():
    pid=verification.Show()
    if pid !=0 : 
        forcepwd=verification.ForeResetPassword(str(pid))
        if (forcepwd == True):
            import PasswordChangeScreen
            if PasswordChangeScreen.ShowWindow(pid,True)==True:
                Menu.showapp(pid)
            else:
                start()
        elif (pid>0):
            Menu.showapp(pid)
start()


