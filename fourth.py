s=input("enter a strinf:")
result=""
for ch in s:
    if ch not in result:
        result += ch
print("string after removing duplicates:",result)
        