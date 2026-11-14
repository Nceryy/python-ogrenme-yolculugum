myCharacter=input("Enter a character: ")
if len(myCharacter) !=1:
    print("Please enter only one character.")
else:
    if myCharacter.isalpha():
        if myCharacter.isupper():
            case="uppercase"
        else:
            case="lowercase"

        vowels="AEIOUaeiou"
        if myCharacter in vowels:
            letter_type="vowel" #sesli harf
        else:
            letter_type="consonant" #sessiz harf

        print(f"The character '{myCharacter}' is an {case} {letter_type}.")
    else:
        print(f"The character '{myCharacter}' is not a letter.")
