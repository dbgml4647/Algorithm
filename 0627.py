#6
def CheckFalse(): 
    a=[None,1,"",0,bool(0)]
    for i in a:
        if i == True: 
            print ("This is True")
        else:
            print("This is False")

CheckFalse()