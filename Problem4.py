# Largest Number

def largest_Number(n1,n2,n3):
    if(n1>n2) and (n1>n3):
        return n1
    elif(n2 > n3) and (n2 > n1):
        return n2
    else:
        return n3
                                         
numbers=largest_Number(12,32,43)
print(f"The largest is {numbers}")