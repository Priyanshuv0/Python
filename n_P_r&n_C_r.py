n=int(input("Enter n:"))
r=int(input("Enter r:"))
def fact(n):
    if n<0:
        return
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def n_P_r(n,r):
    if n<r:
        return
    elif n==r:
        return fact(n)
    else:
        return fact(n)/fact(n-r)
def n_C_r(n,r):
    if n<r:
        return
    elif n==r:
        return 1
    else:
        return fact(n)/(fact(n-r)*fact(r))
print(f"The value of nPr={n_P_r(n,r)}")
print(f"The value of nCr={n_C_r(n,r)}")