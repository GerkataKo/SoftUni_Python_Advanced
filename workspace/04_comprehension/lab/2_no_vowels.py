list_of_vowels=['a', 'o', 'u', 'e', 'i']
text=input()
no_vowels="".join([x for x in text if x.lower() not in list_of_vowels])
print(no_vowels)