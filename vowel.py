# Check if a single letter is a vowel or consonant
ch = input("Enter a single letter: ").strip().lower()
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet letter.")
else:
    if ch in 'aeiou':
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")
