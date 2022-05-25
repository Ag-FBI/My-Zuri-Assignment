# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
# [assignment] Add your code here



word1 = input ("Enter your first word : ")
word2 = input ("Enter your second word : ")

word1 = word1.lower()
word2 = word2.lower()

if(len(word1) == len(word2)):
    sword1 = sorted(word1)
    sword2 = sorted(word2)
    
    if (sword1 == sword2):
        print("True")


else:
    print("False")



