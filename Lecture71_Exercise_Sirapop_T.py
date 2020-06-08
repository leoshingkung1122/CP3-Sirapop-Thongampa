menuList = []
costList = []
totalCost = 0

def showBill():
    totalCost = 0
    print("Bill".center(20,"-"))
    for x in range(len(menuList)):
        print(menuList[x],"cost    :",costList[x])
    for y in range(len(costList)):
        totalCost += costList[y]
    print("Total Price :",totalCost)


while True:
    menuName = input("Order the food : ")
    if menuName.casefold() == "exit":
        break
    else:
        menuPrice = int(input("Price (Bath) : "))
        menuList.append(menuName)
        costList.append(menuPrice)


showBill()








