n=int(input("Enter n:"))
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(n)