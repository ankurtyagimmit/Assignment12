
#2. Write a python script to check whether a given number is Prime or not
N = int(input("Enter a number to check prime or not prime : "))
count=0
for i in range(1,N+1):
    if N%i==0:
        count+=1
if count==2:
    print(N,"is a prime number")
else:
    print(N,"is not a prime nuber")
        


