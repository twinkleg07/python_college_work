n=int(input("Enter number to check if its prime or not: "))
if n<=1:
    print("Not Prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break
