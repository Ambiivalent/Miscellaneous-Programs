def atbashCipher(text):
    alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    finalText = ""

    for character in text:
        if character == " ": finalText += character
        elif character.isupper(): 
            finalText += alphabet[(len(alphabet)-1) - alphabet.index(character.lower())].upper()
        elif not character in alphabet: finalText += character
        else:
            finalText += alphabet[(len(alphabet)-1) - alphabet.index(character.lower())]
    
    return finalText

print(atbashCipher("apple"))
print(atbashCipher("Hello World"))
print(atbashCipher("Christmas is the 25th of December"))

print('-' * 50)

print(atbashCipher("zkkov"))
print(atbashCipher("Svool Dliow"))
print(atbashCipher("Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"))
