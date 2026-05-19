print("Palindrome is a sequence (string, number, or list) that reads the same forward and backward,eg 101,MOM\n\n")

n=input("Enter string to check if its Palindrome or not: ").lower()   

rev=''

for ch in n:
    rev=ch+rev
  
if rev==n:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")
