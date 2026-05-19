n= int(input("Enter a number to generate fibonacci series: "))

fibo=[] 

for i in range (n+1):
    if i==0:
        fibo.append(0)
    elif i==1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1]+fibo[i-2])
      
print(fibo)
