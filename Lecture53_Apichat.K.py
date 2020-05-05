price = float(input("Please enter Price :"))
def vatCalcurate(price):
    total = (price+(price*7/100))
    return total
print("Price: " +str(price) + "\nVat: " + str(vatCalcurate(price)-price) + "\nTotal: " + str(vatCalcurate(price)))