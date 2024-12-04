n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    print("(",i,"^",i,")","/",i,end=" + ")
    s=((i**i)/i)                           #s=i**(i-1) can also be used
    sum+=s
print(end="\n")        
print(f"The sum of the above series={sum}")