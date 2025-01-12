
def MessageToEncode():
    print ("What message would you like to encode?")
    Cypher()
    

def Cypher():
    text = str(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_char = ""
    for i in text:
        new_char += alphabet[alphabet.find(i) + 3]    
    print (new_char)

MessageToEncode()