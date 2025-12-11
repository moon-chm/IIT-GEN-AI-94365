str=input("Enter a string: ")
#print string direct 
print("String :",str)
#print length of string
print("length of string: ",len(str))
#count number of words and vowels in string
words=str.split()  
print("Number of words in string: ",len(words))
#vowel count    
volwels=0
for char in str:
    if char.lower() in 'aeiou':
        volwels+=1
print("Number of vowels in string: ",volwels) 