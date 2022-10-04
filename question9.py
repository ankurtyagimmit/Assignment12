#9. Write a python script to calculate LCM of two numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    m1=a
else:
    m1=b
while(True):#Here we can also replace True in 1 
    if(m1%a==0 and m1%b==0):
        print("LCM is:",m1)
        break
    m1=m1+1
