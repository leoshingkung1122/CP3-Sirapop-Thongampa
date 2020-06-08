menuList = []
totalCost = 0

def showBill():
    totalCost = 0
    print("Bill".center(20,"-"))
    for x in range(len(menuList)):
        print(menuList[x][0],"cost  :",menuList[x][1])
        totalCost += menuList[x][1]
    print("Total Price : ",totalCost)


while True:
    menuName = input("Order the food : ")
    if menuName.casefold() == "exit":
        break
    else:
        menuPrice = int(input("Price (Bath) : "))
        menuList.append([menuName,menuPrice])



showBill()








