print("---------------------------")
print("Welcome to Waifu Model Shop")
print("---------------------------")
userInput = input("Username : ")
passInput = input("Password : ")
if userInput == "customer1" and passInput == "waifushop" :
    print("---------------------------")
    print("You have logged in successfully")
    print("---------------------------")
    print("--Select your Service--")
    print("---------------------------")
    print("1) Go to Model Shop")
    print("2) Go to Stationery&Appliance")
    print("3) H (Adult zone!!!)")
    print("4) Contact us")
    print("-------Please be noted input only an integer following the list-------")
    menuInput = int(input("Please select the Menu : "))
    if menuInput == 1:
        print("--Select your Waifu--")
        print("1) Megumin Figure      x1  : 500 Bath")
        print("2) Yami    Figure      x1  : 550 Bath")
        print("3) Touhou Reimu Figure x1  : 999 Bath")
        print("---------------------------------------------------------------------")
        megumin = int(input("How many Megumin Figure to putting in the cart: "))
        yami    = int(input("How many Yami to putting in the cart          : "))
        reimu   = int(input("How many Touhou Reimu to putting in the cart  : "))
        megumin = megumin*500
        yami    = yami*550
        reimu   = reimu*999
        figureCost = megumin + yami +reimu
        print("---------------------------------------------------------------------")
        print("Total Cost :",figureCost,"Bath")
        print("---------------------------")
        print("--Select your Service transportation--")
        print("---------------------------")
        print("1) EMS                                   : 45   Bath")
        print("2) Airjet Speed                          : 900  Bath")
        print("3) Shop owner come to your destination   : 2000 Bath")
        print("-------Please be noted input only an integer following the list-------")
        transportInput = int(input("Please select the Transportation : "))
        address = input("Please inform you item destination : ")
        if transportInput == 1:
            transportCost = 45
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + figureCost, "Bath")
            print("Your item destination is :",address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")
        if transportInput == 2:
            transportCost = 900
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + figureCost, "Bath")
            print("Your item destination is :", address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")
        if transportInput == 3:
            transportCost = 2000
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + figureCost, "Bath")
            print("Your item destination is :", address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")

    if menuInput == 2:
        print("--Select your Appliance--")
        print("1) เสื้อลายพี่โต(Ricardo Shirt)  x1  : 300 Bath")
        print("2) ผ้าโพกหัวพี่โต(Ricardo Cap)   x1  : 150 Bath")
        print("3) Reimu T-Shirt             x1  : 350 Bath")
        print("4) Annonymous Mask           x1  : 400 Bath")
        print("---------------------------------------------------------------------")
        pToShirt       = int(input("How many เสื้อลายพี่โต(Ricardo Shirt) to putting in the cart : "))
        pToCap         = int(input("How many ผ้าโพกหัวพี่โต(Ricardo Cap) to putting in the cart : "))
        reimuShirt     = int(input("How many Reimu T-Shirt to putting in the cart           : "))
        annonymousMask = int(input("How many Annonymous Mask to putting in the cart         : "))
        pToShirt = pToShirt*300
        pToCap   = pToCap*150
        reimuShirt = reimuShirt*350
        annonymousMask = annonymousMask*400
        applianceCost = pToShirt + pToCap + reimuShirt + annonymousMask
        print("---------------------------------------------------------------------")
        print("Total Cost :", applianceCost, "Bath")
        print("---------------------------")
        print("--Select your Service transportation--")
        print("---------------------------")
        print("1) EMS                                   : 45   Bath")
        print("2) Airjet Speed                          : 900  Bath")
        print("3) Shop owner come to your destination   : 2000 Bath")
        print("-------Please be noted input only an integer following the list-------")
        transportInput = int(input("Please select the Transportation : "))
        address = input("Please inform you item destination : ")
        if transportInput == 1:
            transportCost = 45
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + applianceCost, "Bath")
            print("Your item destination is :", address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")
        if transportInput == 2:
            transportCost = 900
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + applianceCost, "Bath")
            print("Your item destination is :", address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")
        if transportInput == 3:
            transportCost = 2000
            print("---------------------------------------------------------------------")
            print("Total cost :", transportCost + applianceCost, "Bath")
            print("Your item destination is :", address)
            print("---------------------------------------------------------------------")
            print("Thank you for shopping")

    if menuInput == 3:
        adultAge = float(input(" What is your age ? : "))
        if adultAge >= 18:
            print("--Select your H-Item--")
            print("1) H-Dojin         x1  : 100 Bath")
            print("2) H-DVD           x1  : 299 Bath")
            print("3) H-Anime Poster  x1  : 350 Bath")
            print("---------------------------------------------------------------------")
            hDojin  = int(input("How many H-Dojin to putting in the cart         : "))
            hDvd    = int(input("How many H-DVD  to putting in the cart          : "))
            hPoster = int(input("How many H-Anime Poster to putting in the cart  : "))
            hDojin  = hDojin*100
            hDvd    = hDvd*299
            hPoster = hPoster*350
            hItemCost = hDojin + hDvd + hPoster
            print("---------------------------------------------------------------------")
            print("Total Cost :", hItemCost, "Bath")
            print("---------------------------")
            print("--Select your Service transportation--")
            print("---------------------------")
            print("1) EMS                                   : 45   Bath")
            print("2) Airjet Speed                          : 900  Bath")
            print("3) Shop owner come to your destination   : 2000 Bath")
            print("-------Please be noted input only an integer following the list-------")
            transportInput = int(input("Please select the Transportation : "))
            address = input("Please inform you item destination : ")
            if transportInput == 1:
                transportCost = 45
                print("---------------------------------------------------------------------")
                print("Total cost :", transportCost + hItemCost, "Bath")
                print("Your item destination is :", address)
                print("---------------------------------------------------------------------")
                print("Thank you for shopping")
            if transportInput == 2:
                transportCost = 900
                print("---------------------------------------------------------------------")
                print("Total cost :", transportCost + hItemCost, "Bath")
                print("Your item destination is :", address)
                print("---------------------------------------------------------------------")
                print("Thank you for shopping")
            if transportInput == 3:
                transportCost = 2000
                print("---------------------------------------------------------------------")
                print("Total cost :", transportCost + hItemCost, "Bath")
                print("Your item destination is :", address)
                print("---------------------------------------------------------------------")
                print("Thank you for shopping")
        else:
            print("---------------------------------------------------------------------")
            print("Your age is less than 18 you can not entry this zone")
    if menuInput == 4:
        print("---------------------------------------------------------------------")
        print("Please contact to Waifushop112@gmail0com")
        print("Call-center : 09-9999-9999")
        print("---------------------------------------------------------------------")
else:
    print("---------------------------")
    print("Your Username or Password is incorrect")
    print("---------------------------")
