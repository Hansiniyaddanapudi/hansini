num=[26,33,45,18,84,162]
even_count=0
odd_count=0
for num in num:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers counts",even_count)
print("odd numbers counts",odd_count)            