print("Program to print pyramid ")
size = int(input("Please enter pyramid size :"))
print("Input") ,print(size) ,print("Output")
for i in range (size):
    print(" " * (size-(i-1)) + "*" * (i*2+1))