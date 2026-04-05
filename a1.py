word = input ("Enter a word:")
for ch in word:
    if (ch == 'A' or ch == 'E' or ch == 'O' or ch =='U'):
        print ("Vowel found")
        break
    else:
        print("Vowel not found")