#10. Write a python script to calculate HCF of two numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 =num1- num2
    else:
        num2=num2- num1

print("Hcf of", a, "and", b, "is", num1)
