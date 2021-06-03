#unicode characters
with open("unicodeAlphabet-Py.txt", "a",encoding="UTF-8") as unicodeAlphabet:
    for i in range(55295):
        uniCharacter = chr(i)
        print(uniCharacter,end='',file = unicodeAlphabet)
    for i in range(57900,65994):
        uniCharacter = chr(i)
        print(uniCharacter,end='',file = unicodeAlphabet)
    # for i in range(65537):
    #     uniCharacter = chr(i)
    #     print(uniCharacter,end='',file = unicodeAlphabet)
    # for i in range(129):
    #     uniCharacter = chr(i)
    #     print(uniCharacter,end='',file = unicodeAlphabet)
    unicodeAlphabet.close()