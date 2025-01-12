
def MessageToEncode():
    print ("What message would you like to encode?")
    print (Cypher())

def Cypher():
    text = str(input()).lower
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in text:
        char = alphabet.find(x)
        new_char = 