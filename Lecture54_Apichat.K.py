def login():
    usernameInput = input("UserName :")
    passwordInput = input("password :")
    if usernameInput == "Apichat" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("-----Welcome to MoMo Shop----- ")
    print("------Please enter price------ ")
def selectMenu():
    print("1.Price (No Vat)")
    print("2.Price (Include Vat)")
    userSelected = int(input("-----Please Select for Show Price-----"))
    return userSelected
def calcurateVat(totalPrice):
    vat = 7
    return totalPrice + (totalPrice * vat / 100)
def noVat(total):
    total = (price1 + price2)
    return total
def calcuratePrice(price1, price2):
    return calcurateVat(price1 + price2)
if login():
    showMenu()
    price1 = int(input("First product price (THB):"))
    price2 = int(input("Second product price (THB):"))
    menu = selectMenu()
    if menu == 1:
        print("Price :" ,noVat(noVat) ,"(THB)")
    elif menu == 2:
        print("Price Include Vat :",calcuratePrice(price1, price2) ,"(THB)")
else:
    print("Wrong password please try again")