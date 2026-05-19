print("A perfect number is a positive integer that equals the sum of its proper divisors (excluding the number itself)\n.")
print("For example, 6 is a perfect number because its proper divisors 1,2,3 add up to exactly 6, 1 + 2 + 3 = 6. \n\n")

n=int(input("Enter a number to check if its Perfect or not: "))

s=0

for i in range(1,n):
    if n % i == 0:
        s+=i
        
if s==n:
    print("Perfect number")
else:
    print("Not a Perfect number")
