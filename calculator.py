# First Project: Simple Calculator
num1=float(input("Enter the First Number"))
num2=float(input("Enter the Second Number"))
print("Select One of the Operations from given below:")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice from 1 to 4 ="))
if choice == 1:
    print("Sum of num1 & num2 is :", num1+num2)
    
elif choice == 2:
    print("subtraction of num1 & num2 is :", num1-num2)

elif choice == 3:
    print("multiplication of num1 & num2 is :", num1*num2)

elif choice == 4:
    print("divison of num1 & num2 is :", num1/num2)
else :
    print("Invalid Number")
