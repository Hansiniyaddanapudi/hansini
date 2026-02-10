sentence=input("enter a sentence: ")
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1 
print("number of vowels:", vowel_count)
print("number of consonants:", consonant_count)
