#6. Write a python script to print first N prime numbers
N=int(input("Enter any N number"))
n=1
while n<=N+1:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
        print(n,end='\n')
        
    n+=1
