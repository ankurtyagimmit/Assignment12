#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
N=int(input("Enter a number"))
n=1
while n<=N:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
        print(n,end='\n')
        
    n+=1