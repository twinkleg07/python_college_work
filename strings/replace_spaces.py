s=input("Enter a sentence to remove extra spaces: ")
a=s[0]
for i in range(1,len(s)):
    if s[i]==" " and s[i-1] == " ":
        pass
    else:
        a+=s[i]
print(a)
