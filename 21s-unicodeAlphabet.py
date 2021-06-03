#unicode characters
#unicodeAlphabet-Py.txt does not have text wrapping.  
#unicodeAlphabet-Py.txt has text wrapping.  
#unicodeAlphabet-Py.txt
import textwrap
with open("unicodeAlphabet-Py.txt", "w",encoding="UTF-8") as unicodeAlphabet:
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
with open("unicodeAlphabet-Py.txt", "r",encoding="UTF-8") as unicodeAlphabet:
    x = unicodeAlphabet.read()
    with open("unicodeAlphabet-Py-wrapped.txt","w",encoding="UTF-8") as unicodeWrap:
        print("\n".join(textwrap.wrap(x,100)),file=unicodeWrap)
    unicodeWrap.close()
    unicodeAlphabet.close()