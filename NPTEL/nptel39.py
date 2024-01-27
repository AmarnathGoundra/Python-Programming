""" ANAGRAM """

str1=input("Enter the first string\n")
str2=input("Enter the secong string\n")
if(sorted(str1)==sorted(str2)):
    print("These are anagrams")
else:
    print("These are not anagrams")