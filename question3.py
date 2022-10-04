#3. Write a python script to print all Prime numbers under 100
n=1
while n<=100:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
        print(n,end='\n')
        
    n+=1
        
        


