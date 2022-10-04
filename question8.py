
num = int(input("Enter the Range Number: "))
val1 = 0
val2 = 1
for n in range(0, num):
           if(n <= 1):
                      next = n
           else:
                      next = val1 + val2
                      val1 = val2
                      val2 = next
                      print(next)

