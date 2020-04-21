usernameInput = input("UserName :")
passwordInput = input("password :")
if usernameInput == "Apichat" and passwordInput == "1234" :
    a = """-----Welcome to MoMo Shop-----
    - Coffee 100 THB
    - Sugar 50 THB
    - Cream 30 THB
    Please choose product"""
    print(a)
    b = int(input("Coffee :"))
    c = int(input("Sugar :"))
    d = int(input("Cream :"))
    coffeePrice = 100
    sugarPrice = 50
    creamPrice = 30
    e = (b * coffeePrice + c * sugarPrice + d * creamPrice)
    print("List of Product")
    print("Coffee", b, "pcs :", b * coffeePrice, "THB")
    print("Sugar", c, "pcs :", c * sugarPrice, "THB")
    print("Cream", d, "pcs :", d * creamPrice, "THB")
    print("-------------------")
    print("Total :", e, "THB")
    print("-----Thank You-----")
else:
    print("Wrong Password pleas try again!")





