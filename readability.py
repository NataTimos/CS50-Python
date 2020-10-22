from cs50 import get_string

# getting text from a user

text = get_string("Text: ")

letters = 0
words = 1
sentences = 0
index = 0
l = 0.0
s = 0.0

# counting letters, words, sentences

for i in range(len(text)):
    if ord(text[i]) >= 65 and ord(text[i]) <= 90 or ord(text[i]) >= 97 and ord(text[i]) <= 122:
        letters += 1
    if ord(text[i]) == 32:
        words += 1
    if ord(text[i]) == 46 or ord(text[i]) == 33 or ord(text[i]) == 63:
        sentences += 1

# l is the average number of letters per 100 words in the text

l = letters * 100.0 / words

# s is the average number of sentences per 100 words in the text

s = sentences * 100.0 / words

# Coleman-Liau index formula

index = round(0.0588 * l - 0.296 * s - 15.8)
# print(index)

# print Coleman-Liau index
if index < 1:
    print("Before Grade 1")
if index == 1:
    print("Grade 1")
    
if index == 2:
    print("Grade 2")
    
if index == 3:
    print("Grade 3")
    
if index == 4:
    print("Grade 4")
    
if index == 5:
    print("Grade 5")
    
if index == 6:
    print("Grade 6")

if index == 7:
    print("Grade 7")

if index == 8:
    print("Grade 8")

if index == 9:
    print("Grade 9")

if index == 10:
    print("Grade 10")

if index == 11:
    print("Grade 11")

if index == 12:
    print("Grade 12")

if index == 13:
    print("Grade 13")

if index == 14:
    print("Grade 14")

if index == 15:
    print("Grade 15")

if index >= 16:
    print("Grade 16+")
