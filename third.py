string=input("Enter a string:")
vowels="aeiouAEIOU"
print("vowels in the string are:")
for char in string:
    if char in vowels:
        print(char,end="")
    

