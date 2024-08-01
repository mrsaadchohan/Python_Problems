# Remove Duplicates

# mylist=[1,2,3,4,5,4,4,3,]
# mylis=list(dict.fromkeys(mylist))
# print(mylis)


# Remove Duplicate from string

def remove(input):
    seen=[]
    result=[]
    for char in input:
        if char not in seen:
            seen.append(char)
            result.append(char)
    return ''.join(result)
input="SaadChohan"
output=remove(input)
print(output)