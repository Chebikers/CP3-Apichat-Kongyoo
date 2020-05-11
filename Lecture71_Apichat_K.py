menuList = []
priceList = []
def showBill():
    print("-----MoMo Food-----")
    for number in range(len(menuList)):
        print(number+1,"." ,menuList[number],priceList[number] ,"THB")
        sum = 0
        for price in priceList:
            sum += int(price)
    print("Total Menu  :" ,len(menuList) ,"\nTotal price :",sum ,"THB" ,"\n-----Thank You-----")

while True:
    menuName = input("Please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please enter price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
