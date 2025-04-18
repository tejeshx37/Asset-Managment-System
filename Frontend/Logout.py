def restart():
    import Menu 
    import verification

    pid=verification.Show()
    print(pid,"Returned value")
    if pid>0:
        Menu.showapp(pid)