def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

def checkLogin():
    if login() == True:
        showMenu()
    else:
        print("Your Username or Password is incorrect")
        checkLogin()

checkLogin()
if menuSelect() == 1:
    totalPrice = float(input("Input value : "))
    print(vatCalculator(totalPrice))
else:
    print(priceCalculator())




































