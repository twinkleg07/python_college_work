s= input("Enter a sentence to count vowels and consonents: ").lower()
vowels ="aeiou"
c=""
v=""
for i in s:
    if i in vowels:
        v+=i
    else:
        c+=i
print(f"Vowels={v}\nConsonents={c}")
