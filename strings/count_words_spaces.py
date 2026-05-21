s= input("Enter a sentence to count words and spaces: ")
space=0
word=0
for i in s:
    if i== " ":
        space+=1
        word = space+1
print(f"Space in sentence= {space}\nWords in sentence= {word}")
