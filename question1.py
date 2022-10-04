#1. Write a python script to reverse a number.
N=int(input("Enter a number:"))
revers=0
while N!=0:
    Num=N%10
    revers=revers*10+Num
    N//=10
print("Reverse is:" +str(revers))
    
