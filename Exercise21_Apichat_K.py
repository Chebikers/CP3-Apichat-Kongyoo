from tkinter import *
import math
def leftClickButton(event):
    total = int(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100, 2))
    print(int(total))
    if total >= 30:
        labelTotal.configure(text="อ้วนมาก")
    elif total >= 25.0:
        labelTotal.configure(text="อ้วน")
    elif total >= 23.0:
        labelTotal.configure(text="น้ำหนักเกิน")
    elif total >= 18.6:
        labelTotal.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelTotal.configure(text="ผอมเกินไป")
MainWindows = Tk()
labelHight = Label(MainWindows, text = "ส่วนสูง (Cm.)")
labelHight.grid(row = 0 ,column = 0)
textBoxHight = Entry(MainWindows)
textBoxHight.grid(row = 0 , column = 1)
labelWeight = Label(MainWindows, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row = 1 ,column = 0)
textBoxWeight = Entry(MainWindows)
textBoxWeight.grid(row = 1, column = 1)
calculateButton = Button(MainWindows, text = "คำนวณ")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row = 2)
labelTotal = Label(MainWindows , text = "ผลลัพธ์")
labelTotal.grid(row = 2 ,column = 1)

MainWindows.mainloop()