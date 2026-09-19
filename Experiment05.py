#Write Python programs to perform string processing operations, including character replacement,
#string reversal, checking palindromes, and counting character and word frequencies.

#Character Replacement
text = input("Enter a string: ")
old = input("Enter the character to be replaced: ")
new = input("Enter the new character: ")
result = text.replace(old, new)
print("String after replacement:", result)

#String Reversal
text = input("Enter a string to reverse: ")
print("Reversed string:", text[::-1])

#Palindrome Check
text = input("Enter a string : ")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Character Frequency Count
text = input("Enter a string:")
ch = input("Enter Character:")
print("Frequency:",text.count(ch))

#Word Frequency Count
text = input("Enter a string:")
word = input("Enter Word:")
words = text.split()
print("Frequency:", words.count(word))