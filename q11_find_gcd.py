n1 = int(input("Enter a positive integer: "))
n2 = int(input("Enter another positive integer: "))

a = [n1, n2]

a.sort()

gcd = a[0]

while a[0] % gcd != 0 or a[1] % gcd !=0:
    gcd -= 1

print("The greatest common divisor is", gcd)
