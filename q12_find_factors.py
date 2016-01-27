i = int(input("Enter an integer: "))
a = []

for x in range (2,i):
    
   while i % x == 0:
       a.append(x)
       i /= x   

print(a)
