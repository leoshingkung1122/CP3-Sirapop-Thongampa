menuDict = {'Hamburgur':40,'Cheese':30,'Water':10, 'Cola':20}
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
        menuList.append([menuName.capitalize(),menuDict[menuName.capitalize()]])

print(menuList)
showBill()








