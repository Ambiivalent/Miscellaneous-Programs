
def ceasarCipher(string, step, mode="encrypt"):
    if mode.lower() == "encrypt": step *= -1
    newString = ""
    counter = 0
    alphabets = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    for character in string:
        while character in alphabets:
            if character == alphabets[counter]:
                newString += alphabets[(counter+step) % len(alphabets)]
                counter = 0
                break
            counter += 1
    return newString

print(ceasarCipher("hello", 12))
print(ceasarCipher("vszzc", 12,"decipher"))
