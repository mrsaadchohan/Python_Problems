# Factorial

product=1
n=12
if(n<0):
        print("Negative Factorial doesnot exist")
elif(n==0):
        print("Factorial of 0 is 1")
else:
        for i in range(1,n+1):
            product *=i
        print(f"The factorail of {n} is  {product}")
