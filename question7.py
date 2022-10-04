#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
import math

n1=int(input("Enter a number:"))
n2=int(input("Enter second number;"))
def coprime(n1,n2):
    mt=math.gcd(n1,n2)
    
    if mt==1:
        print(n1,"and",n2,"are co-prime number")
    else:
        print(n1,"and",n2,"are not co-prime number")
coprime(n1,n2)
