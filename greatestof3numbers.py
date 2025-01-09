a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
c=int(input("Enter third Number:"))
if(a>=b and a>=c):
    num=a
elif(b>=c):
    num=b
else:
    num=c
print("The greatest number is",num)