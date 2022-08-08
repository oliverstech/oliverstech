try:
    import os
    import sys
    from os import system
except:
    pass    

try:
    import requests
except Exception:
    while True:
        e = input("Requests Module Missing, Wanna Try Auto Fix It (y/n): ")
        if e == "y" or e == "n":
            break
        else:
            print("Enter A Valid Choice")
    if e == "n":
        exit()
    if e == "y":
        try:
            os.system("pip install requests")
            print("It Should Be Fixed Now, Press Enter To Start Main Program")
            input("")
        except Exception:
            print("Error Fixing, Press Enter To Close Program")
            input("")
            exit()

cookie = sys.argv[1]
try:
    r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
    print("Cookie Is Valid")
    try:
        print("Acount User Id: " +  str(r["UserID"]))
    except Exception:
        print("Acount User Id: ERROR")
    try:
        print("Acount Username: " +  str(r["UserName"]))
    except Exception:
        print("Acount Username: ERROR")
    try:    
        print("Robux Balance: " +  str(r["RobuxBalance"]))
    except Exception:
        print("Robux Balance: ERROR")
    try:    
        print("Account Picture: " +  str(r["ThumbnailUrl"]))
    except Exception:
        print("Account Picture: ERROR")
    try:    
        print("Premium: " +  str(r["IsPremium"]))
    except Exception:
        print("Premium: ERROR")
except Exception:       
        print("Cookie Invalid")
