s= input("Enter a sentence to count vowels and consonents: ").lower()
vowels ="aeiou"
c=0
v=0
for i in s:
    if i in vowels:
        v+=1
    else:
        c+=1
print(f"Vowels={v}\nConsonents={c}")
